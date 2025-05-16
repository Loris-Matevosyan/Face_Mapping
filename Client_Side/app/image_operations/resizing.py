from PIL import Image


def resize_image(image: Image.Image):

    width, height = image.size
    decrease = 1

    if width > 3000 or height > 3000:
        decrease = 5
    elif width > 2000 or height > 2000:
        decrease = 4
    elif width > 1500 or height > 1500:
        decrease = 3
    elif width > 1000 or height > 1000:
        decrease = 2

    width = width // decrease
    height = height // decrease

    format = image.format
    image = image.resize((width, height))
    image.format = format

    return image