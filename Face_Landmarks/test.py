from PIL import Image
import numpy as np
import cv2
import time

from ProcessImages.processImages import FaceLandmarksDetection
from TestInput.testInput import testInput


face_landmarks_detect = FaceLandmarksDetection()
time.sleep(1)


def drawImage(image, coordinates):
    for x, y in coordinates:
        cv2.circle(image, (x, y), radius=2, color=(255,0,0), thickness=-1)


def displayImage(image):
    while True:
        cv2.imshow("Face", image)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()


while True:
    try:
        file_path, faceRegion = testInput()
    except ValueError as error:
        print(f'Error: {error}')
        continue

    image = None

    try:
        image = Image.open(file_path)
    except OSError as error:
        print(f"Error opening Image: {error}")
        continue

    coordinates = None
    try:
        coordinates = face_landmarks_detect.findCoordinates(image, faceRegion)
    except IOError as error:
        print(f'Error: {error}')

    print(coordinates)

    image_array = np.asarray(image, dtype=np.uint8)
    image_array = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

    drawImage(image_array, coordinates)
    displayImage(image_array)
