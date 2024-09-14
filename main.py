import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import pygame
import os
from datetime import datetime
import time
import webbrowser 
from tkinter import *
from tkinter import ttk


def open_youtube():
    youtube_path = r"C:\Users\User\Desktop\YouTube.lnk"
    os.startfile(youtube_path)

def open_google():
    google_path = r"c:\Users\User\Desktop\Google Chrome.lnk"
    os.startfile(google_path)

def open_tg():
    tg_path = r"c:\Users\User\Desktop\Telegram.lnk"
    os.startfile(tg_path)

def open_jutsu():
  url = 'https://jut.su/'
  webbrowser.open_new(url)

def speak(text):
    tts = gTTS(text, lang='ru')
    file_name = f'answer_{datetime.now().strftime("%Y%m%d%H%M%S")}.mp3'
    tts.save(file_name)
    pygame.mixer.init()
    pygame.mixer.music.load(file_name)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove(file_name)

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Сер слушаю сер")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
            command = recognizer.recognize_google(audio, language='ru-RU')
            print(f"Вы сказали: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Извините, я не понял вас.")
            return None
        except sr.RequestError:
            speak("Ошибка запроса к серверу.")
            return None

def process_command(command):
    if "открой youtube" in command:
        open_youtube()
    elif "открой гугл" in command:
        open_google()
    elif "открой telegram" in command:
        open_tg()
    elif "открой jut.su" in command:
        open_jutsu()
    elif "заткнись" in command:
        speak("Сер так точно сер")
        time.sleep(2)
        root.mainloop()
        return False
    else:
        speak("Сер да сер!")
    return True

def main():
            speak("привет я многофункцианальний помошник валеры")
            while True:
                command = listen_for_command()
                if command:
                    if not process_command(command):
                        root.mainloop()
                        break


def startMain():
    if __name__ == "__main__":
        main()
     
root = Tk()
root.title("Vasyagpt")
root.geometry("450x300")

# Create a style for the button
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 16),
                padding=10,
                background="black",
                foreground="black")

# Add a hover effect to the button
style.map("TButton",
          foreground=[('pressed', 'black'), ('active', 'black')],
          background=[('pressed', '!disabled', 'blue'), ('active', 'red')])

# Create the button
btn = ttk.Button(root, text="Start Bot", command=startMain, style="TButton")
btn.pack(expand=True)

root.mainloop()