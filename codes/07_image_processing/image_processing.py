import os
from glob import glob
from utils import adjust_image
from utils import show_images_side_by_side
from utils import save_results

image_paths = glob('images/*.*g')

out_dir = 'results'

for img_path in image_paths: 
    img_before, img_after = adjust_image(img_path, 1.8, 1.2, 1.2)
    show_images_side_by_side(img_before, img_after)
    save_results(img_after, out_dir, img_path)
