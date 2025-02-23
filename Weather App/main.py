import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap as ttk
import requests

# Function to get weather information from OpenWeatherMap API
def get_weather(city):
    API_key = "1b2f8c4cbcbd0ee0ce628c4130e28dc2"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    try:
        res = requests.get(url)
        res.raise_for_status()  # Check if request was successful
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Unable to get data: {e}")
        return None
    
    weather = res.json()
    if weather.get('cod') != 200:
        messagebox.showerror("Error", weather.get('message', 'City not found'))
        return None
    
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city_name = weather['name']
    country = weather['sys']['country']
    
    icon_url = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city_name, country)

# Function to search weather for a city
def search():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name")
        return

    result = get_weather(city)
    if result is None:
        return

    icon_url, temperature, description, city_name, country = result
    location_label.configure(text=f"{city_name}, {country}")

    # Get the weather icon image from the URL and update the icon label
    try:
        image = Image.open(requests.get(icon_url, stream=True).raw)
        icon = ImageTk.PhotoImage(image)
    except Exception as e:
        messagebox.showerror("Error", f"Unable to load image: {e}")
        return

    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description.capitalize()}")

# Main window setup
root = ttk.Window(themename="superhero")
root.title("Weather App")
root.geometry("400x400")

# Entry for city name
city_entry = ttk.Entry(root, font="Ubuntu, 18")
city_entry.pack(pady=10)

# Button to search for the weather information
search_button = ttk.Button(root, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

# Labels for displaying weather information
location_label = tk.Label(root, font="Ubuntu, 25")
location_label.pack(pady=20)

icon_label = tk.Label(root)
icon_label.pack()

temperature_label = tk.Label(root, font="Ubuntu, 20")
temperature_label.pack()

description_label = tk.Label(root, font="Ubuntu, 20")
description_label.pack()

root.mainloop()
