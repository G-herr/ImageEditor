from PIL import Image


def image_rotator(image, angle, name='output.jpg', format=None):
    rotated_image = image.rotate(angle)
    rotated_image.save(name, format)


if __name__ == '__main__':
    img = Image.open('JPG_files/pikachu.jpg')
    image_rotator(img, 90, 'rotated.png', 'png')
