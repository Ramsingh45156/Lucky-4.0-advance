import pyttsx3

def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200) 
    voices = engine.getProperty('voices')
    if len(voices) > 6:  # Ensure the index exists
        engine.setProperty('voice', voices[6].id)
    else:
        engine.setProperty('voice', voices[0].id)  # Default to first voice
    
    engine.say(audio)
    engine.runAndWait()
    
    
# speak("Hi Lucky at your service. How can I assist you Hey Lucky here. How may I help you?")