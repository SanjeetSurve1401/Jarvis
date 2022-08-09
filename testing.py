import os
from time import time
import webbrowser
import keyboard
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
from PyDictionary import PyDictionary as Dictionary
from tkinter.filedialog import* 
import datetime
from playsound import playsound

from datetime import datetime


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',178)

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f": {audio}")
    print("   ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        command.pause_threshold = 0.7
        audio = command.listen(source)

        try:
            print("Recognizing..........")
            query = command.recognize_google(audio,language='en-in')
            print(f"You Said : {query}")

        except Exception as Error:
            return "none"

        return query.lower()

def time():
    now = datetime.now()
    Speak(f"{now.strftime('%Y/%m/%d %I:%M:%p')}") #12-hour format

#def greet():
    #t_hr = datetime.datetime.now().hour
    #if 6 > t_hr < 12:
    #    Speak("Good Morning Sir!")
    #elif 12 > t_hr > 16:
    #    Speak("Good Afertoon Sir!")
    #elif 16 > t_hr < 22:
    #    Speak("Good Evening Sir!")
    #elif 22 > t_hr > 1:
    #    Speak("Sir are we gonna work for late night?")
    #else:
    #    Speak("I would recommed you sir, to get a sleep your working for a long time")


    
    query = takecommand()
    if 'close' in query:
        Speak("Closing Browser")
        os.system("TASKKILL /F /IM chrome.exe")
        


def taskexe ():
    time()

    while True:
        query = takecommand()

        if 'hello' in query:
            Speak("Hello Sir, How may I help you?")

        elif 'stop' in query:
            break

taskexe()