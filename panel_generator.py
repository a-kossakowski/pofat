from PIL import Image, ImageDraw, ImageFont

def generate_panel(images, grid_layout, h_space, v_space, h_margin, v_margin, label_pos):
    # split grid layout to cols and rows
    cols, rows = map(int, grid_layout.split('x'))
    
    # calculate max width and height from provided images
    max_width = max(img.width for img in images)
    max_height = max(img.height for img in images)
    # calculate total panel size
    total_width = cols * max_width + (cols - 1) * h_space + 2 * h_margin
    total_height = rows * max_height + (rows - 1) * v_space + 2 * v_margin
    
    # create new blank panel image
    panel_img = Image.new('RGB', (total_width, total_height), 'white')
    
    # set font size and load font
    font_size = 40
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()  # default font if specific not found
    
    draw = ImageDraw.Draw(panel_img)  # create drawing object
    
    x_offset, y_offset = h_margin, v_margin  # initialize offsets
    
    for i, img in enumerate(images):
        label = chr(65 + i)  # generate label A, B, C, ...
        
        # calculate text position based on label_pos parameter
        if label_pos == "Top Left":
            text_position = (x_offset + 10, y_offset + 10) 
        elif label_pos == "Top Right":
            text_position = (x_offset + max_width - font_size * 2, y_offset + 10)  
        elif label_pos == "Bottom Left":
            text_position = (x_offset + 10, y_offset + max_height - font_size - 10)  
        elif label_pos == "Bottom Right":
            text_position = (x_offset + max_width - font_size * 2, y_offset + max_height - font_size - 10) 
        
        # paste current image into panel
        panel_img.paste(img, (x_offset, y_offset))
        # draw label on image
        draw.text(text_position, label, fill=(0, 0, 0), font=font)
        
        # update x_offset, reset and update y_offset after each row
        x_offset += max_width + h_space
        if (i + 1) % cols == 0:
            x_offset = h_margin
            y_offset += max_height + v_space
            
    return panel_img

