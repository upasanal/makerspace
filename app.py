import speech_recognition as sr
import pyttsx3
import sys


recognizer = sr.Recognizer()


while True: 
    
    
    try:
        with sr.Microphone() as mic: 
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            
            text = recognizer.recognize_google(audio)
            text = text.lower()
            
            print(f"{text}")
            sys.stdout.flush()
            
    except sr.UnknownValueError: 
        
        recognizer = sr.Recognizer()
        continue
    
    except sr.RequestError as e: 
        print("Google server problem")
        sys.stdout.flush()
        continue