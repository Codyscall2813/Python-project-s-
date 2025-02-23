import datetime
import time
from playsound import playsound


def set_alarm():
    print("Welcome to the Simple Alarm Clock!")
    print("Enter the time for the alarm (12-hour format, HH:MM AM/PM):")

    while True:
        try:
            alarm_time = input("Set alarm time: ").strip().upper()
            time_obj = datetime.datetime.strptime(alarm_time, "%I:%M %p")
            alarm_hour = time_obj.hour
            alarm_minute = time_obj.minute
            return alarm_hour, alarm_minute
        except ValueError:
            print("Invalid input format. Please enter time in HH:MM AM/PM format.")


def alarm_clock():
    alarm_hour, alarm_minute = set_alarm()
    alarm_time_display = datetime.time(
        alarm_hour, alarm_minute).strftime("%I:%M %p")
    print(f"Alarm set for {alarm_time_display}")

    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        if current_hour == alarm_hour and current_minute == alarm_minute:
            print("Alarm! Wake up!")
            playsound('alarm_sound.mp3')
            break

        time.sleep(10)


alarm_clock()