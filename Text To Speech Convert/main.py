# Importing the library
from gtts import gTTS
import os
import platform

# Providing the text
input_text = ("Hello! PYCODEHUBB Here. Find Coding Projects at our Telegram channel for PYCODEHUBB. "
              "Follow us on Instagram and subscribe to our Telegram channel.")

# Setting the language
language = "en"

# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, slow=False)

# Creating and saving the audio file
audio_file = "demo.mp3"
voice.save(audio_file)

# Playing the file
def play_audio(file_name):
    if platform.system() == "Windows":
        os.system(f"start {file_name}")
    elif platform.system() == "Darwin":  # macOS
        os.system(f"afplay {file_name}")
    else:  # Linux
        os.system(f"mpg321 {file_name}")

play_audio(audio_file)
