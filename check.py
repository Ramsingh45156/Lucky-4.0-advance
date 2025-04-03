import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, init
from Speak_Mark import speak

init(autoreset=True)

def trans_hindi_to_english(txt):
    return translate(txt, to_language="en")

def trans_english_to_hindi(txt):
    return translate(txt, to_language="hi")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(Fore.LIGHTYELLOW_EX + "सुन रहा हूँ...")
        try:
            audio = recognizer.listen(source, timeout=None)
            recognized_txt = recognizer.recognize_google(audio, language="hi-IN").lower()
            
            if recognized_txt:
                translated_txt = trans_hindi_to_english(recognized_txt)
                print(Fore.RED + "Mr.: " + translated_txt)

                # अब इसका हिंदी में उत्तर देंगे
                reply_hindi = trans_english_to_hindi("I understood what you said.")
                speak(Fore.GREEN + "AI: " + reply_hindi)
                return reply_hindi
        except sr.UnknownValueError:
            print(Fore.YELLOW + "माफ़ करें, मैं समझ नहीं पाया।")
        except sr.RequestError:
            print(Fore.RED + "API अनुपलब्ध है।")

if __name__ == "__main__":
    while True:
        listen()
