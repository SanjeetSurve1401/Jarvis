import pyttsx3
import speech_recognition as sr

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print("  ")
    Assistant.runAndWait()

def takecommand():
    a = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        a.pause_threshold = 1
        audio = a.listen(source)

        try:
            print("Recogning...")
            query = a.recognize_google(audio)
            print(f"You said:{query}")

        except Exception as Error:
            return "none"
        return query.lower()
        
Speak ("Hello Sir")
query = takecommand()

if 'hello' in query:
    Speak("Hello Sir, I'm Back")

elif 'bye' in query:
    Speak("ok sir I take leave")
    
else:
    Speak("inappropriate command")
    