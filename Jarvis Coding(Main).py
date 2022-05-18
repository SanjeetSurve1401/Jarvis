from io import TextIOWrapper
import os
from time import time
from tkinter.constants import TRUE
import webbrowser
import keyboard
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
from requests.api import request
import speech_recognition as sr
import wikipedia
from PyDictionary import PyDictionary as Dictionary
from tkinter.filedialog import* 
import datetime
from playsound import playsound
from wikipedia.wikipedia import search
from bs4 import BeautifulSoup
import requests
import speedtest

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',190)

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
    t_now = datetime.datetime.now().strftime("%I:%M:%p")
    Speak(f"its {t_now}")

def greet():
    t_hr = datetime.datetime.now().hour
    if 6 < t_hr < 12:
        Speak("Good Morning Sir!")
    elif 12 <= t_hr < 16:
        Speak("Good Afteroon Sir!")
    elif 16 <= t_hr < 22:
        Speak("Good Evening Sir!")
    elif 22 <= t_hr > 1:
        Speak("Sir are we gonna work for late night?")
    else:
        Speak("I would recommed you sir, to get a sleep your working for a long time")

def SS():
    myscreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path+"_ss.png")

def Youtubecontroling():
    comm = takecommand()

    if 'pause' in comm:
        keyboard.press('space bar')
    elif 'play' in comm:
        keyboard.press('space bar')
    elif 'begining' in comm:
        keyboard.press('0')
    elif 'mute' in comm:
        keyboard.press('m')
    elif 'unmute' in comm:
        keyboard.press('m')
    elif 'forward' in comm:
        keyboard.press('l')
    elif 'backward' in comm:
        keyboard.press('j')
    elif 'full screen' in comm:
        keyboard.press('f') 
    elif 'cinema mode' in comm:
        keyboard.press('t')
    elif 'increase volume 25%' in comm:
        keyboard.press_and_release('Up Arrow + Up Arrow + Up Arrow + Up Arrow + Up Arrow')
    elif 'decrese volume 25%' in comm:
        keyboard.press_and_release('Down Arrow + Down Arrow + Down Arrow + Down Arrow + Down Arrow')
    elif 'Next video' in comm:
        keyboard.press_and_release('Shift + N') 
    elif 'Previous' in comm:
        keyboard.press_and_release('Shift + P') 
    elif 'Mini' in comm:
        keyboard.press('i') 
    
def ChromeAuto():
    command = takecommand()

    if ('close tab') in command:
        keyboard.press_and_release('ctrl + w')
    elif ('new window') in command:
        keyboard.press_and_release('ctrl + n')
    elif ('home page') in command:
        keyboard.press_and_release('Alt + Home')
    elif ('Back') in command:
        keyboard.press_and_release('Alt + Left Arrow')
    elif ('forward') in command:
        keyboard.press_and_release('Alt + Right Arrow')
    elif ('stop refreshing') in command:
        keyboard.press_and_release('Esc')
    elif ('normal zoom') in command:
        keyboard.press_and_release('Ctrl + 0')
    elif ('bookmark') in command:
        keyboard.press_and_release('Ctrl + D')
    elif ('Find') in command:
        keyboard.press_and_release('Ctrl + F')
    elif ('Download') in command:
        keyboard.press_and_release('Ctrl + J')
    elif ('address') in command:
        keyboard.press_and_release('Ctrl + K')
    elif ('privatemode') in command:
        keyboard.press_and_release('Ctrl + Shift + N')
    elif ('Refresh') in command:
        keyboard.press_and_release('F5')
    elif ('new tab') in command:
        keyboard.press_and_release('Ctrl + T')
    elif ('Close Window') in command:
        keyboard.press_and_release('Alt + F4')

