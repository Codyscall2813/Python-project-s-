import tkinter as tk
from tkinter import ttk, messagebox
import pyshorteners


def generate_shortened_url():
    url = entry_url.get("1.0", tk.END).strip()
    selected_service = service_combobox.get()

    if not url:
        messagebox.showwarning("Empty URL", "Please enter a URL to shorten.")
        return

    try:
        s = get_shortener_instance(selected_service)
        shortened_url = s.short(url)
        entry_shortened_url.delete("1.0", tk.END)
        entry_shortened_url.insert("1.0", shortened_url)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def copy_shortened_url():
    shortened_url = entry_shortened_url.get("1.0", tk.END).strip()
    if shortened_url:
        root.clipboard_clear()
        root.clipboard_append(shortened_url)
        messagebox.showinfo("Copied", "Shortened URL copied to clipboard.")
    else:
        messagebox.showwarning("Empty URL", "No shortened URL to copy.")


def get_shortener_instance(selected_service):
    if selected_service == 'Adf.ly':
        return pyshorteners.Shortener(api_key='YOUR_API_KEY', user_id='YOUR_USER_ID').adf_ly
    elif selected_service == 'Bit.ly':
        return pyshorteners.Shortener(api_key='YOUR_API_KEY').bit_ly
    elif selected_service == 'Clck.ru':
        return pyshorteners.Shortener().clckru
    elif selected_service == 'Cutt.ly':
        return pyshorteners.Shortener(api_key='YOUR_API_KEY').cuttly
    elif selected_service == 'Da.gd':
        return pyshorteners.Shortener().dagd
    elif selected_service == 'Is.gd':
        return pyshorteners.Shortener().isgd
    elif selected_service == 'Os.db':
        return pyshorteners.Shortener().osdb
    elif selected_service == 'Ow.ly':
        return pyshorteners.Shortener().owly
    elif selected_service == 'Po.st':
        return pyshorteners.Shortener(api_key='YOUR_API_KEY').post
    elif selected_service == 'Qps.ru':
        return pyshorteners.Shortener().qpsru
    elif selected_service == 'Short.cm':
        return pyshorteners.Shortener(api_key='YOUR_API_KEY').shortcm
    elif selected_service == 'Tiny.cc':
        return pyshorteners.Shortener(api_key='YOUR_API_KEY', login='YOUR_LOGIN').tinycc
    elif selected_service == 'TinyURL.com':
        return pyshorteners.Shortener().tinyurl
    elif selected_service == 'Git.io':
        return pyshorteners.Shortener(code='YOUR_CUSTOM_CODE').gitio
    else:
        raise ValueError("Selected service is not supported.")


root = tk.Tk()
root.title("URL Shortener")

labels = ['URL', 'Choose API', 'Shortened URL']
for index, label_text in enumerate(labels):
    label = ttk.Label(root, text=label_text)
    label.grid(row=index, column=0, padx=10, pady=5, sticky=tk.W)

entry_url = tk.Text(root, width=30, height=1)
entry_url.grid(row=0, column=1, padx=10, pady=5)

API = [
    'Adf.ly', 'Bit.ly', 'Clck.ru', 'Cutt.ly', 'Da.gd',
    'Is.gd', 'Os.db', 'Ow.ly', 'Po.st', 'Qps.ru', 'Short.cm',
    'Tiny.cc', 'TinyURL.com', 'Git.io', 'Tiny.cc'
]
service_combobox = ttk.Combobox(root, values=API, width=37, state='readonly')
service_combobox.grid(row=1, column=1, padx=10, pady=5)
service_combobox.current(0)

entry_shortened_url = tk.Text(root, width=30, height=1)
entry_shortened_url.grid(row=2, column=1, padx=10, pady=5)

button_frame = ttk.Frame(root)
button_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky=tk.E)

generate_button = ttk.Button(
    button_frame, text="Generate", width=18, command=generate_shortened_url)
generate_button.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

copy_button = ttk.Button(button_frame, text="Copy",
                         width=17, command=copy_shortened_url)
copy_button.grid(row=0, column=1, padx=10, pady=5, sticky=tk.E)

root.mainloop()
