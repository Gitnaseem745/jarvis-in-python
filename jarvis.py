import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import smtplib
import time
import requests
import json
import subprocess
import wolframalpha
# from ecapture import ecapture as ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    print("I'm J.A.R.V.I.S.")
    speak("I'm Jarvis")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")

    except Exception as e:
        speak("I'm sorry, but i can't help with that")
        print("I'm sorry, but i can't help with that")
        return "none"
    return query


print("Loading J.A.R.V.I.S.")
speak("Loading JARVIS")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mrnaseem745@gmail.com', 'xxxxxxxx')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Youtube is open now")
            time.sleep(5)

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Google is open now")
            time.sleep(1)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Stackoverflow is open now")
            time.sleep(1)

        elif 'say hello' in query:
            speak("Hello, Mr. Stark")
            print("Hello, Mr. Stark")

        elif 'who are you' in query or 'what can you do' in query:
            speak('I am JARVIS version 1 point 0 your personal assistant. I am programmed to minor tasks like'
                  'opening youtube, google chrome, gmail and stackoverflow, predict time, take a photo, search wikipedia, predict weather'
                  'In diffrent cities, get top headlines news from times of india and you can ask me computational or geographical questions too! ')

        elif 'who made you' in query or 'who create you' in query or 'who discovered you' in query:
            speak("I was built by Naseem Ansari")
            print("I was built by Naseem Ansari")

        elif 'tell me power level' in query:
            speak('we are now runnig on emergency backup power.')

        elif 'jarvis are you up' in query:
            speak('for you sir, always.')

        elif 'hello jarvis' in query:
            speak("oh, hello sir")

        elif 'jarvis you there' in query:
            speak('At you service. sir')

        elif 'play music' in query:
            music_dir = 'E:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Music is playing now")
            time.sleep(1)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            speak(F"Sir, the time is {strTime}")
            time.sleep(1)

        elif 'open code' in query:
            codePath = "C:\\Users\\Administrator\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("Visual studio Code is open now")
            time.sleep(1)

        elif 'open portfolio' in query:
            portPath = "C:\\Users\\Administrator\\Desktop\\PORT.  SITE\\index.html"
            os.startfile(portPath)
            speak("Portfolio Website is open now")
            time.sleep(1)

        elif 'open epic games' in query:
            epicPath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\Win32\\EpicGamesLauncher.exe"
            os.startfile(epicPath)
            speak("Epic games is open now")
            time.sleep(1)

        elif 'email to naseem' in query:

            try:
                speak("What should i say?")
                content = takeCommand()
                to = "mrnaseem745@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry MR. STARK. I am not able to send this email")

        elif 'news' in query:
            news = webbrowser.open_new_tab(
                "https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines from the Times Of India, Happy reading")
            time.sleep(1)

      # elif 'camera' in query or "take a photo" in query:
      #     ec.capture(0,"robo camera", "img.jpg")

        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(1)

        elif 'ask' in query:
            speak("I can answer to computational and geographical questions and what question do you want to ask now")
            question = takeCommand()
            app_id = "HJWLX5-ERHEH33E54"
            client = wolframalpha.Client('HJWLX5-ERHEH33E54')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "weather" in query:
            api_key = "a67f902aeb09f7bb5ba42b73fd8c123c"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif 'log off' in query or 'sign out' in query:
            speak(
                "Ok, your pc will log off in 10 seconds make sure you exit from all applications")
            subprocess.call(["shutdown", "/1"])
            time.sleep(3)


        # if 'shutdown' in query:
        #     speak('Your personal assistant JARVIS is shutting down, Good bye')
        #     print('Your personal assistant JARVIS is shutting down, Good bye')
        #     exit()

# def greet(name):
#   name = input("Enter your name : ")
#   speak("Hello "+name+" ,How are you!")
#   greet(name)
