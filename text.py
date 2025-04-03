import speech_recognition as sr
import mtranslate
from Main_Brain import search_and_save
import pyttsx3
import sys
import time
import datetime
import random


engine = pyttsx3.init()

def speak(audio):
    engine.setProperty('rate', 200) 
    V = engine.getProperty('voices')
    engine.setProperty('voice', V[6].id)
    engine.say(audio)
    engine.runAndWait()

            
            # audio=mtranslate.translate(audio,to_language="hi",from_language="en-in")


USER ='Bosse !'

def greet_me():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak(f"Good Morning {USER}")
    elif 12 <= hour < 16:
        speak(f"Good Afternoon {USER}")
    elif 16 <= hour < 19:
        speak(f"Good Evening {USER}")
    sentences = ["How can I assist you today?", "Hope you're having a great day!", "What can I do for you?"]
    text = random.choice(sentences)
    speak(text)






def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_adjustment_damping = 0.2
    recognizer.dynamic_energy_ratio = 0.4
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        print("Listening...", flush=True)
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source, phrase_time_limit=3)  # Time limit added
    
    try:
        # print("Processing...", flush=True)
        text = recognizer.recognize_google(audio, language="en-IN")
        text=mtranslate.translate(text,to_language="en-in")
        # print(f"You said: {text}")
        return text.lower()        
    except sr.UnknownValueError:
        # print("Sorry, I didn't catch that. Can you repeat?")
        return None
    except sr.RequestError:
        print("I’m unable to connect. Please check your internet connection.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def Main():
    while True:
        command=listen()
        if command: 
            if "hello lucky" in command or "lucky" in command or "Lucky" in command or "laki" in command:
                command=command.replace("hello lucky","").strip()
                command=command.replace("lucky","").strip()
                command=command.replace("Lucky","").strip()
                command=command.replace("laki","").strip()
                response_text=search_and_save(command)
                speak(response_text)
                print(response_text)
        else:
            pass






while True:
    greet_me()
    # listen()
    Main()




































# def print_animated_message(audio):
#     for char in audio:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(0.050)  # Adjust this for speed
#     print()

# # def speak(audio):
# #     t1 = threading.Thread(target=Co_speak, args=(audio,))
# #     t2 = threading.Thread(target=print_animated_message, args=(audio,))
    
# #     t1.start()  
# #     t2.start()  
    
# #     t1.join()  
# #     t2.join()  



