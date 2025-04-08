from PIL import Image

from ProcessImages.processImages import FaceLandmarksDetection


def findLandmarksCoordinates(face_image: Image.Image, face_region):

    face_landmarks_detect = FaceLandmarksDetection()

    try:
        region_coordinates = face_landmarks_detect.findCoordinates(face_image, face_region)

        return region_coordinates

    except IOError as error:
        print(f'Error: {error}')
