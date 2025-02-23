import requests
import io
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkbootstrap import Style

# Create the main window
root = tk.Tk()
root.title("Image Generator")
root.geometry("700x500")
root.config(bg="white")
root.resizable(False, False)

# Apply the ttkbootstrap theme
style = Style(theme="superhero")

# Function to retrieve and display an image based on the selected category
def display_image(category):
    if category == "Choose Category":
        return  # Do not make an API call if the default option is selected

    try:
        url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=OeMVpNmvnyqkzwZD9EhNl3N6TWPPob9zI4GFb6N8qAg"
        data = requests.get(url).json()
        img_data = requests.get(data["urls"]["regular"]).content

        image = Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label.config(image=photo)
        label.image = photo  # Keep a reference to the image to avoid garbage collection

    except Exception as e:
        label.config(text="Error loading image.")
        print(f"Error: {e}")

# Function to enable/disable the "Generate Image" button
def enable_button(*args):
    state = "normal" if category_var.get() != "Choose Category" else "disabled"
    generate_button.config(state=state)

# Create the GUI elements
def create_gui():
    global category_var, generate_button, label

    # Create a dropdown menu for selecting the category
    category_var = tk.StringVar(value="Choose Category")
    category_options = ["Choose Category", "Food", "Animals", "People", "Music", "Art", "Vehicles", "Random"]
    category_dropdown = ttk.OptionMenu(root, category_var, *category_options, command=enable_button)
    category_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    category_dropdown.config(width=20)

    # Create a button for generating the image
    generate_button = ttk.Button(root, text="Generate Image", state="disabled", command=lambda: display_image(category_var.get()))
    generate_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # Create a label to display the image
    label = tk.Label(root, background="white", text="Select a category and click 'Generate Image'.")
    label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    # Make the columns/rows expandable
    root.columnconfigure([0, 1], weight=1)
    root.rowconfigure(1, weight=1)

# Run the application
if __name__ == '__main__':
    create_gui()
    root.mainloop()
