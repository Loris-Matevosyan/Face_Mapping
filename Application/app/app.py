from PIL import Image

from .process_images.face_processing import FaceLandmarksDetection


class FindLandmarks:

    def __init__(self):

        self.face_landmarks_detect = FaceLandmarksDetection()


    def process_image(self, image: Image.Image, face_region):

        try:
            region_coordinates = self.find_coordinates(image, face_region)

            return region_coordinates

        except IOError as error:
            print(f'Error: {error}')


    def find_coordinates(self, image, face_region):
        return self.face_landmarks_detect.findCoordinates(image, face_region)


find_landmarks = FindLandmarks()