from flask import Flask, request, jsonify
from flask_restful import Api, Resource, abort, reqparse
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from waitress import serve
from PIL import Image
import jsons

from pathlib import Path
import base64
import io
import os

from main import findLandmarksCoordinates



app = Flask(__name__)
api = Api(app)
app.config["JWT_SECRET_KEY"] = "super_secret_key"
jwt = JWTManager(app)


parser = reqparse.RequestParser()
parser.add_argument('first_name')
parser.add_argument('last_name')
parser.add_argument('age')
parser.add_argument('image')
parser.add_argument('file_extension')
parser.add_argument('face_region')


#Must be hidden
users = { "client" : "secret_password" }


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if username in users and users[username] == password:

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({ "message" : "Invalid credentials"}), 401


class ProcessImage(Resource):

    @jwt_required()
    def post(self):
        try:
            current_user = get_jwt_identity()
            self.checkReceivedType()

            region_coordinates = self.getFaceCoordinates()
            serialized_coordinates = self.serialize(region_coordinates,
                                           'Image proceeded successfully')

            return serialized_coordinates, 200

        except (ValueError, TypeError, IOError, FileNotFoundError) as error:
            abort(406, answer=f'Error: {error}')
        except Exception as error:
            abort(406, answer=f"General error: {error}")


    def get(self):
        abort(404, answer='Wrong request, nothing to get')


    def delete(self):
        abort(404, message='Wrong request for delete')


    def put(self):
        abort(404, message='Wrong request for put')


    def checkReceivedType(self):
        if request.content_type != 'application/json':
            raise ValueError("Wrong format, use json format")


    def getFaceCoordinates(self):

        serialized_image, face_region = self.parseJsonArguments()
        image = self.deserialize(serialized_image)
        region_coordinates = findLandmarksCoordinates(image, face_region)

        return region_coordinates


    def parseJsonArguments(self):

        self.arguments = parser.parse_args()
        serialized_image = self.arguments['image']
        face_region = self.arguments['face_region']

        return (serialized_image, face_region)


    def deserialize(self, serialized_image):

        deserialized_image = jsons.load(serialized_image)
        base64_image = base64.b64decode(deserialized_image)
        bytes_array_image = io.BytesIO(base64_image)
        image = Image.open(bytes_array_image)

        return image


    def serialize(self, region_coordinates, response):

        serialized_coordinated = jsons.dump({'response': response,
                                             'coordinates': region_coordinates})

        return serialized_coordinated


    def save(self, image):
        file_name = f'{self.arguments['first_name']}_{self.arguments['last_name']}_{self.arguments['age']}.{self.arguments['file_extension']}'
        image.save(Path(os.getcwd()) / '..' / "Images" / file_name)



api.add_resource(ProcessImage, '/image')


if __name__ == '__main__':
    serve(app, host="127.0.0.1", port=5001)



# FOR RECEIVING MULTIPLE IMAGES
# class ReceivedImages(Resource):
# api.add_resource(ReceivedImages, '/images')

# FOR DEBUG MODE
# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5001, debug = True)