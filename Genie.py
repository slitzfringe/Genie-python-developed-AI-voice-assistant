# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 20:16:20 2021

@author: revan
"""

'''lets start a neew project!!!!!'''

''' Revz '''

import pyttsx3 #Is an engine, using sapi for voice, voice = zira
import datetime
import speech_recognition as sr #speech_recognition is represented as sr
#import pyaudio
import wikipedia
import webbrowser
import os
import google

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def greatme():
    hour = int(datetime.datetime.now().hour)
    if hour in range(0,13):
        speak("Good morning")
    elif hour in range(13,4):
        speak("Good afternoon")
    else :
        speak("Good evening")
    speak("Hi Man!, ")    

def command_input():#take command()
    #input is taken from using
    
    inp = sr.Recognizer()
    
    with sr.Microphone() as source: #sr uses microphone for taking input and the string as output!
        print("Listening ... !")
        inp.pause_threshold = 1
        inp.energy_threshold = 700
        audio = inp.listen(source)  #the speack recognised is stored in audio as string!
        
    try:
         #print("recognition.....")
         query = inp.recognize_google(audio,language="en-in")
         print("Query: \n ",query) #can also use f string methond, ie., print(f"Query: {query}/n")
        
    except Exception as e:
         '''
         if the google search engine is unable to recoqnise the audio text
         then this block will be executed'''
         #print(e)
         print("Pardon me!")
         return "None"
    return query
if __name__ == "__main__":
    greatme()
    while(True):
        query = command_input().lower()
        
# execution of the task based on the query
        if "wikipedia" in query:
            speak("Searching in WIKIPEDIA....!")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak ("According to wikipedia")
            print(results)
            speak(results)
            break
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "play music" in query:
            os.system("spotify")
        elif "open whatsapp" in query:
           webbrowser.open("whatsapp.com")
        elif "open telegram" in query:
            webbrowser.open("telegram")
#greatme()
#command_input()