def OpenApps():
    command = takecommand()
    if 'chrome' in command:
        os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        Speak("Opening chrome browser")
    elif 'firefox' in command:
        os.startfile("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
        Speak("Opening Firefox")
    elif 'cut' in command:
        os.startfile("C:\\Windows\\System32\\SnippingTool.exe")
        Speak("Opening Snipping Tool")

def CloseApps():
    command = takecommand()
    if 'close chrome browser' in command:
        os.system("TASKKILL /F /IM chrome.exe")
        Speak("Closing chrome browser")

    elif 'close firefox browser' in command:
        os.system("TASKKILL /F /IM firefox.exe")
        Speak("Closing Firefox")

    elif 'close snipping' in command:
        os.system("TASKKILL /F /IM SnippingTool.exe")
        Speak("Closing Snipping Tool")
    
def Temp():
    query = takecommand()
    if 'temperature in' in query:
        query = query.replace("jarvis", "")
        query1 = query.replace ("search","")
        url = f"https://www.google.com/search?q={query1}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        Speak(f"{query1} is {temperature}")

def Temperature():
    search = "Temperature in My Location"
    url = f"https://www.google.com/search?q={search}"
    tr = requests.get(url)
    data = BeautifulSoup(tr.text,"html.parser")
    temp = data.find("div",class_= 'BNeawe').text
    Speak(f"The current temperature in Chiplun is {temp}")

def SpeedTest():
    query = takecommand()

    Speak("Checking Speed....")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUpload = int(uploading/800000)

    if 'upload' in query:
        Speak(f"The Uploading Speed is {correctUpload} Mbps")
    elif 'download' in query:
        Speak(f"The Downloading Speed is {correctDown} Mbps")
    else:
        Speak(f"The Downloading Speed is {correctDown} & The Uploading Spped is {correctUpload} Mbps")

def TaskExe():
    greet()
    time()
    Temperature()
    Speak("Jarvis is at your service")

    while True:
        query = takecommand()

    #General Commands
        if 'hey' in query:
            Speak("Hello Sir")

        elif 'audible' in query:
            Speak("Yes, Crystal Clear")
            Speak("my processing speed is little bit slow, sorry for that")

        elif 'good job' in query:
            Speak("I hope you Satisfy with my service?")

        elif 'its ok' in query:
            Speak("Sounds Good!")

        elif 'totally satisfy' in query:
            Speak("sounds Good")

        elif 'thank' in query:
            Speak("Most welcome master")
        
        elif 'no bro' in query:
            Speak("Ok sir, let me know if you need something")

        elif 'nothing' in query:
            Speak("we should think about new project, what say Sir?")
            Speak("Or you can make me more advanced")
            Speak("so I can be more more powerfull and help you in your daily task")

        elif 'working on you' in query:
            Speak("Oops sorry i was not knowing that")
            Speak("Please carry on improving me")

        elif 'right bro' in query:
            Speak("do you have any idea Sir")

        elif 'going on' in query:
            Speak("nothing much")
            Speak("What about you Sir")

        elif 'i am fine' in query:
            Speak("sounds good, how can I help you sir")

        elif 'getting bore' in query:
            Speak("I tell you jokes, you just have to say tell jokes")

        
#Task performing 

    #YT
        elif 'open youtube' in query:
            Speak("Opening youtube")
            query = query.replace("jarvis", "")
            web= 'https://www.youtube.com/'
            webbrowser.open(web)
            Speak("Looking for the match ")
            Speak("Task Completed")
            Speak("Do you want to Activate Youtube Controlling Mode")
        
        elif 'on youtube' in query:
            Speak("Opening Youtube")
            query = query.replace("jarvis search","")
            query = query.replace("on youtube", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            Speak("Looking for the match ")
            Speak("Task Completed")
            Speak("Do you want to Activate Youtube Controlling Mode")

     #YT Controlling
        elif 'activate youtube'in query:
            Speak("Youtube Controling Mode is now Activated ")
            while TRUE:
                query = takecommand() 
                if 'pause' in query:
                    Speak("video paused")
                    keyboard.press('space bar')
                    Speak("Video is paused, when you want to play just say it")
                elif 'play' in query:
                    keyboard.press('space bar')
                    Speak("Enjoy the video")
                elif 'begining' in query:
                    keyboard.press('0')
                    Speak("Video Starting from Begnning")
                elif 'mute' in query:
                    keyboard.press('m')
                    Speak("Audio is mute,whenever you want to unmute just say it")
                elif 'unmute' in query:
                    keyboard.press('m')
                    Speak("Unmuted")
                elif 'forward' in query:
                    keyboard.press('l')
                    Speak("Forwarding 10 seconds")
                elif 'backward' in query:
                    keyboard.press('j')
                    Speak("Backward 10 seconds")
                elif 'full screen' in query:
                    keyboard.press('f') 
                    Speak("Full Screen Enjoy the video")
                elif 'cinema' in query:
                    keyboard.press('t')
                    Speak("Cinema Mode Activated")
                elif 'normal' in query:
                    keyboard.press('Esc')
                    Speak("Exit the full Screen") 
                elif 'increase volume 25%' in query:
                    keyboard.press_and_release('Up Arrow + Up Arrow + Up Arrow + Up Arrow + Up Arrow')
                    Speak("Video Volume increased by 25%")
                elif 'decrese volume 25%' in query:
                    keyboard.press_and_release('Down Arrow + Down Arrow + Down Arrow + Down Arrow + Down Arrow')
                    Speak("Video Volume decreased by 25%")
                elif 'Next video' in query:
                    keyboard.press_and_release('Shift + N')
                    Speak("Playing next video") 
                elif 'Previous' in query:
                    keyboard.press_and_release('Shift + P') 
                    Speak("Going back to the pervious one")
                elif 'Mini' in query:
                    keyboard.press('i') 
                    Speak("Mini Mode activated")
                elif 'youtube tool' in query:
                    Youtubecontroling()
                elif'deactivate' in query:
                    Speak("Deactivated Youtube Controling Mode")
                    break
        
    #Google Search
    
        elif 'google it' in query:
            Speak("Searching on Google")
            query = query.replace("jarvis", "")
            query = query.replace("google it", "")
            pywhatkit.search(query)
            Speak("Looking for the match ")
            Speak("Task Completed")

    #Wikipedia Search
        elif 'search on wikipedia' in query:
            Speak("Opening Browser")
            query = query.replace("jarvis", "" )
            query = query.replace("for", "")
            query = query.replace("Search", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query,2)
            Speak ("Opening Browser")
            Speak ("Searching on Wikipedia")
            Speak (f"According to wikipedia : {wiki}")

    #Browser Operations
        elif ('close current tab') in query:
            keyboard.press_and_release('ctrl + w')
            Speak('Closing the current tab')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('new tab') in query:
            keyboard.press_and_release('Ctrl + T')
            Speak('opening new tab')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('Close Window') in query:
            keyboard.press_and_release('Alt + F4')
            Speak('Browser Closed')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('new window') in query:
            keyboard.press_and_release('ctrl + n')
            Speak('Opening a new Window')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('home page') in query:
            keyboard.press_and_release('Alt + Home')
            Speak('moving to home page, google engine')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('Back') in query:
            keyboard.press_and_release('Alt + Left Arrow')
            Speak('Going back')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('forward') in query:
            keyboard.press_and_release('Alt + Right Arrow')
            Speak('going forward')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('stop refreshing') in query:
            keyboard.press_and_release('Esc')
            Speak('Stop Loading')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('Refresh') in query:
            keyboard.press_and_release('F5')
            Speak('refreshing the page')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('normal zoom') in query:
            keyboard.press_and_release('Ctrl + 0')
            Speak('Default or the normal view')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('save bookmark') in query:
            keyboard.press_and_release('Ctrl + D')
            Speak('saved as a bookmark')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('Find') in query:
            keyboard.press_and_release('Ctrl + F')
            Speak('Quick searching mode activated')
        elif ('Download') in query:
            keyboard.press_and_release('Ctrl + J')
            Speak('Here are the download Files')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('address') in query:
            keyboard.press_and_release('Ctrl + K')
            Speak('now your at address bar')
            Speak("Task Completed")
            Speak("anything else sir?")
        elif ('private mode') in query:
            keyboard.press_and_release('Ctrl + Shift + N')
            Speak('Opening the Incognito mode')
            Speak("Task Completed")
            Speak("anything else sir?")
        
       

    #Jokes
        elif 'jokes' in query:
            get = pyjokes.get_joke()
            Speak(get)

    #Repeatation Mode
        elif 'repeat' in query:
            Speak('Repetation Mode started')
            jj = takecommand()
            Speak(f"You Said: {jj}")

    #Screenshot
        elif 'screenshot' in query:
            Speak("taken screenshot, now give the path & name do save the file")
            SS()
            Speak("Task Completed")

    #Application Launch/ Shut
        
        if 'chrome' in query:
            OpenApps()
        elif 'close chrome browser' in query:
            CloseApps()
        elif 'firefox' in query:
            OpenApps()
        elif 'close firefox browser' in query:
            CloseApps()        
        elif 'cut' in query:
            OpenApps()        
        elif 'close snipping' in query:
            CloseApps()

    #Internet Speed Testt
        elif 'internet speed' in query:
            SpeedTest()
        elif 'download' in query:
            SpeedTest()
        elif 'upload' in query:
            SpeedTest()

    #Temp.
        elif 'temperature in ' in query:
            Temp()

    #Break Statements
        elif 'break' in query:
            Speak("Ok Sir. I take a leave Let me know if you need anything")
            break
        elif 'sleep' in query:
            Speak("By Sir, I take a leave Let me know if you need anything")
            break
        elif 'good night' in query:
            Speak("Good Night Sir")
            break
        elif 'goodnight' in query:
            Speak("Good Night Sir")
            break
        elif 'stop' in query:
            Speak("Sorry Sir I was not able to full filled your tasked, I will stop running")
            break
        elif'allow me to edit' in query:
            Speak("Sure, hope you will make me better")

TaskExe()
