import tkinter as tk
from tkinter import messagebox, filedialog
import os

class Notepad:
    def __init__(self, width=400, height=400):
        self.root = tk.Tk()
        self.root.title("Untitled - Notepad")
        self.root.geometry(f"{width}x{height}")

        try:
            self.root.iconbitmap("Collection/Notepad/notepad_win11.ico")
        except tk.TclError:
            pass
        
        text_font = ("Arial", 16)
        self.text_area = tk.Text(self.root, font=text_font, wrap="word")
        self.text_area.pack(expand=True, fill="both", side=tk.LEFT)

        self.setup_menu()
        self.setup_scrollbar()

        self.file = None

    def setup_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit_application)
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)
        menubar.add_cascade(label="Edit", menu=edit_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About Notepad", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menubar)

    def setup_scrollbar(self):
        scrollbar = tk.Scrollbar(self.root, command=self.text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=scrollbar.set)

    def quit_application(self):
        self.root.destroy()

    def show_about(self):
        messagebox.showinfo("Notepad", "Created by: @Pycode.Hubb")

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file_path:
            self.file = file_path
            self.root.title(f"{os.path.basename(self.file)} - Notepad")
            with open(self.file, "r") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, file.read())

    def new_file(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.text_area.delete(1.0, tk.END)

    def save_file(self):
        if self.file is None:
            self.file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if self.file:
            with open(self.file, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.root.title(f"{os.path.basename(self.file)} - Notepad")

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def run(self):
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    notepad = Notepad(width=600, height=400)
    notepad.run()
