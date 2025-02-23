import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
import time

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('600x300')
        self.root.title('Pomodoro Timer')
        self.root.call('wm', 'iconphoto', self.root._w, PhotoImage(file='Collection/Pomodoro Timer GUI/icon.png'))
        self.root.resizable(False, False)

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill='both', expand=True, pady=10)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab4 = ttk.Frame(self.tabs, width=600, height=100)

        self.tabs.add(self.tab1, text='Pomodoro')
        self.tabs.add(self.tab2, text='Short Break')
        self.tabs.add(self.tab3, text='Long Break')
        self.tabs.add(self.tab4, text='Settings')

        self.pomodoro_timer_label = ttk.Label(self.tab1, text='25:00', font=('Ubuntu', 78))
        self.pomodoro_timer_label.pack(pady=20)
        self.short_break_timer_label = ttk.Label(self.tab2, text='5:00', font=('Ubuntu', 78))
        self.short_break_timer_label.pack(pady=20)
        self.long_break_timer_label = ttk.Label(self.tab3, text='15:00', font=('Ubuntu', 78))
        self.long_break_timer_label.pack(pady=20)

        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)

        button_style = ttk.Style()
        button_style.configure('TButton', font=('Ubuntu', 16), padding=3)

        self.start_button = ttk.Button(self.grid_layout, text='Start', command=self.start_timer, style='TButton')
        self.start_button.grid(row=0, column=0, padx=3)
        self.skip_button = ttk.Button(self.grid_layout, text='Skip', command=self.skip_clock, style='TButton')
        self.skip_button.grid(row=0, column=1, padx=3)
        self.reset_button = ttk.Button(self.grid_layout, text='Reset', command=self.reset_clock, style='TButton')
        self.reset_button.grid(row=0, column=2, padx=3)

        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text='Pomodoros: 0', font=('Ubuntu', 16))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.pomodoros = 0
        self.skipped = False
        self.stopped = False
        self.timer_running = False
        self.remaining_seconds = 0

        self.pomodoro_time = 25
        self.short_break_time = 5
        self.long_break_time = 15

        ttk.Label(self.tab4, text="Pomodoro Time (min):").grid(row=0, column=0, padx=10, pady=5, sticky="W")
        self.pomodoro_entry = ttk.Entry(self.tab4, width=5)
        self.pomodoro_entry.insert(0, str(self.pomodoro_time))
        self.pomodoro_entry.grid(row=0, column=1, padx=10, pady=5, sticky="W")

        ttk.Label(self.tab4, text="Short Break Time (min):").grid(row=1, column=0, padx=10, pady=5, sticky="W")
        self.short_break_entry = ttk.Entry(self.tab4, width=5)
        self.short_break_entry.insert(0, str(self.short_break_time))
        self.short_break_entry.grid(row=1, column=1, padx=10, pady=5, sticky="W")

        ttk.Label(self.tab4, text="Long Break Time (min):").grid(row=2, column=0, padx=10, pady=5, sticky="W")
        self.long_break_entry = ttk.Entry(self.tab4, width=5)
        self.long_break_entry.insert(0, str(self.long_break_time))
        self.long_break_entry.grid(row=2, column=1, padx=10, pady=5, sticky="W")

        button_style.configure('SaveButton.TButton', font=('Ubuntu', 12), padding=1)
        ttk.Button(self.tab4, text="Save Settings", command=self.save_settings, style='SaveButton.TButton').grid(row=3, column=0, columnspan=1, pady=2)
        self.tabs.bind("<<NotebookTabChanged>>", self.on_tab_change)
        print("Initialized Pomodoro Timer")
        self.root.mainloop()

    def save_settings(self):
        try:
            self.pomodoro_time = int(self.pomodoro_entry.get())
            self.short_break_time = int(self.short_break_entry.get())
            self.long_break_time = int(self.long_break_entry.get())
            if self.pomodoro_time <= 0 or self.short_break_time <= 0 or self.long_break_time <= 0:
                raise ValueError
            print(f"Settings saved: Pomodoro Time={self.pomodoro_time}, Short Break Time={self.short_break_time}, Long Break Time={self.long_break_time}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter positive numeric values for all fields.")
            print("Failed to save settings: Invalid input")

    def on_tab_change(self, event):
        selected_tab = self.tabs.select()
        if selected_tab == self.tab4:
            self.start_button.grid_forget()
            self.skip_button.grid_forget()
            self.reset_button.grid_forget()
            self.pomodoro_counter_label.grid_forget()
            print("Settings tab selected: Buttons hidden")
        else:
            self.start_button.grid(row=0, column=0, padx=3)
            self.skip_button.grid(row=0, column=1, padx=3)
            self.reset_button.grid(row=0, column=2, padx=3)
            self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10)
            print("Timer tab selected: Buttons visible")

    def start_timer(self):
        if self.timer_running:
            messagebox.showinfo("Timer Running", "The timer is already running.")
            print("Start button pressed but timer is already running")
            return

        print("Starting timer...")
        self.stopped = False
        self.skipped = False
        self.timer_running = True

        timer_id = self.tabs.index(self.tabs.select())
        if timer_id == 0:
            self.remaining_seconds = 60 * self.pomodoro_time
        elif timer_id == 1:
            self.remaining_seconds = 60 * self.short_break_time
        else:
            self.remaining_seconds = 60 * self.long_break_time

        print(f"Timer started: Tab={timer_id + 1}, Time={self.remaining_seconds} seconds")
        self.update_timer()

    def update_timer(self):
        if self.stopped:
            print("Timer stopped")
            self.timer_running = False
            return

        if self.remaining_seconds <= 0:
            print("Timer ended")
            self.handle_timer_end()
            return

        minutes, seconds = divmod(self.remaining_seconds, 60)
        if self.tabs.index(self.tabs.select()) == 0:
            self.pomodoro_timer_label.config(text=f'{minutes:02d}:{seconds:02d}')
        elif self.tabs.index(self.tabs.select()) == 1:
            self.short_break_timer_label.config(text=f'{minutes:02d}:{seconds:02d}')
        else:
            self.long_break_timer_label.config(text=f'{minutes:02d}:{seconds:02d}')

        self.remaining_seconds -= 1
        self.root.after(1000, self.update_timer)

    def handle_timer_end(self):
        self.timer_running = False
        self.stopped = True
        if not self.skipped:
            self.pomodoros += 1
            self.pomodoro_counter_label.config(text=f'Pomodoros: {self.pomodoros}')
            print(f"Timer completed: Total Pomodoros={self.pomodoros}")

            if self.pomodoros % 4 == 0:
                self.tabs.select(2)
                print("Switching to Long Break")
            else:
                self.tabs.select(1)
                print("Switching to Short Break")
        else:
            self.skipped = False
            print("Timer skipped")

        # Reset timer state for the next cycle
        self.reset_clock()

    def skip_clock(self):
        print("Skip button pressed")
        self.stopped = True
        self.timer_running = False

        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.tabs.select(1)
            print("Skipping to Short Break")
        elif current_tab == 1:
            self.tabs.select(2)
            print("Skipping to Long Break")
        else:
            self.tabs.select(0)
            print("Skipping to Pomodoro")

        self.update_timer()

    def reset_clock(self):
        print("Resetting clock")
        self.stopped = True
        self.timer_running = False
        self.remaining_seconds = 0
        self.update_timer_display()
        self.pomodoros = 0
        self.pomodoro_counter_label.config(text='Pomodoros: 0')

    def update_timer_display(self):
        tab_index = self.tabs.index(self.tabs.select())
        if tab_index == 0:
            self.pomodoro_timer_label.config(text='25:00')
        elif tab_index == 1:
            self.short_break_timer_label.config(text='5:00')
        else:
            self.long_break_timer_label.config(text='15:00')

if __name__ == "__main__":
    PomodoroTimer()
