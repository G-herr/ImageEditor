from PIL import Image, ImageFilter


def filter_applier(image, function, name='output.jpg', format=None):
    filtered_img = image.filter(function)
    filtered_img.save(name, format)


if __name__ == '__main__':
    img = Image.open('JPG_files/pikachu.jpg')
    filter_applier(img, ImageFilter.BLUR, 'blur.png', 'png')

'''
Filters:
BLUR
CONTOUR
DETAIL
EDGE_ENHANCE
EDGE_ENHANCE_MORE
EMBOSS
FIND_EDGES
SHARPEN
SMOOTH
SMOOTH_MORE
'''
