import tkinter as tk
from ttkbootstrap import Style, ttk
import requests

def get_definition(word):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        if data:
            meanings = data[0]['meanings']
            definitions = []
            for i, meaning in enumerate(meanings):
                part_of_speech = meaning['partOfSpeech']
                definition_text = meaning['definitions'][0]['definition']
                definitions.append(f"Meaning: {part_of_speech}\nDefinition: {definition_text}")
                if (i + 1) % 2 == 0:
                    definitions.append("")  # Add a newline after every second pair
            return '\n\n'.join(definitions)
        return "No definition found."
    else:
        return "Error fetching definition."

def search_definition():
    word = entry_word.get()
    definition = get_definition(word)
    
    # Debugging: Print the type and content of definition in a better format
    print("----- Debug Info -----")
    print(f"Definition type: {type(definition)}")
    print(f"Definition content:\n{definition}")
    print("----------------------")
    
    text_output.configure(state='normal')
    text_output.delete('1.0', tk.END)
    text_output.insert(tk.END, definition)
    text_output.configure(state='disabled')

root = tk.Tk()
style = Style(theme="superhero")
root.title("Dictionary App")
root.geometry("500x300")

# Set the font to Ubuntu
ubuntu_font = ('Ubuntu', 15)

# Search frame
frame_search = ttk.Frame(root)
frame_search.pack(padx=20, pady=20)

# Label for the word entry field
label_word = ttk.Label(frame_search, text="Enter a word:", font=ubuntu_font)
label_word.grid(row=0, column=0, padx=5, pady=5)

# Entry field for the word
entry_word = ttk.Entry(frame_search, width=20, font=ubuntu_font)
entry_word.grid(row=0, column=1, padx=5, pady=5)

# Search button
button_search = ttk.Button(frame_search, text="Search", command=search_definition)
button_search.grid(row=0, column=2, padx=5, pady=5)

# Output frame
frame_output = ttk.Frame(root)
frame_output.pack(padx=20, pady=10)

# Text output field for displaying the definition with word wrap
text_output = tk.Text(frame_output, height=10, state='disabled', font=ubuntu_font, wrap='word')
text_output.pack()

root.mainloop()
