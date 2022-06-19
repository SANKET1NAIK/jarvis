from ast import operator
from email.mime import audio
from traceback import print_tb
from turtle import st
import cv2
from matplotlib import image
import pyttsx3
import speech_recognition as sr
import datetime
import os
from requests import get
import random
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyautogui
import datetime
import time
import pyjokes
import requests
import psutil
from datetime import date
import speedtest

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# test to speech


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def make_request(url):
    response = requests.get(url)
    return response.text
# to convert voice into text


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)
# to wishme


def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
        print("Good Morning sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir  !")
        print("Good Afternoon sir !")

    else:
        speak("Good Evening sir !")
        print("Good Evening sir !")

    speak("I am jarvis  Please tell me how may I help you")
    print("I am jarvis  Please tell me how may I help you")


if __name__ == "__main__":
    wishme()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'open command prompt' in query:
            print(" Opening Command Prompt ")
            speak('opening command prompt')
            os.system("start cmd")

        elif "open camera" in query:

            cap = cv2.VideoCapture(0)
            speak("opening camera")
            while True:
                ret, img = cap.read()
                cv2.imshow("webcam", img)
                k = cv2.waitKey(50)
                if k == 27:
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = 'E:\music'
            songs = os.listdir(music_dir)
            print(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            # print(results)
            speak(results)

        elif " open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open stack overflow" in query:
            webbrowser.open("stackoverflow.com")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f" {cm}")

        elif "play songs on youtube" in query:
            kit.playonyt("see you again")

        elif 'volume up' in query or 'increase the volume' in query:
            print("Jarvis 2.0 : Increasing the volume")
            speak("Increasing the volume")
            pyautogui.press("volumeup")
        elif 'volume down' in query or 'decrease the volume' in query:
            print("Jarvis 2.0 : Decreasing the volume")
            speak("Decreasing  the volume")
            pyautogui.press("volumedown")
        elif 'volume mute' in query or 'mute' in query:
            print("Jarvis 2.0 : Muting the volume")
            speak("Muting the volume")
            pyautogui.press("volumemute")

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            print("thanks for using me sir, have a good day.")
            sys.exit()

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'your name' in query:
            speak('My name is JARVIS')
        elif 'who made you' in query:
            speak('I was created by sanket in 2021')

        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("please sir hold the screen for few seconds, i am taking sreenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak(
                "i an done sir, the screenshot is saved in our main folder, now i am ready for next command ")
        elif "show me the screenshot" in query:
            try:
                img = image.open('D:\jarvis' + name)
                img.show(img)
                speak("Here it is sir")
                time.sleep(2)

            except IOError:
                speak("Sorry sir, I am unable to display the screenshot")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'cpu' in query:
            cpu()

        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'how much is the battery' in query:
            battery = psutil.sensors_battery()
            percetage = battery.percent
            speak(f"sir our system have {percetage} percent battery ")

        elif "what is the internet speed" in query:

            st = speedtest.Speedtest()
            dl = st.download()
            dl = dl/(1000000)  # converting bytes to megabytes
            up = st.upload()
            up = up/(1000000)
            print(dl, up)
            speak(
                f"Boss, we have {dl} megabytes per second downloading speed and {up} megabytes per second uploading speed")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif "buzzing" in query or "news" in query or "headlines" in query:
            news_res = engine.news()
            speak('Source: The Times Of India')
            speak('Todays Headlines are..')
            for index, articles in enumerate(news_res):
                print.print(articles['title'])
                speak(articles['title'])
                if index == len(news_res)-2:
                    break
            speak('These were the top headlines, Have a nice day Sir!!..')
        speak("sir, do you have any other work")
