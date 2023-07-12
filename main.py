from os import listdir, makedirs
from os.path import isfile, join, getsize
from shutil import copyfile
from PIL import Image
import logging

# Define constants
LOG_FILE = './status.log'
SRC_PATH = './source_images'
DEST_PATH = './images'
MIN_SIZE = 10**5  # Minimum size of image in bytes

# Create logger
log_format = '%(levelname)s:%(asctime)s: %(message)s'
logger = logging.basicConfig(format=log_format, filename=LOG_FILE, encoding='utf-8', level=logging.INFO)

try:
    # Create destination subfolders
    makedirs(join(DEST_PATH, 'horizontal'), exist_ok=True)
    makedirs(join(DEST_PATH, 'vertical'), exist_ok=True)

    # Get all images from the source path that are larger than MIN_SIZE
    files = [f for f in listdir(SRC_PATH) if isfile(join(SRC_PATH, f)) and getsize(join(SRC_PATH, f)) > MIN_SIZE]
    # Iterate over all images
    for file in files:
        # Open image
        img = Image.open(join(SRC_PATH, file))
        # Get image size
        w, h = img.size
        # Close image
        img.close()
        # Copy image to destination path depending on orrientation
        copyfile(join(SRC_PATH, file), join(DEST_PATH, 'horizontal' if w > h else 'vertical', file + '.jpg'))

    # Log success
    logging.info(f'Successfully copied {len(files)} images')

except Exception as e:
    # Log error
    logging.error(e)
