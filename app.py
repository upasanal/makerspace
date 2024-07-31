import speech_recognition as sr
import pyttsx3
import sys
import requests
import threading
from threading import Thread
import time



recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine_lock = threading.Lock()

url = "http://192.168.149.1:8000/hello"

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[8].id)
engine.say("makerspace tour demo code")
engine.runAndWait()



def request_wrapper(): 
    requests.post(url)
    
def virtual_tour():
    file = open('tour.txt',"r") #read script
    
    
    for line in file: 
        
        
            engine.say(line)
            engine.runAndWait()
         
        
    file.close()


while True: 
    
    
    try:
        with sr.Microphone() as mic: 
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            
            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            if ("hello" or "hi") and "robot" in text:
                response = requests.post(url)
                print(response)
                
            elif ("tour" and "makerspace") in text:
                
                
                Thread(target=request_wrapper).start()
                Thread(target=virtual_tour).start()
                
                
                
                
            elif("turn" in text) or ("rotate" in text):
                response = requests.post(url)
                print(response)
    
            else:
                pass 
            print(f"{text}")
            sys.stdout.flush()
            
    except sr.UnknownValueError: 
        
        recognizer = sr.Recognizer()
        continue
    
    except sr.RequestError as e: 
        print("Google server problem")
        sys.stdout.flush()
        continue



