from PIL import Image
import numpy as np
import cv2

from app.image_operations.resizing import resize_image


def display_image(image: Image.Image, coordinates):

    image = resize_image(image)

    np_array = np.asarray(image, dtype=np.uint8)
    np_array = cv2.cvtColor(np_array, cv2.COLOR_RGB2BGR)

    for x, y in coordinates:
        cv2.circle(np_array, (x,y), radius=1, color=(255, 0, 0), thickness=-1)

    while True:
        cv2.imshow("FaceLandmarks", np_array)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cv2.destroyAllWindows()