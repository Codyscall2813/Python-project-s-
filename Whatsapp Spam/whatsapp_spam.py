import pyautogui
import webbrowser as wb
import time

# Open WhatsApp Web
wb.open("https://web.whatsapp.com")
time.sleep(20)

message = "spam_1k"
No_of_times_you_want_to_send_the_message = 500
delay_between_message = 1

# Send the message
for i in range(No_of_times_you_want_to_send_the_message):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(delay_between_message)

print("Messages sent successfully!")
