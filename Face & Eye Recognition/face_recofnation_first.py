import cv2 as cv
import os

def detect_faces_and_eyes():
    """
    Detects faces and eyes in real-time using the webcam.

    Press 'q' to exit the program.
    """
    # Define the directory and file names
    base_dir = os.path.dirname(__file__)
    face_cascade_path = os.path.join(base_dir, 'libs', 'haarcascade_frontalface_default.xml')
    eye_cascade_path = os.path.join(base_dir, 'libs', 'haarcascade_eye.xml')

    # Load the pre-trained classifiers for face and eye detection
    face_cascade = cv.CascadeClassifier(face_cascade_path)
    eye_cascade = cv.CascadeClassifier(eye_cascade_path)

    # Open the webcam
    cap = cv.VideoCapture(0)

    while cap.isOpened():
        flag, img = cap.read()
        if not flag:
            print("Error: Unable to read from webcam.")
            break

        # Convert the frame to grayscale for better performance
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

        # Detect eyes in the frame
        eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=7)

        # Draw rectangles around faces and eyes
        for x, y, w, h in faces:
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

        for a, b, c, d in eyes:
            cv.rectangle(img, (a, b), (a + c, b + d), (255, 0, 0), 1)

        # Display the resulting frame
        cv.imshow("Face and Eye Detection", img)

        # Check for the 'q' key to exit the program
        key = cv.waitKey(1)
        if key == ord("q"):
            break

    # Release the webcam and close all windows
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    detect_faces_and_eyes()
