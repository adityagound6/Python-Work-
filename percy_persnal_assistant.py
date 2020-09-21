import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
import pyaudio

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning sir")
    elif hour>=12 and hour<=6:
        speak("Good afternoon sir")
    else:
        speak("good evening sir")

    speak("I am percy how can I help you ")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recoginizing..")
        query=sr.Recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("I can not here you how caan I help you")
        return "None"
    return query
def sendMail(to,content):
    server=smtplib.SMTP("smpt.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gamil.com','your password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('sir thoda entazar kariye...')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir ,the time is {strTime}")
        elif 'email to harry' in query:
            try:
                speak("what should I say?..sir")
                content=takeCommand()
                sendMail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry my friend harru . ")
