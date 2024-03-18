from PIL import Image

def resize_image(image_path, target_width, target_height):
    with Image.open(image_path) as img:  # open image
        if img.mode != 'RGB':  # convert non-RGB to RGB
            img = img.convert('RGB')
        # resize using high-quality Lanczos filter
        resized_image = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
        return resized_image

def inches_to_pixels(inches, dpi=300):
    return int(inches * dpi)  # convert inches to pixels

