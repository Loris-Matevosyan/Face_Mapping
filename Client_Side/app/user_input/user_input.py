from pathlib import Path
import os


def user_input():

    file_name = input('Enter file name: ')
    region_detect = int(input(face_region_to_choose()))

    if region_detect < 1 or region_detect > 13:
        raise ValueError("Wrong region chosen, must be between 1 and 13")

    image_path = find_file_path(file_name)
    face_region = find_face_region(region_detect)

    return { "image_path" : image_path, "face_region" : face_region }


def face_region_to_choose():

    region_choice = (
        'Please choose from the following regions to capture'
        '\nAll - 1'
        '\nForehead - 2'
        '\nEyebrows - 3    Left eyebrow - 4     Right eyebrow - 5'
        '\nEyes - 6        Left eye - 7         Right eye - 8'
        '\nCheekbones - 9  Left cheekbone - 10  Right cheekbone - 11'
        '\nNose - 12'
        '\nLips - 13'
        '\nChoose: ')

    return region_choice


def find_file_path(file_name):

    current_directory = os.getcwd()
    image_path = Path(current_directory) / 'Images' / file_name

    return image_path


def find_face_region(region_choice):

    region = None

    if region_choice == 1:
        region = "All"
    elif region_choice == 2:
        region = "Forehead"
    elif region_choice == 3:
        region = "Eyebrows"
    elif region_choice == 4:
        region = "Left eyebrow"
    elif region_choice == 5:
        region = "Right eyebrow"
    elif region_choice == 6:
        region = "Eyes"
    elif region_choice == 7:
        region = "Left eye"
    elif region_choice == 8:
        region = "Right eye"
    elif region_choice == 9:
        region = "Cheekbones"
    elif region_choice == 10:
        region = "Left cheekbone"
    elif region_choice == 11:
        region = "Right cheekbone"
    elif region_choice == 12:
        region = "Nose"
    elif region_choice == 13:
        region = "Lips"

    return region