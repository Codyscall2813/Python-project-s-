import tkinter as tk
from tkinter import PhotoImage
import webbrowser
import requests
import threading
import time
import locale
from PIL import Image, ImageTk, ImageDraw
from io import BytesIO


def fetch_user_data(username):
    url = f"https://backend.mixerno.space/instagram/test/{username}"

    proxies = {
        "http": "socks5://qbdxcyua-rotate:aetl8bajmvvm@p.webshare.io:80/",
        "https": "socks5://qbdxcyua-rotate:aetl8bajmvvm@p.webshare.io:80/"
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9",
        "If-None-Match": 'W/"407-D+G+pbsC04ExhIFep0BY+psb5AY"',
        "Origin": "https://livecounts.nl",
        "Priority": "u=1, i",
        "Referer": "https://livecounts.nl/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()
        # print(response.text)
        data = response.json()
        if 'user' in data:
            user_data = data['user']
            return user_data
        else:
            print("Unexpected response format:", data)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
    return None


def update_follower_count_to_canvas(username):
    def update():
        while True:
            user_data = fetch_user_data(username)
            if user_data is not None:
                formatted_count = format_number_with_commas(
                    user_data['followerCount'])
                canvas.itemconfig(number_text, text=formatted_count)
                canvas.itemconfig(username_text, text=user_data['username'])
                profile_pic_url = user_data['pfp']
                profile_image = fetch_profile_image(profile_pic_url)
                if profile_image:
                    circular_image = create_circular_image(profile_image, 140)
                    circular_image = ImageTk.PhotoImage(circular_image)
                    canvas.itemconfig(profile_pic, image=circular_image)
                    canvas.profile_image = circular_image
            else:
                canvas.itemconfig(
                    number_text, text="Error fetching follower count")
            time.sleep(1)

    threading.Thread(target=update, daemon=True).start()


def format_number_with_commas(number):
    return '{:,}'.format(number)


def visit_instagram():
    username = canvas.itemcget(username_text, 'text')
    if username:
        url = f"https://www.instagram.com/{username}/"
        webbrowser.open_new_tab(url)


def fetch_profile_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        return image
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred while fetching profile image: {err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred while fetching profile image: {err}")
    return None


def create_circular_image(image, size):
    mask = Image.new('L', (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    result = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    image = image.resize((size, size), Image.LANCZOS)
    result.paste(image, (0, 0), mask)
    return result


initial_username = "pycode.hubb"

root = tk.Tk()
root.title("Instagram Live Followers Counter")
root.geometry("510x260")
icon_path = "Icons/instagram.png"
icon_image = PhotoImage(file=icon_path)
root.iconphoto(False, icon_image)
root.wm_attributes("-topmost", 1)

canvas = tk.Canvas(root, width=640, height=240)
canvas.pack()
rect = canvas.create_rectangle(30, 30, 480, 190, outline="black", width=5)
profile_pic = canvas.create_image(120, 110, anchor="center")
number_text = canvas.create_text(
    290, 110, text="Loading...", font=("Arial", 24), anchor="w")
username_text = canvas.create_text(
    340, 60, text=initial_username, font=("Arial", 16), anchor="center")
followers_text = canvas.create_text(
    340, 160, text="Followers", font=("Arial", 16), anchor="center")

button_width = 30
button_height = 2
visit_instagram_btn = tk.Button(root, text="Visit on Instagram",
                                command=visit_instagram, height=button_height, width=button_width)
canvas.create_window(150, 210, anchor="nw", window=visit_instagram_btn)

update_follower_count_to_canvas(initial_username)

root.mainloop()
