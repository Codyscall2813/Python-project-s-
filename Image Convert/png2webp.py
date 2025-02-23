import os
from PIL import Image

def convert_png_to_webp(directory):
    os.makedirs(f'{directory}/webp', exist_ok=True)
    for f in os.listdir(directory):
        if f.lower().endswith('.png'):
            img = Image.open(f'{directory}/{f}')
            img.save(f'{directory}/webp/{f[:-4]}.webp', 'webp')
            print(f'Converted {f} to {f[:-4]}.webp')

convert_png_to_webp('bulk-png')