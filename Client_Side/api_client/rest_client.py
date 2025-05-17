from PIL import Image
import requests
import jsons

from .login import login
from .post_access import post_access
from .image_serialization import ImageSerialization


class RestClient:

    def __init__(self):
        #Must be hidden
        username = "client"
        password = "secret_password"
        #Must be hidden

        self.token = self.login(username, password)


    def login(self, username, password):
        return login(username, password)


    def process_data(self, face_image: Image.Image, user_data):
        serialized_data = self.serialize(face_image, user_data)

        response = self.sending_data(serialized_data, self.token)

        serialized_coordinates = self.process_response(response)
        coordinates = self.deserialize(serialized_coordinates)

        return coordinates


    def sending_data(self, serialized_data, token):
        response = post_access(serialized_data, token)

        print(response.status_code)
        print(response.reason)

        return response


    def process_response(self, response):

        if response.status_code != 200:
            raise Exception("File haven't received due the error")

        json_response_data = response.json()
        received_response = json_response_data['response']
        serialized_coordinates = json_response_data['coordinates']

        self.display_response(received_response)

        return serialized_coordinates


    def display_response(self, received_response):
        print(received_response)


    def serialize(self, face_image, user_data):
        serialized_info = ImageSerialization(face_image, user_data).serialize()
        return serialized_info


    def deserialize(self, serialized_coordinates):
        coordinates = jsons.load(serialized_coordinates)
        return coordinates



rest_client = RestClient()