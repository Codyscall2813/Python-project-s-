import cv2
import time
from datetime import datetime

print("Press Space-bar to take a selfie")
print("Press Escape key to terminate the window")
time.sleep(5)  # Wait for 5 seconds before starting the webcam

# Initialize the webcam
cam = cv2.VideoCapture(0)

# Create a named window for the webcam feed
cv2.namedWindow("Take Selfie with Python")

# Counter for selfies
selfie_count = 0

while True:
    # Capture frame-by-frame
    ret, frame = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Display the frame
    cv2.imshow("Take Selfie with Python", frame)

    # Wait for a key press
    key = cv2.waitKey(1)

    # Check if the 'Escape' key was pressed
    if key == 27:  # Escape key
        print("Escape key pressed, closing the window")
        break

    # Check if the 'Space-bar' key was pressed
    if key == 32:
        # Create a filename with a timestamp to avoid collisions
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        img_name = f"Selfie_{timestamp}.jpg"
        # Save the captured frame
        cv2.imwrite(img_name, frame)
        print(f"Selfie taken! Saved as {img_name}")
        selfie_count += 1

# Release the webcam and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
