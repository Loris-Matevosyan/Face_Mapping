from PIL import Image
import jsons

from UserInput.userInput import userInput
from Serialization.imageSerialization import ImageSerialization
from Network.sendingImage import sendingData
from Network.login import login
from DisplayImage.displayImage import displayImage



class InitializeProgram():

    def __init__(self):
        #Must be hidden
        self.username = "client"
        self.password = "secret_password"

        self.token = login(self.username, self.password)


    def start(self):

        try:
            user_data = userInput()
            face_image = Image.open(user_data["image_path"])
            serialized_data = self.serialize(face_image, user_data)

            response = sendingData(serialized_data, self.token)

            serialized_coordinates = self.processResponse(response)
            coordinates = self.deserialize(serialized_coordinates)

            if coordinates == []:
                raise ValueError('No coordinates were found')

            self.displayCoordinates(coordinates)

            displayImage(face_image, coordinates)

        except (OSError, IOError) as error:
            print(f"Wrong file path, please try again: {error}")
        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")


    def processResponse(self, response):

        if response.status_code != 200:
            raise Exception("File haven't received due the error")

        json_response_data = response.json()
        received_response = json_response_data['response']
        serialized_coordinates = json_response_data['coordinates']

        self.displayResponse(received_response)

        return serialized_coordinates


    def serialize(self, face_image, user_data):
        serialized_info = ImageSerialization(face_image, user_data).serialize()
        return serialized_info

    def deserialize(self, serialized_coordinates):
        coordinates = jsons.load(serialized_coordinates)
        return coordinates


    def displayResponse(self, received_response):
        print(received_response)

    def displayCoordinates(self, coordinates):
        print(coordinates)




















