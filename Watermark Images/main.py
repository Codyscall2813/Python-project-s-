from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text, position, offset=10):
    try:
        # Open the original image
        original = Image.open(input_image_path).convert("RGBA")
        print(f"Opened image: {input_image_path}")
    except FileNotFoundError:
        print(f"Error: The file '{input_image_path}' was not found.")
        return
    
    # Make the image editable
    txt = Image.new("RGBA", original.size, (255, 255, 255, 0))
    
    # Choose a font and size
    try:
        font = ImageFont.truetype("Collection/Watermark Images/Mali-Regular.ttf", 36)
        print(f"Using font: Collection/Watermark Images/Mali-Regular.ttf")
    except IOError:
        print("Error: Font file not found or cannot be opened.")
        return
    
    # Initialize ImageDraw
    draw = ImageDraw.Draw(txt)
    
    # Get the bounding box of the text and position it
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    if position == 'bottom_right':
        text_position = (original.size[0] - text_width - 10, original.size[1] - text_height - 10 - offset)
    elif position == 'bottom_left':
        text_position = (10, original.size[1] - text_height - 10 - offset)
    elif position == 'top_right':
        text_position = (original.size[0] - text_width - 10, 10 - offset)
    elif position == 'top_left':
        text_position = (10, 10 - offset)
    else:
        text_position = (10, 10 - offset)  # Default to top-left if position is not specified

    print(f"Watermark text: '{watermark_text}'")
    print(f"Position: {position}")
    print(f"Adjusted position: {text_position}")
    
    # Apply the watermark with the specified color and full opacity
    watermark_color = (187, 20, 34, 255)  # RGBA with full opacity
    draw.text(text_position, watermark_text, fill=watermark_color, font=font)
    
    # Combine the original image with the watermark
    watermarked = Image.alpha_composite(original, txt)
    
    # Save the result
    watermarked = watermarked.convert("RGB")  # Convert to RGB before saving
    watermarked.save(output_image_path, "JPEG")
    print(f"Watermarked image saved as: {output_image_path}")

# Example usage
input_image_path = "Collection/Watermark Images/Page 1.png"
output_image_path = "Collection/Watermark Images/watermarked.jpg"
watermark_text = "@pycode.hubb"
position = "bottom_right"  # Options: bottom_right, bottom_left, top_right, top_left

add_watermark(input_image_path, output_image_path, watermark_text, position, offset=25)
