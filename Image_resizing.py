from PIL import Image


def image_resizing(image, size, name='output.jpg', format=None):
    image.thumbnail(size)
    image.save(name, format)


if __name__ == '__main__':
    img = Image.open('JPG_files/pikachu.jpg')
    image_resizing(img, (100, 100), 'resized.png', 'png')
