import speech_recognition as sr
import pyttsx3
import sys
import requests
from threading import Thread
import threading
import time
import multiprocessing
from multiprocessing import Process



recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine_lock = threading.Lock()

url = "http://192.168.149.1:8000/hello"
api_url = " http://127.0.0.1:8000/mock_tour"
action_test_url = "http://192.168.149.1:8000/test"

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[8].id)



#Request wrapper function for multiprocessing
def request_wrapper(u : str) -> requests: 
    r = requests.post(u)
    return r


#Meat of the program reads the script
def virtual_tour() -> None:
    file = open('tour.txt',"r") 
    for line in file: 
        engine.say(line)
        engine.runAndWait()
        print(line)
         
        
    file.close()

#Event loop for the program, busywait for someone to ask for a tour
def run_tour() -> None:
    recognizer = sr.Recognizer()

    while True: 
        
        #Microphone
        try:
            with sr.Microphone() as mic: 
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                
                text = recognizer.recognize_google(audio)
                text = text.lower()
                
                if ("hello" or "hi") and "robot" in text:
                    request_wrapper()
                    
                elif ("tour" and "makerspace") in text:
                    
                    #Seperate processes for running tour and robot code
                    rwp = Process(target=request_wrapper,args=[url])
                    vtp = Process(target=virtual_tour)

                    vtp.start()
                    rwp.start()

                    rwp.join()
                    vtp.join()
                    
                
                    
                elif("turn" in text) or ("rotate" in text):
                    response = request_wrapper()
                    print(response)

                elif("test" in text): 
                    response = request_wrapper()
                    print(response)

                    
                else:
                    pass 


                print(f"{text}")
                sys.stdout.flush()
                
        except sr.UnknownValueError: 
            
            recognizer = sr.Recognizer()
            continue
        
        except sr.RequestError as e: 
            print(e)
            sys.stdout.flush()
            continue



#would not be possible without this right here because of windows lack of forking
if __name__ == "__main__":

    run_tour()
