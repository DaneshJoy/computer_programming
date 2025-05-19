from PIL import Image, ImageEnhance

# خواندن تصویر
image = Image.open("old.jpg")

# نمایش تصویر
image.show()

# Enhance brightness
brightness_enhancer = ImageEnhance.Brightness(image)
# Increase brightness (1.0 means no change)
image_b = brightness_enhancer.enhance(2)

# image_b.show()

# Enhance contrast
contrast_enhancer = ImageEnhance.Contrast(image_b)
# Increase contrast
image_c = contrast_enhancer.enhance(1.2)  

# image_c.show()

# Enhance color
color_enhancer = ImageEnhance.Color(image_c)
 # Increase color intensity
image_cc = color_enhancer.enhance(3) 

image_cc.show()


image_cc.save('reslut.png')
image_cc.save("result_2.jpg", format="JPEG", quality=95, optimize=True)
