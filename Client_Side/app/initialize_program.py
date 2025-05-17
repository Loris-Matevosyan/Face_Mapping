from PIL import Image
import jsons

from api_client.rest_client import rest_client
from .user_input.user_input import user_input
from .image_operations.display import display_image



class InitializeProgram:

    def start(self):

        try:
            user_data = user_input()
            face_image = Image.open(user_data["image_path"])

            coordinates = rest_client.process_data(face_image, user_data)

            if coordinates == []:
                raise ValueError('No coordinates were found')

            display_image(face_image, coordinates)

        except (OSError, IOError) as error:
            print(f"Wrong file path, please try again: {error}")
        except ValueError as error:
            print(f"Error: {error}")
        except Exception as error:
            print(f"Error: {error}")