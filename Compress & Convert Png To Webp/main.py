from PIL import Image

def convert_and_compress_png_to_webp(input_path, output_path, quality=80):
    """
    Converts a PNG image to WebP format and compresses it.

    :param input_path: Path to the input PNG image
    :param output_path: Path to save the converted WebP image
    :param quality: Quality of the output WebP image (1 to 100, higher means better quality)
    """
    # Open the PNG image
    with Image.open(input_path) as img:
        # Convert the image to RGB mode if it's in RGBA mode
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        # Save the image in WebP format with specified quality
        img.save(output_path, format='WEBP', quality=quality)
        print(f'Image saved to {output_path} with quality={quality}')

# Example usage
convert_and_compress_png_to_webp('compress & convert png to webp/imgs/1.png', 'compress & convert png to webp/output/example.webp', quality=85)
