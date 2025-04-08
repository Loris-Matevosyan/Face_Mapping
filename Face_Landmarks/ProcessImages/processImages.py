from PIL import Image
import mediapipe as mp
import numpy as np

from Landmarks.faceLandmarks import FaceLandmarks



class FaceLandmarksDetection():

    def __init__(self):

        self.face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1)
        self.face_landmarks = FaceLandmarks()


    def findCoordinates(self, face_image: Image.Image, face_region):

        region_landmarks = self.getRegionLandmarks(face_region)
        coordinates = self.getCoordinates(face_image, region_landmarks)

        return coordinates


    def getRegionLandmarks(self, region):

        region_landmarks = []

        match region:
            case "All":
                region_landmarks = [index for index in range(0,468)]
            case "Forehead":
                region_landmarks = self.face_landmarks.foreheadLandmarks()
            case "Eyebrows":
                region_landmarks = list(self.face_landmarks.leftEyebrowLandmarks())
                region_landmarks.extend(self.face_landmarks.rightEyebrowLandmarks())
            case "Left eyebrow":
                region_landmarks = self.face_landmarks.leftEyebrowLandmarks()
            case "Right eyebrow":
                region_landmarks = self.face_landmarks.rightEyebrowLandmarks()
            case "Eyes":
                region_landmarks = list(self.face_landmarks.leftEyeLandmarks())
                region_landmarks.extend(self.face_landmarks.rightEyeLandmarks())
            case "Left eye":
                region_landmarks = self.face_landmarks.leftEyeLandmarks()
            case "Right eye":
                region_landmarks = self.face_landmarks.rightEyeLandmarks()
            case "Cheekbones":
                region_landmarks = list(self.face_landmarks.leftCheekboneLandmarks())
                region_landmarks.extend(self.face_landmarks.rightCheekboneLandmarks())
            case "Left cheekbone":
                region_landmarks = self.face_landmarks.leftCheekboneLandmarks()
            case "Right cheekbone":
                region_landmarks = self.face_landmarks.rightCheekboneLandmarks()
            case "Nose":
                region_landmarks = self.face_landmarks.noseLandmarks()
            case "Lips":
                region_landmarks = self.face_landmarks.lipsLandmarks()
            case _:
                print("Wrong input")

        return region_landmarks


    def getCoordinates(self, image: Image.Image, region_landmarks):

        region_coordinates = []

        face_image = np.asarray(image)
        height, width, channels = face_image.shape

        results = self.face_mesh.process(face_image)

        if results.multi_face_landmarks:
            face_landmarks = results.multi_face_landmarks[0]

            for index in region_landmarks:
                x = int(face_landmarks.landmark[index].x * width)
                y = int(face_landmarks.landmark[index].y * height)

                region_coordinates.append([x, y])


        return region_coordinates