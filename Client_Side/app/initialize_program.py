from PIL import Image
import jsons

from .user_input.user_input import user_input
from .image_operations.display import display_image
from api_client.image_serialization import ImageSerialization
from api_client.sending_data import sending_data
from api_client.login import login



class InitializeProgram():

    def __init__(self):
        #Must be hidden
        username = "client"
        password = "secret_password"
        #Must be hidden

        self.token = self.login(username, password)


    def start(self):

        try:
            user_data = user_input()
            face_image = Image.open(user_data["image_path"])
            serialized_data = self.serialize(face_image, user_data)

            response = sending_data(serialized_data, self.token)

            serialized_coordinates = self.process_response(response)
            coordinates = self.deserialize(serialized_coordinates)

            if coordinates == []:
                raise ValueError('No coordinates were found')

            display_image(face_image, coordinates)

        except (OSError, IOError) as error:
            print(f"Wrong file path, please try again: {error}")
        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")


    def login(self, username, password):
        return login(username, password)


    def process_response(self, response):

        if response.status_code != 200:
            raise Exception("File haven't received due the error")

        json_response_data = response.json()
        received_response = json_response_data['response']
        serialized_coordinates = json_response_data['coordinates']

        self.display_response(received_response)

        return serialized_coordinates


    def serialize(self, face_image, user_data):
        serialized_info = ImageSerialization(face_image, user_data).serialize()
        return serialized_info


    def deserialize(self, serialized_coordinates):
        coordinates = jsons.load(serialized_coordinates)
        return coordinates


    def display_response(self, received_response):
        print(received_response)