import subprocess
import pyttsx3 
import webbrowser 
import os
import subprocess
import datetime 
import pyautogui
import wikipedia
import speech_recognition as sr
import smtplib
import random
import sys
from tkinter import *
from PIL import Image,ImageTk,ImageSequence
import time
#import pywhatkit
#702
#576  
from pynput.keyboard import Key,Controller
from time import sleep
import requests
import winsound
import operator
from bs4 import BeautifulSoup
import subprocess
from difflib import get_close_matches as find
from os import system



v = pyttsx3.init()
keyboard = Controller()



def recognize_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source , phrase_time_limit=3)

    try:
        print("    ")
        print("Recognizing...")
        print("    ")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)

        return "none"
    query.lower()
    return query
    
    
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        v.say("Good morning Aman!")
        v.runAndWait()
        print("Good morning!")

    elif 12 <= hour < 18:
        v.say("Good afternoon Aman!")
        v.runAndWait()
        print("Good afternoon!")

    else: 
        v.say("Good evening Aman!")
        v.runAndWait()
        print("Good evening!")



def start():
    v.say("I am Jarvis  ,how  can  i  assist  you  sir")
    v.runAndWait()
    print("I am Jarvis  ,how  can  i  assist  you  sir")


def respond(query):


    if query == "jarvis": 
        v.say("yes sir , how i can assist you: ")
        v.runAndWait()
        print("yes sir , how i can assist you:")
           
    elif query == "are you here jarvis"    :
        v.say("yes sir , i am here ")
        v.runAndWait()
        print("yes sir i am here")

    elif "how are you" in query:
        query.replace("jarvis","")
        v.say("I am fine sir ")
        v.runAndWait()
        print("I am fine sir")
        v.say("What about you sir")
        v.runAndWait()
        print('What about you sir')

    elif "i am fine"  in query:
        query.replace("jarvis","")
        v.say("that's good ,how may i help you sir")
        v.runAndWait()
        print("that's good sir")
        v.say("stay always good")
        v.runAndWait()
        print('stay always good')   

    elif "i am also fine"  in query:
        query.replace("jarvis","")
        v.say("that's good ,how may i help you sir")
        v.runAndWait()
        print("that's good sir")
        v.say("stay always good")
        v.runAndWait()
        print('stay always good')       

    elif "thanks for compliment"  in query:
        query.replace("jarvis", "")
        v.say("welcome sir , i am always here to help you ")
        v.runAndWait()
        print("welcome sir , i am always here to help you ")

    elif "thanks for company"  in query:
        query.replace("jarvis", "")
        v.say("welcome sir , i am always here to help you ")
        v.runAndWait()
        print("welcome sir , i am always here to help you ")
   

    elif "thanks for acompany" in query:
        query.replace("jarvis", "")
        v.say("welcome sir , i am always here to help you ")
        v.runAndWait()
        print("welcome sir , i am always here to help you ")    

    elif "close and exit"  in query:
        query.replace("jarvis","")
        v.say("Ok sir exiting and closing vs.code")
        v.runAndWait()
        print("Ok sir exiting and closing vscode")
        v.say("thanks,sir have a nice day")
        v.runAndWait()
        os.system(f'taskkill /F /IM Code.exe')

    elif " exit and close" in query:
        query.replace("jarvis","")
        v.say("Ok sir exiting and closing vs.code")
        v.runAndWait()
        print("Ok sir exiting and closing vscode")
        v.say("thanks,sir have a nice day")
        v.runAndWait()
        os.system(f'taskkill /F /IM Code.exe')   

    elif "close"  in query:
        from offapp import close
        close

    elif " close and shutdown"   in query:
        query.replace("jarvis","")
        v.say("Ok sir exiting and shudowning system")
        v.runAndWait()
        print("Ok sir exiting and shutdowning")
        v.say("thanks,sir have a nice day")
        v.runAndWait()
        os.system("shutdown /s /t 1")

    elif 'exit and shutdown' in query:
        query.replace("jarvis","")
        v.say("Ok sir exiting and shudowning system")
        v.runAndWait()
        print("Ok sir exiting and shutdowning")
        v.say("thanks,sir have a nice day")
        v.runAndWait()
        os.system("shutdown /s /t 1")   

    elif "not good" in query:
        v.say("sir i am sorry to ask")
        v.runAndWait()
        print("sorry to ask sir")
        v.say(" please tell me your problem may be i am able to help you you solve them")  
        v.runAndWait()
        print(" please tell me your problem may be i am able to help you you solve them")

    elif "not fine" in query:
        v.say("sir i am sorry to ask")
        v.runAndWait()
        print("sorry to ask sir")
        v.say(" please tell me your problem may be i am able to help you you solve them")  
        v.runAndWait()
        print(" please tell me your problem may be i am able to help you you solve them")   
    
    elif query == "are you listening to me":
        v.say("yes sir ,i am listening to  you ")
        v.runAndWait()
        print("yes sir")

    elif  "nice jarvis" in query:
        v.say("Thanks sir! if you have any other task for me or need my assistance ,please call me ")
        v.runAndWait()
        print("Thankyou sir! if you have any other task for me or need my assistance ,please call me ")

    elif  "nice " in query:
        v.say("Thanks sir! if you have any other task for me or need my assistance ,please call me ")
        v.runAndWait()
        print("Thankyou sir! if you have any other task for me or need my assistance ,please call me ")
   
    elif query == "hello jarvis":
        v.say("Hello sir,how may i help you ")
        v.runAndWait()
        print("Hello sir ")

    elif "hello" in query:
        v.say("Hello sir,how can i help you ")
        v.runAndWait()
        print("Hello sir")

    elif 'date' in query:
        query = query.replace("jarvis","")
        date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        v.say(f"Today is {date}")
        v.runAndWait()
        print(f"Today is {date}")

    elif 'time' in query:
        query = query.replace("jarvis","")
        time = datetime.datetime.now().strftime("%H:%M:%S")
        v.say(f"The time is {time}")
        v.runAndWait()
        print(f"Today is {time}")

    elif query == "ok":
        v.say(" take care sir! if you need anything don't hesitate to ask ")
        v.runAndWait()
        print(" take care sir! if you need anything don't hesitate to ask")

    elif query == "ok jarvis":
        v.say("ok sir, have a great day")
        v.runAndWait()
        print("ok sir , have a great day") # ##

    elif query == "thanks jarvis":
        v.say("welcome sir , it's my pleasure sir ")
        v.runAndWait()
        print("welcome sir , it's my pleasure")

    elif query == "thanks":
        v.say("welcome sir , it's my pleasure ")
        v.runAndWait()
        print("welcome sir , it's my pleasure ")

    elif query == "ok thanks":
        v.say("welcome  , it's my pleasure sir ")
        v.runAndWait()
        print("welcome sir , it's my pleasure")

    elif query == "ok thanks jarvis":
        v.say("welcome , it's my pleasure ")
        v.runAndWait()
        print("welcome sir , it's my pleasure")

    elif query == "exit":
        query = query.replace("jarvis","")
        v.say("ok sir ,exited ")
        v.runAndWait()
        print("ok sir , exited ")
        exit()
        
    elif query  == "exit jarvis":
        query = query.replace("jarvis","")
        v.say("ok sir goodbye ,exited  ")
        v.runAndWait()
        print("ok sir goodbye , exited ")
        exit()
        
    elif query == 'by nothing':
        query = query.replace("jarvis","")
        v.say('ok sir , if you need my help please call me again ')
        v.runAndWait()
        print("ok sir , if you need my help please call me again")

    elif query == "good morning":
       query = query.replace("jarvis","")
       v.say("good morning sir")
       v.runAndWait()
       print("good morning sir")

    elif query == "good afternoon":
        query = query.replace("jarvis","")
        v.say("good afternoon sir")
        v.runAndWait()
        print("good afternoon sir ")

    elif query == "good evening":
        query = query.replace("jarvis","")
        v.say("good evening sir ")
        v.runAndWait()
        print("good evening sir ")

    elif query == "good night":
        query = query.replace("jarvis","")
        v.say("good night sir having a good nap ")
        v.runAndWait()
        print("good night sir having a good nap")
        exit()

    elif query == "open google":
        query = query.replace("jarvis","")
        v.say("opening  google in  browser ...                                                                                                                                                                                                                                                                                         wait for a moment just loading..")
        v.runAndWait()
        webbrowser.open("www.google.com")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")

    elif query == " edge":
        query = query.replace("jarvis","")
        v.say("opening  edge browser ...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        file = subprocess.Popen("C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")    
        
    elif query == "open browser":
        query = query.replace("jarvis","")
        v.say("opening  edge browser ...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        file = subprocess.Popen("C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")

    elif query == "open edge":
        query = query.replace("jarvis","")
        v.say("opening  edge browser ...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        file = subprocess.Popen("C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")
    
    elif "open word"  in query:
        query = query.replace("jarvis","")
        v.say("opening  word...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        query = ("word")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.press("enter")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")    
   
    elif "open excel"  in query:
        query = query.replace("jarvis","")
        v.say("opening  excel ...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        query = ("excel")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.press("enter")  
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")    

    elif "open access"  in query:
        query = query.replace("jarvis","")
        v.say("opening  access...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        query = ("access")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.press("enter") 
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")    

    elif "open publisher"  in query:
        query = query.replace("jarvis","")
        v.say("opening  publisher ...                                                                                                                                                                                                                                                                                  wait for a moment just loading...")
        v.runAndWait()
        query = ("publisher")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.press("enter")  
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")   

    elif "open one note"  in query:
        query = query.replace("jarvis","")
        v.say("opening  one note...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        query = ("one note")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.press("enter")   
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")     

    elif "open presentaion"  in query:
        query = query.replace("jarvis","")
        v.say("opening  presentation ...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        query = ("presentation")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.press("enter") 
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")      

    elif "open outlook"  in query:
        query = query.replace("jarvis","")
        v.say("opening  outlook ...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        query = ("outlook")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.press("enter")   
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")    

    elif "open photoshop"  in query:
        query = query.replace("jarvis","")
        v.say("opening  photoshop ...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        query = ("photoshop")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.press("enter")  
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")    

    elif "open ImageReady"  in query:
        query = query.replace("jarvis","")
        v.say("opening  imageready ...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        query = ("imageready")
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.press("enter")  
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")                      

    elif query == "edge":
        query = query.replace("jarvis","")
        v.say("opening  edge browser ...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        file = subprocess.Popen("C:\\Program Files (x86)\\Microsoft\Edge\\Application\\msedge")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")   
   
    elif query == "open chrome":
        query = query.replace("jarvis","")
        v.say("opening  chrome browser ...                                                                                                                                                                                                                                                                                         wait for a moment just loading...")
        v.runAndWait()
        file = subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          opened sir")
        v.runAndWait()
        print("opened sir")

    elif query == "open arduino":
        query = query.replace("jarvis","")
        v.say("opening  arduino ...                                                                                                                                                                                                                                                                                         wait for a moment just loading..")
        v.runAndWait()
        file2 = subprocess.Popen("C:\\Program Files (x86)\\Arduino\\arduino.exe")
        v.say ("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               opened sir ")
        v.runAndWait()
        print("opened sir")

    elif query == "open file reader" :
        query = query.replace("jarvis","")
        v.say("opening  adobe reader ...                                                                                                                                                                                                                                                                                         wait for a moment just loading..")
        v.runAndWait()
        file = subprocess.Popen("C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               opened sir ")
        v.runAndWait()
        print("opened sir")

    elif query == "open firefox":
        query = query.replace("jarvis","")
        v.say("opening  firefox...                                                                                                                                                                                                                                                                                         wait for a moment just loading..")
        v.runAndWait()
        file = subprocess.Popen("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                opened sir             ")
        v.runAndWait()

    elif query == "open google drive":
        query = query.replace("jarvis","")
        v.say("opening  google drive ...                                                                                                                                                                                                                                                                                         wait for a moment just loading..")
        v.runAndWait()
        file2 = subprocess.Popen(   "C:\Program Files\Google\Drive File Stream\88.0.0.0\GoogleDriveFS.exe")
        v.say ("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               opened sir ")
        v.runAndWait()
        print("opened sir")

    elif query == "whatsapp":
        query = query.replace("jarvis","")
        v.say("opening  whatsapp ...                                                                                                                                                                                                                                                                                         wait for a moment just loading..")
        v.runAndWait()
        try:
            os.system("Start whatsapp:")
            print("opening whatsapp...")
        except  Exception as e:
            print(f"Error opening whatsapp : {e}")
        v.say('                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    opened sir       '         )
        v.runAndWait()
        print("opened whatsapp sir")

    elif query == "open telegram":
        query = query.replace("jarvis","")
        v.say("opening  telegram desktop...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 wait for a moment just loading..")
        v.runAndWait()
        try:
            os.system("Start telegram-desktop")
            print("opening...")
        except  Exception as e:
            print(f"Error opening telegram desktop: {e}")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   opened sir ")
        v.runAndWait()
        print("opened telegram")

    elif query == "open settings":
        query = query.replace("jarvis","")
        v.say(
            "opening  settings...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 wait for a moment just loading..")
        v.runAndWait()
        try:
            os.system("Start ms-settings:")
            print("opening...")
        except  Exception as e:
            print(f"Error opening telegram desktop: {e}")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   opened sir ")
        v.runAndWait()
        print("opened settings")

    elif query == "open facebook":
        query = query.replace("jarvis","")
        v.say("opening  facebook...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 wait for a moment just loading..")
        v.runAndWait()
        webbrowser.open("www.facebook.com")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   opened sir ")
        v.runAndWait()
        print("opened facebook")

    elif query == "open instagram":
        query = query.replace("jarvis","")
        v.say("opening  instagram...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 wait for a moment just loading..")
        v.runAndWait()
        webbrowser.open("www.instagram.com")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   opened sir ")
        v.runAndWait()
        print("opened instagram")

    elif query == "open snapchat":
        query = query.replace("jarvis","")
        v.say("opening  snapchat...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 wait for a moment just loading..")
        v.runAndWait()
        webbrowser.open("web.snapchat.com")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   opened sir ")
        v.runAndWait()
        print("opened snapchat")

    elif query == "open youtube":
        query = query.replace("jarvis","")
        v.say("opening  youtube...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 wait for a moment just loading..")
        v.runAndWait()
        webbrowser.open("www.youtube.com")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   opened sir ")
        v.runAndWait()
        print("opened youtube")

    elif query == "open chatgpt":
         query = query.replace("jarvis","")
         v.say("opening  chat gpt ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 wait for a moment just loading..")
         v.runAndWait()
         webbrowser.open("chat.openai.com")
         v.say( "                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  opened sir ")
         v.runAndWait()
         print("opened chatgpt")

    elif query == "store":
        query = query.replace("jarvis","")
        v.say("opening microsoft  store...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 wait for a moment just loading..")
        v.runAndWait()
        try:
            os.system("Start ms-windows-store:")
            print("opening...")
        except  Exception as e:
            print(f"Error opening Microsoft store: {e}")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   opened sir ")
        v.runAndWait()
        print("opened store")

    elif query == "open explorer":
        query = query.replace("jarvis","")
        v.say("opening  file explorer...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 wait for a moment just loading..")
        v.runAndWait()
        try:
            os.system("explorer")
            print("opening...")
        except  Exception as e:
            print(f"Error opening explorer: {e}")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   opened sir ")
        v.runAndWait()
        print("opened file explorer")

    elif query == "spotify":
        query = query.replace("jarvis","")
        v.say("opening  spotify ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 wait for a moment just loading..")
        v.runAndWait()
        try:
            os.system("open-spotify:")
            print("opening...")
        except  Exception as e:
            print(f"Error opening spotify: {e}")
        v.say("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   opened sir ")
        v.runAndWait()
        print("opened telegram")

    elif query == 'wikipedia':
        query = query.replace("jarvis","")
        v.say("Searching wikipedia ")
        v.runAndWait()
        query = query.replace( "wikipedia" , "")

        try:
            result = wikipedia.summary(query, sentences=10)
            print(result)
            v.say(result)
            v.runAndWait()
        except:
            print("Due to no internet connection search failed:please check your internet connection")
            v.say("Due to no internet connection wikipedia search failed:")
            v.runAndWait()
    
    elif "search"   in query:
        query = query.replace("jarvis","")
        query = query.replace("search" , "")
        query = query.replace("about" , "")
        query = query.replace("jarvis" , "")
        v.say("Searching sir ...")
        v.runAndWait()
        try:

            googlesearch = f"https://www.google.com/search?q={query}"
            result2 = webbrowser.open(googlesearch)
            v.say("Search completed please have a look on the results")
            v.runAndWait()
        except:
            v.say("Search failed ,due to no internet")
            v.runAndWait()
            print("Due to no internet search failed")
    
    elif "website"   in query:
        query = query.replace("search" , "")
        query = query.replace("about" , "")
        query = query.replace("jarvis" , "")
        query = query.replace("website","")
        v.say("Searching sir ...")
        v.runAndWait()
        try:

            googlesearch = f"https://www.google.com/search?q={query}"
            result2 = webbrowser.open(googlesearch)
            #pywhatkit.playonyt(query)
            v.say("website opened sir")
            v.runAndWait()
        except:
            v.say("Search failed ,due to no internet")
            v.runAndWait()
            print("Due to no internet search failed")        
     
    elif "youtube"   in query:
        query = query.replace("search" , "")
        query = query.replace("youtube" , "")
        query = query.replace("about" , "")
        query = query.replace("jarvis" , "")
        query = query.replace("of" , "")
        query = query.replace("video" , "")
        v.say("Searching sir ...")
        v.runAndWait()
        try:

            youtubesearch = f"https://www.youtube.com/results?search_query={query}"
            result2 = webbrowser.open(youtubesearch)
            v.say("Search completed please have a look on the results")
            v.runAndWait()
        except:
            v.say("Search failed ,due to no internet")
            v.runAndWait()
            print("Due to no internet search failed")  

    elif "screenshot" in query:
        v.say("taking screenshot sir")
        v.runAndWait()
        im = pyautogui.screenshot()     
        im.save("ss.jpg")    
        v.say("have a look on screenshot")
        v.runAndWait()    
        
    elif "shutdown" in query:
        query = query.replace("jarvis","")
        shutdown = v.say("Are you really want to shutdown th system? (yes/no)")  
        v.runAndWait() 
        if shutdown == "y e s":
            v.say("ok sir system is shudowning,have a nice day")
            v.runAndWait()
            print("ok sir system is shudowning,have a nice day")           
            os.system("shutdown /s /t 1")

        elif  shutdown == "yes":
            v.say("ok sir system is shudowning,have a nice day")
            v.runAndWait()
            print("ok sir system is shudowning,have a nice day")
            os.system("shutdown /s /t 1")

        elif shutdown == 'no':
            v.say("system shudown request cancelled")
            v.runAndWait()
            print("systen shutdown request canclled")
            breakpoint()

    elif "app" in query:
        query = query.replace("app" , "")
        query = query.replace("open" , "")
        query = query.replace("jarvis" , "")
        v.say("opening sir........")
        v.runAndWait()
        pyautogui.press("super")
        pyautogui.typewrite(query)
        pyautogui.sleep(1)
        pyautogui.press("enter")
        v.say("app is opened sir,have a look Aman")
        v.runAndWait()
    
    elif "pause" in  query:
        query = query.replace("jarvis","")
        pyautogui.press("k") 
        v.say("video paused")
        v.runAndWait()

    elif "play" in query:
        query = query.replace("jarvis","")
        pyautogui.press("k")
        v.say("video played")
        v.runAndWait()

    elif "mute video" in query:
        query = query.replace("jarvis","")
        pyautogui.press("m")
        v.say("video muted")
        v.runAndWait()

    elif "volume up"  in query:
        query = query.replace("jarvis","")
        v.say("turning volume up")
        v.runAndWait()
        for i in range(5):
            keyboard.press(Key.media_volume_up)
            keyboard.release(Key.media_volume_up)
            sleep(0.1)

    elif "volume down" in query:
        query = query.replace("jarvis","")
        v.say("turning volume down")
        v.runAndWait()
        for i in range(5):
            keyboard.press(Key.media_volume_down)
            keyboard.release(Key.media_volume_down)
            sleep(0.1)
            
    elif "mute" in query:
        query = query.replace("jarvis","")
        v.say("volume muting")
        v.runAndWait()
        pyautogui.press("volumemute")
        sleep(0.1)
    
    elif "alarm" in query:
        v.say("please tell me the time to set alarm")
        #set alarm to 
        query = recognize_command()
        query.replace("jarvis","")
        query.replace("set","")
        query.replace("alarm","")
        query.replace("for","")
        query.replace("to","")
        query.replace(".","")
        query = query.upper()
        v.say("alarm has been set according to the time given by you")
        v.runAndWait()
        
        def alarm(Timings):
            altime = str(datetime.datetime.now().strptime(Timings,"%I:%M %p"))
            
            altime = altime[11:-3]
            print(altime)
            Horeal = altime[:2]
            Horeal = int(Horeal)
            Mireal = altime[3:5]
            Mireal = int(Mireal)
            print(f"Done, alarm is set for{Timings}")

            while True:
                if Horeal==datetime.datetime.now().hour:
                    if Mireal==datetime.datetime.now().minute:
                        print("Alarm is running")
                        winsound.PlaySound("abc",winsound.SND_LOOP)

                elif Mireal<datetime.datetime.now().minute:
                    break
        if __name__ == '__main__':
            alarm()    

    elif "temperature"  in query:
        query.replace("jarvis","")
        try:
            search = 'temperature in jammu'
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            v.say(f"current {search} is  {temp}")
            v.runAndWait()

        except:
            print("Due to no internet connection search failed:please check your internet connection")
            v.say("Due to no internet connection wikipedia search failed:")
            v.runAndWait()

    elif "do some calculations" in query or "calculate" in query or "can you calculate"in query:
        query.replace("jarvis" , "")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            v.say("what you want to calculate sir")
            v.runAndWait()
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        my_string =r.recognize_google(audio)  
        print(my_string) 
        def get_operator_fn(op):
            return {
                "+" : operator.add,
                "-" : operator.sub,
                "x" : operator.mul,
                'divided' :operator.__truediv____,
           } 
            {op}

        def eval_binary_exper(opl, opper, op2):
            opl,op2 = int(opl), int(op2)
            return get_operator_fn(opper) (opl, op2)
        v.say(" result is")
        v.runAndWait()
        v.say(eval_binary_exper(*(my_string.split())))
        v.runAndWait()
        print(eval_binary_exper(*(my_string.split())))

    elif "my photo" in query:
        query = query.replace("jarvis","") 
        pyautogui.press(super)   
        pyautogui.typewrite("camera")
        pyautogui.sleep(4)
        pyautogui.press("enter")
        pyautogui.sleep(2)
        v.say('Smile   please')
        v.runAndWait
        pyautogui.press("enter")

    




    
        
            
def run_jarvis():
    t= Tk()
    t.geometry("1280x620")

    def play():
        t.lift()
        t.attributes("-topmost",True)
        global img
        img = Image.open("gui.gif")
        lbl = Label(t)
        lbl.place(x=0,y=0)
        i = 0

        for img in ImageSequence.Iterator(img):
            img = img.resize((1280,620))
            img = ImageTk.PhotoImage(img)
            lbl.config(image=img)
            t.update()
            time.sleep(0.05)

    play()  

    t.mainloop()

    greet()
    start()
    while True:
        query = recognize_command().lower()
        respond(query)
        

def password():
    v.say("Sir For security purpose please,Write the password First")
    v.runAndWait()
    pin = input("write password first: ")
    
    if pin == "jarvis it's me Aman":
        
        if __name__ == "__main__":
            run_jarvis()
            
    else:
        v.say("password is wrong,try again")
        v.runAndWait()
        v.say("program  code  is exited,try by reruning it")
        v.runAndWait()
        exit()    
       

password()   





# notepad
#close app




