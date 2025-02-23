import cv2

# Read the image
image = cv2.imread("Collection/Draw Sketch/image.jpg")

# Check if the image is loaded correctly
if image is None:
    print("Error: Unable to load image.")
else:
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray_image
    blur = cv2.GaussianBlur(inverted, (21, 21), 0)
    inverted_blur = 255 - blur
    sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

    # Save the sketch image
    cv2.imwrite("Collection/Draw Sketch/sketch_image.png", sketch)

    # Resize the sketch image
    max_width = 800  # Maximum width for display
    max_height = 600  # Maximum height for display

    height, width = sketch.shape[:2]
    scaling_factor = min(max_width / width, max_height / height)
    new_width = int(width * scaling_factor)
    new_height = int(height * scaling_factor)
    
    resized_sketch = cv2.resize(sketch, (new_width, new_height), interpolation=cv2.INTER_AREA)

    # Display the resized image
    cv2.imshow("Image", resized_sketch)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
