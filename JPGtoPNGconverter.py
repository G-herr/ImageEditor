from PIL import Image
import sys
import os

'''
Converts all jpg files from a folder to png. 
Must provide folder path with jpg files and new path for generated png files.
Paths must have format "./path"
'''


# Get agruments from terminal
_, image_path, new_folder = sys.argv

# Check if Image path exists
if os.path.exists(image_path):

    # Get current path
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    new_path = os.path.join(parent_dir, new_folder)

    # Check if new folder already exists, if not, create it
    if os.path.exists(new_path) == False:
        os.mkdir(new_path)
        print('Path created!')

    directory = os.fsencode(image_path)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg"):
            img = Image.open(parent_dir + image_path + '\\' + filename)
            new_file_path = new_path + '\\' + filename[:-4] + '.png'
            img.save(new_file_path, 'png')

else:
    print('Path does not exists!')

# img = Image.open('JPG_files/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save('blur.png', 'png')
