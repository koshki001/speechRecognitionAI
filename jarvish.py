import datetime
import os
import webbrowser

import pyttsx3
import pywhatkit as wk
import speech_recognition as sr
import wikipedia
import cv2

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # change voice of speak to male female with 0 and 1
engine.setProperty('rate', 150)    # change the speed of jarvis with 150 by increasing and decreasing

def speak(audio):
     
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("Ready to comply. What can i do for you?")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1  # listen for 1 second
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en=in')
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

if __name__=="__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'jarvis' in query:
            print("yes sir")
            speak("yes sir")
        elif "how are you" in query:
            print("I am incredible and ready to assist you")
            speak("I am incredible and ready to assist you")

        elif "who are you" in query:
            print("I am Jarvis. Your personal assitant.")
            speak("I am Jarvis Your personal assistant")

        elif "who created you" in query:
            print("I am created by Kaushiki")
            speak("I am created by kaushiki")

        elif "what is" in query:
            speak('searching wikipedia')
            query=query.replace("What is", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'just open google' in query:
            webbrowser.open('google.com')

        elif 'open google' in query:
            speak("What should i search?")
            qry=takeCommand().lower()
            webbrowser.open(f"{qry}")
            results=wikipedia.summary(qry, sentences=1)
            speak(results)

        elif 'just open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open youtube' in query:
            speak("What do you want to watch?")
            qrry=takeCommand().lower()
            wk.playonyt(f"{qrry}")
        elif 'search on youtube' in query:
            query=query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
        elif 'close browser' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        ###############################################

      #  elif 'open paint' in query:
         ##   apath=''
          ##  os.startfile(apath)

        elif 'open notepad' in query:
            npath="C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2401.26.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(npath)

        elif 'close notepad' in query:
            os.system("taskkill /f /im Notepad.exe")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'close command prompt' in query:
            os.system("taskkill /f /im cmd.exe")

        elif 'what is the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "shut down the system" in query:
            os.system("shutdown /r /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "lock the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


        elif "hibernate the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



        elif "open camera" in query:
            print("Not now")

        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Gaurav. further It's a secret")

        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)

        elif ' What is the love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Kaushiki")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Kaushiki")



