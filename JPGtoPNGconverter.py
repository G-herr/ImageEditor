from PIL import Image, ImageFilter

img = Image.open('JPG_files/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')
