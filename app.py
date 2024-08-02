import speech_recognition as sr
import pyttsx3
import sys
import requests
from threading import Thread
import threading
import time
import multiprocessing
from multiprocessing import Process
import pvporcupine
import struct
import pyaudio
import winsound



recognizer = sr.Recognizer()
engine = pyttsx3.init()
engine_lock = threading.Lock()

url = "http://192.168.149.1:8000/hello"
api_url = " http://127.0.0.1:8000/mock_tour"
action_test_url = "http://192.168.149.1:8000/test"

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def chirp():
    winsound.Beep(500,100)

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



def active_word(): 
    porcupoine = None 
    pa = None 
    audio_stream = None 




    try:
        porcupoine = pvporcupine.create(keywords=["computer","jarvis"])
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupoine.sample_rate,
            channels=1, 
            format=pyaudio.paInt16,
            input = True,
            frames_per_buffer=porcupoine.frame_length
            )
        
    
        while (True):
            pcm = audio_stream.read(porcupoine.frame_length)
            pcm = struct.unpack_from("h" * porcupoine.frame_length, pcm)


            keyword_index = porcupoine.process(pcm)
            if keyword_index >= 0: 
                chirp()
                print("Word detected, now Listening")

                run_tour()
                time.sleep(1)

    

    finally:
        if porcupoine is not None: 
            porcupoine.delete()
        
        if audio_stream is not None: 
            audio_stream.close()

        if pa is not None:
            pa.terminate()





        

#would not be possible without this right here because of windows lack of forking
if __name__ == "__main__":
    active_word()
    
