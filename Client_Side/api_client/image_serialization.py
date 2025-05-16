from PIL import Image
import jsons

import base64
import io

from app.image_operations.resizing import resize_image


class ImageSerialization():

    def __init__ (self, image: Image.Image, user_data):
        self.image = image
        self.user_data = user_data


    def serialize(self):

        self.resizeImage()

        base64_image = self.encodeImage()
        client_info = self.createClientInfo(base64_image)
        serialized_data = jsons.dump(client_info)

        return serialized_data


    def resizeImage(self):

        self.image = resize_image(self.image)


    def encodeImage(self):

        buffer = io.BytesIO()
        self.image.save(buffer, format=self.image.format)
        byte_array_image = buffer.getvalue()

        base64_image = base64.b64encode(byte_array_image).decode('utf-8')

        return base64_image


    def createClientInfo(self, base64_image):

        client_info = {
            "image": base64_image,
            "face_region": self.user_data["face_region"]
        }

        return client_info