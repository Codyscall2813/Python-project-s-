import cv2
import mediapipe as mp
import pyautogui as pa
import time
import numpy as np

# Easy module names
drawing_utils = mp.solutions.drawing_utils
drawing_styles = mp.solutions.drawing_styles
hand_detection = mp.solutions.hands

def convert_to_pixel_coordinates(landmark, image_width, image_height):
    """
    Convert relative hand landmark coordinates to pixel coordinates.
    """
    return int(landmark.x * image_width), int(landmark.y * image_height)

# Track the last time input was processed
last_process_time = time.time()

def handle_gesture(slope, distance):
    """
    Detect hand gestures and simulate key presses based on the gesture.
    """
    global last_process_time

    # Only process input every 500 milliseconds
    if time.time() - last_process_time > 0.5:
        last_process_time = time.time()

        # Only process if the hand is within a reasonable distance
        if distance > 0.2:
            if slope < -78:
                print("Gesture detected: Left")
                pa.press("left")
            elif 0 < slope < 78:
                print("Gesture detected: Right")
                pa.press("right")

# Open webcam for input
cap = cv2.VideoCapture(0)

with hand_detection.Hands(
    model_complexity=0, min_detection_confidence=0.5, min_tracking_confidence=0.5
) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Convert the image to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        # Convert the image back to BGR
        frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

        image_height, image_width, _ = frame.shape

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Get coordinates for specific landmarks
                landmark1 = hand_landmarks.landmark[0]
                x1, y1 = convert_to_pixel_coordinates(landmark1, image_width, image_height)
                frame = cv2.circle(frame, (int(x1), int(y1)), 20, (255, 0, 0), thickness=2)

                landmark2 = hand_landmarks.landmark[5]
                x2, y2 = convert_to_pixel_coordinates(landmark2, image_width, image_height)
                frame = cv2.circle(frame, (int(x2), int(y2)), 20, (255, 0, 0), thickness=2)

                # Calculate the angle and distance between landmarks
                slope = np.degrees(np.arctan2((landmark1.y - landmark2.y), (landmark1.x - landmark2.x)))
                distance = np.sqrt((landmark1.x - landmark2.x) ** 2 + (landmark1.y - landmark2.y) ** 2)
                print(f"Slope: {slope}, Distance: {distance}")
                handle_gesture(slope, distance)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                drawing_utils.draw_landmarks(
                    frame,
                    hand_landmarks,
                    hand_detection.HAND_CONNECTIONS,
                    drawing_styles.get_default_hand_landmarks_style(),
                    drawing_styles.get_default_hand_connections_style(),
                )
        
        # Flip the image horizontally for a mirror view
        cv2.imshow("MediaPipe Hands", cv2.flip(frame, 1))
        
        # Check for key presses
        key = cv2.waitKey(5) & 0xFF
        if key == 27 or key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
