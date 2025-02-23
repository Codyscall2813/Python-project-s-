import tkinter as tk
from tkinter import messagebox
import emoji
import re

class EmojiKeypad(tk.Frame):
    EMOJI_GRID = [
        ["😀", "🥰", "😴", "🤓", "🤮", "🤬", "😨", "🤑", "😫", "😎"],
        [
            "🐒", "🐕", "🐎", "🐪", "🐁", "🐘", "🦘", "🦈", "🐓", "🐝",
            "👀", "🦴", "👩🏿", "‍🤝", "🧑", "🏾", "👱🏽", "‍♀", "🎞", "🎨", "⚽",
        ],
        [
            "🍕", "🍗", "🍜", "☕", "🍴", "🍉", "🍓", "🌴", "🌵", "🛺",
            "🚲", "🛴", "🚉", "🚀", "✈", "🛰", "🚦", "🏳", "‍🌈", "🌎", "🧭",
        ],
        [
            "🔥", "❄", "🌟", "🌞", "🌛", "🌝", "🌧", "🧺", "🧷", "🪒",
            "⛲", "🗼", "🕌", "👁", "‍🗨", "💬", "™", "💯", "🔕", "💥", "❤",
        ],
    ]

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.target_entry = None
        self.clipboard = ""

        for row_index, row in enumerate(self.EMOJI_GRID):
            for col_index, emoji_char in enumerate(row):
                button = tk.Button(
                    self,
                    text=emoji_char,
                    command=lambda char=emoji_char: self.add_to_entry(char),
                    font=("Segoe UI Emoji", 14),
                    bg="#F0E68C",  # Khaki
                    fg="#4682B4",  # SteelBlue
                    borderwidth=2,
                    relief="raised"
                )
                button.grid(row=row_index, column=col_index, sticky="news")

        self._create_control_buttons()

    def _create_control_buttons(self):
        buttons = [
            ("Space", self.add_space, 10, 1),
            ("Tab", self.add_tab, 12, 2),
            ("Backspace", self.remove_last_char, 14, 3),
            ("Clear", self.clear_entry, 17, 2),
            ("Hide", self.hide_keypad, 19, 2)
        ]

        for text, command, col, colspan in buttons:
            button = tk.Button(
                self,
                text=text,
                command=command,
                font=("Roboto", 14),
                bg="#F0E68C",  # Khaki
                fg="#4682B4",  # SteelBlue
                borderwidth=2,
                relief="raised"
            )
            button.grid(row=0, column=col, columnspan=colspan, sticky="news")

    def add_to_entry(self, emoji_char):
        if self.target_entry:
            self.target_entry.insert("end", emoji_char)

    def clear_entry(self):
        if self.target_entry:
            self.target_entry.delete(0, tk.END)

    def remove_last_char(self):
        if self.target_entry:
            current_text = self.target_entry.get()
            self.target_entry.delete(0, tk.END)
            self.target_entry.insert("end", current_text[:-1])

    def add_space(self):
        if self.target_entry:
            self.add_to_entry(" ")

    def add_tab(self):
        if self.target_entry:
            self.add_to_entry("    ")

    def show_keypad(self, entry_widget):
        self.target_entry = entry_widget
        self.place(relx=0.5, rely=0.6, anchor="center")

    def hide_keypad(self):
        self.target_entry = None
        self.place_forget()

def clear_text_fields():
    entry_text.delete(0, tk.END)
    result_text.delete("1.0", tk.END)

def search_emoji_meaning():
    text = entry_text.get()
    if not text:
        result_text.insert(tk.END, "No emoji entered.\n")
        return
    
    emojis = re.findall(r'[\U0001F600-\U0001F64F]|[\U0001F300-\U0001F5FF]|[\U0001F680-\U0001F6FF]|[\U0001F700-\U0001F77F]|[\U0001F780-\U0001F7FF]|[\U0001F800-\U0001F8FF]|[\U0001F900-\U0001F9FF]|[\U0001FA00-\U0001FA6F]|[\U0001FA70-\U0001FAFF]', text)
    
    if not emojis:
        result_text.insert(tk.END, "No valid emojis found.\n")
        return
    
    meanings = [emoji.demojize(e).replace(":", "").replace("_", " ") for e in emojis]
    result_text.insert(tk.END, f"Emoji meanings: {', '.join(meanings)}\n")

def exit_application():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        main_window.destroy()

main_window = tk.Tk()
main_window.title("Emoji Dictionary")
main_window.geometry("1000x700")

title_label = tk.Label(
    main_window,
    text="Emoji Dictionary",
    font=("Roboto", 50),
    fg="#f17102"  # Magenta
)
title_label.place(x=160, y=10)

prompt_label = tk.Label(
    main_window,
    text="Enter any emoji to search...",
    font=("Roboto", 30),
    fg="#32CD32"  # LimeGreen
)
prompt_label.place(x=160, y=120)

entry_text = tk.Entry(
    main_window,
    font=("Roboto", 35),
    width=28,
    border=2,
    bg="#FFFFE0",  # LightYellow
    fg="#8B4513"  # SaddleBrown
)
entry_text.place(x=120, y=180)
entry_text.bind("<Button-1>", lambda event: entry_text.delete(0, tk.END))

search_button = tk.Button(
    main_window,
    text="🔍 Search",
    command=search_emoji_meaning,
    font=("Roboto", 20),
    bg="#90EE90",  # LightGreen
    fg="#0000FF",  # Blue
    borderwidth=2,
    relief="raised"
)
search_button.place(x=270, y=250)

clear_button = tk.Button(
    main_window,
    text="🧹 Clear",
    command=clear_text_fields,
    font=("Roboto", 20),
    bg="#FFA500",  # Orange
    fg="#0000FF",  # Blue
    borderwidth=2,
    relief="raised"
)
clear_button.place(x=545, y=250)

meaning_label = tk.Label(
    main_window,
    text="Meaning...",
    font=("Roboto", 30),
    fg="#32CD32"  # LimeGreen
)
meaning_label.place(x=160, y=340)

result_text = tk.Text(
    main_window,
    height=7,
    width=57,
    font=("Roboto", 17),
    bg="#FFFFE0",  # LightYellow
    fg="#8B4513",  # SaddleBrown
    borderwidth=2,
    relief="solid"
)
result_text.place(x=120, y=400)

exit_button = tk.Button(
    main_window,
    text="❌ Exit",
    command=exit_application,
    font=("Roboto", 20),
    bg="#FF6347",  # Tomato
    fg="#000000",  # Black
    borderwidth=2,
    relief="raised"
)
exit_button.place(x=435, y=610)

emoji_keypad = EmojiKeypad(main_window)
keypad_button = tk.Button(
    main_window,
    text="⌨",
    command=lambda: emoji_keypad.show_keypad(entry_text),
    font=("Roboto", 18),
    bg="#FFFFE0",  # LightYellow
    fg="#32CD32",  # LimeGreen
    borderwidth=2,
    relief="raised"
)
keypad_button.place(x=870, y=183)

main_window.protocol("WM_DELETE_WINDOW", exit_application)
main_window.mainloop()
