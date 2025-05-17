from flask import request
from flask_restful import Resource, abort, reqparse
from flask_jwt_extended import get_jwt_identity, jwt_required
from PIL import Image

from api.serialization.serializer import serializer
from app.app import find_landmarks


class ProcessImage(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('image', location='json')
        self.parser.add_argument('face_region', location='json')


    @jwt_required()
    def post(self):
        try:
            # Can do authorization
            current_user = get_jwt_identity()
            # Can do authorization

            self.checkReceivedType()
            serialized_image, face_region = self.parseJsonArguments()

            image = self.deserialize(serialized_image)
            region_coordinates = self.get_coordinates(image, face_region)

            response = self.get_response(region_coordinates)
            serialized_coordinates = self.serialize(region_coordinates, response)

            return serialized_coordinates, 200

        except (ValueError, TypeError, IOError, FileNotFoundError) as error:
            abort(406, answer=f'Error: {error}')
        except Exception as error:
            abort(406, answer=f"General error: {error}")


    def checkReceivedType(self):
        if request.content_type != 'application/json':
            raise ValueError("Wrong format, use json format")


    def parseJsonArguments(self):

        self.arguments = self.parser.parse_args()
        serialized_image = self.arguments['image']
        face_region = self.arguments['face_region']

        return (serialized_image, face_region)


    def get_response(self, region_coordinates):

        if region_coordinates != []:
            response = 'Image proceeded successfully'
        else:
            response = 'Face is not recognized'

        return response


    def deserialize(self, serialized_image):
        return serializer.deserialize(serialized_image)


    def serialize(self, region_coordinates, response):
        return serializer.serialize(region_coordinates, response)


    def get_coordinates(self, image, face_region):
        return find_landmarks.process_image(image, face_region)








