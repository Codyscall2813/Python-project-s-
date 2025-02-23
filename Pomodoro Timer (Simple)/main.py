import time
import sys

def countdown(minutes, message):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        seconds -= 1
    print(message)

def pomodoro():
    try:
        work_duration = int(input("Enter work duration in minutes (default is 25): ") or 25)
        short_break = int(input("Enter short break duration in minutes (default is 5): ") or 5)
        long_break = int(input("Enter long break duration in minutes (default is 15): ") or 15)
        cycles = int(input("Enter number of cycles before a long break (default is 4): ") or 4)
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return

    for cycle in range(1, cycles + 1):
        print(f"\nCycle {cycle}: Work for {work_duration} minutes")
        countdown(work_duration, "Time to take a short break!")

        if cycle < cycles:
            print(f"Take a {short_break}-minute break.")
            print("")
            countdown(short_break, "Break over. Time to get back to work!")
        else:
            print(f"Take a long {long_break}-minute break.")
            print("")
            countdown(long_break, "Break over. Start a new set of cycles or take a longer break if needed.")

if __name__ == "__main__":
    try:
        print("Focus and dedication lead to great results. Let's get started with your Pomodoro Timer!")
        print("")
        pomodoro()
    except KeyboardInterrupt:
        print("\nPomodoro session ended. Have a productive day!")
        sys.exit(0)
