import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

# Get screen dimensions
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)
screen_size = (screen_width, screen_height)

# Set the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
fps = 30.0
video_output = cv2.VideoWriter("ScreenRecord.mp4", fourcc, fps, screen_size)

# Set recording duration (in seconds)
record_duration = 10
end_time = time.time() + record_duration

print("Recording started... Press 'q' to stop recording early.")

# Start recording
while time.time() < end_time:
    # Capture screenshot and convert to NumPy array
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)

    # Convert color from BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the video output
    video_output.write(frame_rgb)

    # Display the frame
    cv2.imshow('Recording', frame_rgb)

    # Check if the user wants to stop recording early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoWriter and destroy all windows
video_output.release()
cv2.destroyAllWindows()

print("Screen recording finished.")
