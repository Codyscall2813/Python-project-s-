import io
import tkinter as tk
from tkinter import messagebox
import requests
from ttkbootstrap import Style, ttk
from PIL import Image, ImageTk

# API URLs
CAT_IMAGE_API = "https://cataas.com/cat"
CAT_FACT_API = "https://catfact.ninja/fact"

def fetch_cat_fact():
    try:
        response = requests.get(CAT_FACT_API)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        fact_json = response.json()
        return fact_json.get('fact', "No fact available.")
    except requests.RequestException as e:
        print(f"Error fetching cat fact: {e}")
        return "Failed to retrieve cat fact."

def fetch_cat_image():
    try:
        response = requests.get(CAT_IMAGE_API)
        response.raise_for_status()
        pic_bytes = response.content
        pic_data_stream = io.BytesIO(pic_bytes)
        cat_image = Image.open(pic_data_stream)
        cat_image = cat_image.resize((400, 400))
        return ImageTk.PhotoImage(cat_image)
    except requests.RequestException as e:
        print(f"Error fetching cat image: {e}")
        return None

def generate_cat():
    cat_fact = fetch_cat_fact()
    cat_image = fetch_cat_image()

    # Update GUI elements
    fact_label.config(text=cat_fact)
    if cat_image:
        pic_label.config(image=cat_image)
        pic_label.image = cat_image
    else:
        pic_label.config(image=None)

# Create the main window
root = tk.Tk()
root.title("Random Cat Generator")
root.geometry("600x660")

# Create the Style object and configure fonts
style = Style(theme="flatly")
style.configure('TButton', font=("Ubuntu", 14))

# Create the GUI elements
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

fact_label = tk.Label(frame, text="Click on the button to generate a random cat fact and picture!", wraplength=400, font=("Ubuntu", 12), justify=tk.LEFT)
fact_label.pack(padx=10, pady=10, fill=tk.X)

pic_label = tk.Label(frame)
pic_label.pack(padx=10, pady=10)

generate_button = ttk.Button(frame, text="Generate", command=generate_cat)
generate_button.pack(padx=10, pady=20)

root.mainloop()
