import os
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt


def adjust_image(img_path, brightness_factor,
                 contrast_factor, color_factor):
    image_in = Image.open(img_path)
        
    # Enhance brightness
    brightness_enhancer = ImageEnhance.Brightness(image_in)
    # Increase brightness (1.0 means no change)
    image_b = brightness_enhancer.enhance(brightness_factor)
    
    # Enhance contrast
    contrast_enhancer = ImageEnhance.Contrast(image_b)
    # Increase contrast
    image_c = contrast_enhancer.enhance(contrast_factor)  
    
    # Enhance color
    color_enhancer = ImageEnhance.Color(image_c)
     # Increase color intensity
    image_out = color_enhancer.enhance(color_factor) 
    
    return image_in, image_out


def show_images_side_by_side(img_before, img_after):
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(img_before, cmap='gray')
    axes[0].set_axis_off()
    axes[0].set_title('Before')
    axes[1].imshow(img_after, cmap='gray')
    axes[1].set_axis_off()
    axes[1].set_title('After')
    plt.tight_layout()
    plt.show()


def save_results(img_after, out_dir, input_file_path):
    # Create output dir
    os.makedirs(out_dir, exist_ok=True)
    # Save results inside output dir
    out_file = os.path.basename(input_file_path)
    name_ext = out_file.split('.')
    filename = os.path.join(out_dir, name_ext[0] + '_processed.' + name_ext[-1])
    img_after.save(filename)
