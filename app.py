import speech_recognition as sr
import pyttsx3
import sys
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

url = "http://192.168.149.1:8000/hello"

engine.say("makerspace tour demo code")
engine.runAndWait()


def virtual_tour():
    file = open('tour.txt',"r")
    g = "@"
    for x in g: 
        engine.say(x)
        engine.runAndWait()
        
    file.close()


while True: 
    
    
    try:
        with sr.Microphone() as mic: 
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            
            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            if "hello" or "hi" in text:
                response = requests.post(url)
                print(response)
                
            if "tour" and "makerspace" in text:
                virtual_tour()
                
            
            print(f"{text}")
            sys.stdout.flush()
            
    except sr.UnknownValueError: 
        
        recognizer = sr.Recognizer()
        continue
    
    except sr.RequestError as e: 
        print("Google server problem")
        sys.stdout.flush()
        continue



