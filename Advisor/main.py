import requests
import tkinter as tk
from tkinter import messagebox

# Function to retrieve advice from the advice API
def get_advice():
    try:
        response = requests.get("https://api.adviceslip.com/advice")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        advice_message.set(data["slip"]["advice"])
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Unable to fetch advice: {e}")

# Create the main window
app = tk.Tk()
app.title("Advice Generator")

# Create and configure widgets
advice_message = tk.StringVar()
message_label = tk.Label(
    app, textvariable=advice_message, wraplength=400, font=("Arial", 14)
)
fetch_button = tk.Button(app, text="Get Advice", command=get_advice)

# Pack widgets
message_label.pack(pady=20)
fetch_button.pack(pady=10)

# Initial advice fetching
get_advice()

# Run the main event loop
app.mainloop()

