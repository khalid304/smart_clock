import pyttsx3
import tkinter as tk
from time import strftime, localtime

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # Try voice[1] instead of [0]

# Create main window
root = tk.Tk()
root.title("Smart Clock")

last_greeting = [""]

def speak(greeting):
    print("Speaking:", greeting)  # Debug print
    engine.say(greeting)
    engine.runAndWait()

def time():
    current_time = strftime("%H:%M:%S\n%d-%m-%Y")
    hour = localtime().tm_hour

    if 0 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 18:
        greeting = "Good Afternoon"
    elif 18 <= hour < 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    if greeting != last_greeting[0]:
        speak(greeting)
        last_greeting[0] = greeting

    label.config(text=current_time + "\n" + greeting)
    label.after(1000, time)

label = tk.Label(root, font=('Calibri', 50, 'bold'), background='white', foreground='black')
label.pack(anchor='center')

time()
root.mainloop()
