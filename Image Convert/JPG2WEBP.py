from PIL import Image

img = Image.open("image.jpg")
img.save("image.png")

print("Successfull (JPG --> PNG)")

