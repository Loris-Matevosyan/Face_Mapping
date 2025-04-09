from flask import request
from flask_restful import Resource, abort, reqparse
from flask_jwt_extended import get_jwt_identity, jwt_required
from PIL import Image
import jsons

from pathlib import Path
import base64
import io
import os

from main import findLandmarksCoordinates



class ProcessImage(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('first_name')
        self.parser.add_argument('last_name')
        self.parser.add_argument('age')
        self.parser.add_argument('image')
        self.parser.add_argument('file_extension')
        self.parser.add_argument('face_region')


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

        self.arguments = self.parser.parse_args()
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


