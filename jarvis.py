import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install SpeechRecognition
import wikipedia  # pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui  # pip install pyautogui
import psutil  # pip install psutil
import pyjokes  # pip install pyjokes

from wikipedia.wikipedia import search

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("Hi Mario! How are you today?")

def time():
    Time = datetime.datetime.now().strftime('%H:%M:%S')
    speak(Time)

# time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)

# date()

def wishme():
    speak("Welcome back sir!")
    #time()
    #date()
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour > 12 and hour < 18:
        speak("Good afternoon")
    elif hour > 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("Good night")

    speak("At your service. How can I help you?")

# wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
    
        return "None"

    return query

# takeCommand()

# def sendmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login("email@gmail.com", "password")
#     server.sendmail("email@gmail.com", to, content)
#     server.close()

# def screenshot():
#     img = pyautogui.screenshot()
#     img.save("enter a path for saving screenshot")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)

    # battery = psutil.sensors_battery
    # speak("Battery is at ")
    # speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            speak("Going offline...")
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        # elif "send email" in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "email@gmail.com"
        #         sendmail(to, content)
        #         speak("Email sent succesfully")
        #     except Exception as e:
        #         speak(e)
        #         speak("Unable to send the message")
        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath = "enter a path to chrome browser %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query:
            speak("Logging out...")
            os.system("shutdown /l")

        elif "shut down" in query:
            speak("Shutting down...")
            os.system("shutdown /s /t 1")
        
        elif "restart" in query:
            speak("Restarting...")
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            songs_dir = "enter a path to directory"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember for me" in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You said me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you know anything" or "any notes" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that" + remember.read())

        # elif "screenshot" in query:
        #     screenshot()
        #     speak("Screenshot done!")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()


