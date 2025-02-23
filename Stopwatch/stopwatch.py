import tkinter as tk
from tkinter import font as tkfont
import time

class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("900x200")
        self.root.configure(bg='purple')

        self.custom_font = tkfont.Font(family="Courier", size=100, weight="bold")

        self.time_label = tk.Label(root, font=self.custom_font, background='#0C359E', foreground='white')
        self.time_label.pack(expand=True, fill='both')

        self.start_button = tk.Button(root, text="Start", font=tkfont.Font(size=20), command=self.start)
        self.start_button.pack(side='left', fill='x', expand=True)
        
        self.stop_button = tk.Button(root, text="Stop", font=tkfont.Font(size=20), command=self.stop)
        self.stop_button.pack(side='left', fill='x', expand=True)
        
        self.reset_button = tk.Button(root, text="Reset", font=tkfont.Font(size=20), command=self.reset)
        self.reset_button.pack(side='left', fill='x', expand=True)
        
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.update_time()

    def format_time(self, seconds):
        millis = int((seconds % 1) * 100)
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        return "{:02}:{:02}:{:02}.{:02}".format(int(hours), int(mins), int(secs), millis)
    
    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        formatted_time = self.format_time(self.elapsed_time)
        self.time_label.config(text=formatted_time)
        self.root.after(50, self.update_time)
    
    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
    
    def stop(self):
        if self.running:
            self.running = False
    
    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.time_label.config(text=self.format_time(self.elapsed_time))

root = tk.Tk()
app = StopwatchApp(root)

root.mainloop()