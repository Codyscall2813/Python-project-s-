import time
import pyautogui

def keep_active():
    """
    Moves the mouse back and forth every 10 seconds to keep apps active.
    """
    print("Press CTRL-C to stop.")
    try:
        while True:
            # Move mouse right and left
            pyautogui.moveRel(5, 0, duration=0.5)
            pyautogui.moveRel(-5, 0, duration=0.5)
            time.sleep(10)
    except KeyboardInterrupt:
        print("Process terminated.")

if __name__ == "__main__":
    keep_active()
