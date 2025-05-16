from PIL import Image
import jsons

import base64
import io


class Serializer:

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


serializer = Serializer()