# (c) 2020 James M. Tucker

import os
import sys

from PIL import Image
from config import config_hb_images

img_dir = config_hb_images('b19a')

orig_img = 'jp2'

print(f"Processing tif files in: {img_dir}")

os.chdir(img_dir)

for f in os.listdir('.'):
    if f.endswith(orig_img):
        print(f'Converting {f}…')
        i = Image.open(f)
        i = i.convert('1')
        fn, fext = os.path.splitext(f)
        i.save('{}_BW.tif'.format(fn))