try:
    import pyttsx3
    import speech_recognition as sr
    import webbrowser
    from conv import random_text
    from Random_sentences import sentences
    from check_battery import *
    from happy import Happy
    from random_advice import *
    from Joke import *
    import random
    import time
    import os
    import re
    import yt_dlp
    import wikipedia
    import pywhatkit as kit
    import requests
    from email.message import EmailMessage
    import smtplib
    import imdb
    import wolframalpha
    import subprocess as sp
    from datetime import datetime
    import datetime
    from plyer import notification
    import pyautogui
    import mtranslate
    from Main_Brain import search_and_save
    from device_info import get_info
    

    def all():
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
            text = random.choice(sentences)
            speak(text)
        
          

        def listen():
            recognizer = sr.Recognizer()
            recognizer.dynamic_energy_adjustment_damping = 0.1
            recognizer.dynamic_energy_ratio = 0.4
            recognizer.dynamic_energy_threshold = False
            recognizer.energy_threshold = 100
            recognizer.pause_threshold = 0.3
            recognizer.operation_timeout = None
            recognizer.non_speaking_duration = 0.2

            with sr.Microphone() as source:
                # print("Listening...", flush=True)
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source, phrase_time_limit=3)  # Time limit added
            
            try:
                text = recognizer.recognize_google(audio, language="en-IN")
                text=mtranslate.translate(text,to_language="en-in")
                # print(f"You said: {text}")
                return text.lower()
            except sr.UnknownValueError:
                # speak("Sorry, I didn't catch that. Can you repeat sir?")
                return None
            except sr.RequestError:
                speak("I’m unable to connect. Please check your internet connection.")
                return None
        
        def send_whatsapp_message():
            speak("What is your message, Bosse?")
            message = listen()

            if not message:
                speak("I didn't hear anything. Please try again.")
                return

            speak(f"Sending your message on WhatsApp.")
            speak(f"Your message is {message}")
            kit.sendwhatmsg_instantly("+91 9918324502", message, wait_time=15)

        def find_my_ip():
            ip_address=requests.get('https://api.ipify.org?format=json').json()
            return ip_address["ip"]

        EMAIL = "ramsinghkus12345@gmail.com"
        PASSWORD = "Ram@455878123"

        def send_email(receiver_add,subject,message):
            try:
                email=EmailMessage()
                email['to']=receiver_add
                email['Subject']=subject
                email['From']=EMAIL
                
                email.set_content(message)
                s=smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login(EMAIL,PASSWORD)
                s.send_message(email)
                s.close()
                return True
            except Exception as e:
                print(e)
                return False

        def get_news():
            news_headline=[]
            result=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=f9e6cc903ee34c10a2e2b48ca8104540").json()
            articles=result["articles"]
            for article in articles:
                news_headline.append(article["title"])
            return news_headline[:6]

        def get_ip_location():
            text = random.choice(random_text)
            speak(text)
            try:
                ip_info = requests.get("https://ipinfo.io/json").json()
                city = ip_info.get("city", "Delhi")
                return city
            except requests.exceptions.RequestException as e:
                print("Error occurred while fetching IP location:", e)
                return "Delhi"
            
        def weather_forecast(city):
            api_key = "a6a270b365c923a59cf9db2086008f02"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            try:
                response = requests.get(url)
                res = response.json()
                # print("API Response:", res)
                if res.get("cod") == 200:
                    weather = res["weather"][0]["main"]
                    temp = res["main"]["temp"]
                    feels_like = res["main"]["feels_like"]
                    return weather, temp, feels_like
                else:
                    return None, None ,None
            except Exception:
                print("Error occurred while fetching weather data:\n")
                return None
            

        def subscribe_channel(channel_name): 
            try:
                speak("Opening YouTube Bosse!")
                webbrowser.open("https://www.youtube.com/")
                time.sleep(5)
                speak("Searching for the channel Name!")
                speak("Click on search bar")
                pyautogui.click(x=806, y=125) 
                speak("Type the channel name ")
                pyautogui.write(channel_name, interval=0.1)
                speak("Press Enter")
                pyautogui.press('enter')
                time.sleep(5)
                speak("Clicking on the channel")
                pyautogui.moveTo(638, 700, duration=1)
                pyautogui.click()
                time.sleep(5)
                speak("Clicking on the Subscribe button")
                pyautogui.moveTo(700, 608, duration=1)
                pyautogui.click()
                time.sleep(2)
                speak("Clicking on the Bell icon")
                pyautogui.moveTo(806, 607, duration=1)
                pyautogui.click()
                time.sleep(2)
                speak("Selecting All notifications")
                pyautogui.moveTo(705, 657, duration=1)
                pyautogui.click()
                time.sleep(2)
                speak(f"Successfully subscribed and enabled notifications for {channel_name}!")

            except Exception as e:
                speak(f"An error occurred: {str(e)}")
                
                
        def search_wikipedia(query):
            try:
                result = wikipedia.summary(query, sentences=2)
                print(result,"\n")
                speak(result)
            except Exception as e:
                speak("I did not understand your question Bosse!.")
                print("Error:", e)

        
        def get_first_youtube_link(query):
            ydl_opts = {
                'quiet': True,
                'extract_flat': True,
                'force_generic_extractor': True,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                search_url = f"ytsearch1:{query}"
                info = ydl.extract_info(search_url, download=False)
                
                if 'entries' in info and len(info['entries']) > 0:
                    return info['entries'][0]['url']
                return None


        def main():
                
            while True:
                command = listen()
                if command: 
                    if "search Wikipedia" in command or "search wikipedia" in command or "wikipedia" in command or "Wikipedia" in command.lower():
                        speak("What would you like to search on Wikipedia Bosse?")
                        search_query = listen()
                        text = random.choice(random_text)
                        speak(text)
                        if search_query:
                            search_wikipedia(search_query)

                    
                    elif "music" in command or "play music" in command or "lucky play song" in command:
                        speak("What music would you like to play Bosse?")
                        search_query = listen()
                        if search_query:
                            speak(f"Playing {search_query} on YouTube.")
                            video_link = get_first_youtube_link(search_query)
                            if video_link:
                                webbrowser.open(video_link)
                                speak("enjoy bosse ")
                            else:
                                speak("Sorry, I couldn't find the song on YouTube Bosse.")
                            time.sleep(2)
                        else:
                            pass
                    
                    elif "navigate forward" in command or "forward jao" in command:
                        speak("Navigating forward to the next page.")
                        pyautogui.hotkey("alt", "right")

                    elif "zoom in on the current page" in command or "current page me zoom in" in command:
                        speak("Zooming in on the current page.")
                        pyautogui.hotkey("ctrl", "+")
                        
                    elif "zoom out on the current page" in command or "current page me zoom out" in command or "zoom" in command:
                        speak("Zooming out on the current page.")
                        pyautogui.hotkey("ctrl", "-")

                    elif "reset the zoom level" in command or "zoom reset karo" in command:
                        speak("Resetting the zoom level to default.")
                        pyautogui.hotkey("ctrl", "0")
                    
                    elif "how are you lucky" in command or "how are you" in command or "kaise ho lucky" in command.lower():
                        text3 = random.choice(Happy)
                        speak(text3)
                    
                    elif "search google" in command or "search on google" in command or "lucky search on google" in command:
                        command=command.replace("lucky","")
                        command=command.replace("search google","")
                        command=command.replace("lucky search on google","")
                        speak("What would you like to search on Google, Bosse?")
                        search_query = listen()
                        if search_query:
                            speak(f"Searching for {search_query} on Google.")
                            webbrowser.open(f"https://www.google.com/search?q={search_query}")
                            time.sleep(2)
                        else:
                            None
                    
                    elif "close tab" in command or "lucky close all tab" in command or "close all tab" in command or "close all tabs lucky" in command:
                        speak("I am closing all open tabs Bosse.")
                        os.system("taskkill /im chrome.exe /f")
                        time.sleep(1)
                    
                    elif "open" in command:
                        query=command.replace("open","")
                        speak("I Am Working Bosse.")
                        pyautogui.press("super")
                        pyautogui.sleep(2)
                        pyautogui.typewrite(query)
                        speak(f"Type {query}")
                        pyautogui.sleep(2)
                        pyautogui.press("enter")
                        speak("Press Enter")
                    
                    elif "check battery" in command or "check battery persent" in command or "check battery persentage" in command or "Check battery" in command or "battery" in command or "Battery" in command:
                        battery_percentage()
                        
                    elif "close window" in command or "Close window" in command or "Close" in command or "remove window" in command  or "hata do" in command  or "hatao" in command  or "band karo" in command or "close" in command:
                        pyautogui.hotkey("alt","f4")
                        random_dlg=random.choice(closedlg)
                        speak(random_dlg)
                        
                    elif "minimise" in command or "minimise the window" in command or "minimize karoge" in command or "minimize" in command:
                        speak("Minimizing...")
                        pyautogui.hotkey("win", "down")
                        pyautogui.hotkey("win", "down")
                        
                    elif "mute" in command or "Mute" in command or "Stop the mike" in command:
                        pyautogui.press("volumemute")

                    elif "write" in command or "likho" in command or "right" in command:
                        speak("Writing")
                        command = command.replace("write", "").replace("likho", "").replace("right", "")
                        pyautogui.write(command)
                        
                    elif "enter" in command or "press enter" in command or "send" in command:
                        pyautogui.press("enter")
                        
                    elif "select all" in command or 'select all paragraph' in command or "Select" in command:
                        pyautogui.hotkey("ctrl", "a")
                        
                    elif "copy" in command or 'copy this' in command:
                        pyautogui.hotkey("ctrl", "c")
                        
                    elif "paste" in command or 'paste here' in command:
                        pyautogui.hotkey("ctrl", "v")
                        
                    elif "undo" in command or 'undo karo' in command:
                        pyautogui.hotkey("ctrl", "z")

                    elif "copy last paragraph" in command:
                        pyautogui.hotkey("ctrl", "shift", "c")

                    elif "increase volume" in command or "volume badhao" in command or "increase the volume" in command:
                        for _ in range(5):
                            pyautogui.press("volumeup")
                        speak("Volume increased.")

                    elif "Decrees volume" in command or "volume kam karo" in command or "decrease the volume" in command or "Reduce volume" in command or "decrease volume" in command:
                        for _ in range(5):
                            pyautogui.press("volumedown")
                        speak("Volume decreased.")    
                        
                    elif "full volume" in command or "full volume kr do" in command:
                        for _ in range(15):
                            pyautogui.press("volumeup")
                        speak("Now your system is at full volume.")
    
                    elif "launch" in command or "Lunch" in command:
                        Nameofweb = command.replace("launch ", "").strip()
                        speak(f"Launching {Nameofweb}")
                        Link = f"https://www.{Nameofweb}.com"
                        webbrowser.open(Link)     
                    
                    elif "scroll up" in command or "Do it" in command or "And up" in command or "do it" in command:
                        pyautogui.scroll(500) 
                        
                    elif "scroll down" in command or "Do down" in command or "And down" in command:
                        pyautogui.scroll(-500) 
                        
                    elif "play" in command or "pause" in command or "stop" in command:
                        pyautogui.press("space")
                        
                    elif command.startswith("search"):
                        pyautogui.hotkey("/") 
                        command = command.replace("search", "").strip()
                        
                        pyautogui.write(command)
                        time.sleep(3)
                        pyautogui.press("enter")
                        
                        speak(f"Searching {command}")
                            
                    elif "restore window" in command:
                        speak("Restoring Window.")
                        pyautogui.hotkey("win", "shift", "up")

                    
                    elif "switch window" in command or "next window" in command or "Witch next window" in command or "Witch window" in command or "Next window" in command:
                        speak("Switching to Next Window.")
                        pyautogui.hotkey("alt", "tab")

                   
                    elif "previous window" in command or "back window" in command or "back window" in command or "TVS window" in command:
                        speak("Switching to Previous Window.")
                        pyautogui.hotkey("alt", "shift", "tab")

                    
                    elif "private window" in command:
                        speak("Opening Incognito Window.")
                        pyautogui.hotkey("ctrl", "shift", "n")

                    elif "bookmark page" in command or "save page" in command:
                        speak("Bookmarking Page.")
                        pyautogui.hotkey("ctrl", "d")

                    elif "history" in command or "browse history" in command or "view history" in command:
                        speak("Opening Browsing History.")
                        pyautogui.hotkey("ctrl", "h")

                    elif "download" in command or "download history" in command or "Download history" in command:
                        speak("Opening Downloads History.")
                        pyautogui.hotkey("ctrl", "j")

                    elif "maximize window" in command:
                        speak("Maximizing Window.")
                        pyautogui.hotkey("win", "up")    
                       
                    elif "fullscreen" in command or "full screen" in command:
                        speak("Entering Fullscreen Mode.")
                        pyautogui.hotkey("f11")    
                    
                    elif "save as page" in command or "save as" in command or "Save save" in command:
                        speak("Saving Page As.")
                        pyautogui.hotkey("ctrl", "s")

                    elif "print page" in command or "print" in command:
                        speak("Printing Page.")
                        pyautogui.hotkey("ctrl", "p")


                    elif "scroll to top" in command:
                        speak("Scrolling to Top.")
                        pyautogui.press("home")

                    elif "scroll to bottom" in command:
                        speak("Scrolling to Bottom.")
                        pyautogui.press("end")

                    elif "then" in command or "new tab" in command or "New then" in command:
                        speak("Opening New Tab.")
                        pyautogui.hotkey("ctrl", "t")

                    elif "reopen closed then" in command or "restore closed tab" in command:
                        speak("Reopening Closed Tab.")
                        pyautogui.hotkey("ctrl", "shift", "t")

                    elif "switch to tab" in command or "go to tab" in command:
                        tab_number = ''.join(filter(str.isdigit, command))  # Extract number from text
                        if tab_number:
                            speak(f"Switching to Tab {tab_number}.")
                            pyautogui.hotkey("ctrl", tab_number)
                        else:
                            speak("Please specify a tab number.")
                            
                    elif "show desktop" in command or "hide windows" in command:
                        speak("Showing Desktop.")
                        pyautogui.hotkey("win", "m")
                    
                    elif "notification" in command or "show notification" in command or "Notification" in command:
                        speak("Opening Notification Center.")
                        pyautogui.hotkey("win", "a")

                    elif "lock screen" in command or "lock computer" in command or "switch user" in command or "change user" in command:
                        speak("Locking Screen.")
                        pyautogui.hotkey("win", "l")

                    elif "shutdown" in command or "turn off computer" in command or "shut down" in command or "Shutdown computer" in command:
                        speak("Shutting Down.")
                        pyautogui.hotkey("win", "d")
                        time.sleep(0.5)
                        pyautogui.hotkey("alt", "f4")
                        time.sleep(0.5)
                        pyautogui.press("enter")
                        
                    elif "restart" in command or "reboot" in command:
                        speak("Restarting.")
                        pyautogui.hotkey("win", "d")
                        time.sleep(0.5)
                        pyautogui.hotkey("alt", "f4")
                        time.sleep(0.5)
                        pyautogui.hotkey("alt", "Down")
                        time.sleep(0.5)
                        pyautogui.press("enter")

                        
                    elif "Find ip address" in command or "IP address" in command or "tell me ip address" in command:
                        ip_address=find_my_ip()
                        speak(f"Find you ip address Bosse")
                        print(f"your ip address is {ip_address}")
                        speak(f"you ip address is {ip_address}")
                    
                    elif "send email" in command:
                        speak("On what email address do you want to send, Bosse? Please enter it in the terminal.")
                        receiver_add = input("Email address: ")
                        speak("What should be the subject of the email?")
                        subject = listen()
                        speak("What is the message?")
                        message = listen() 
                        if subject and message:
                            if send_email(receiver_add, subject, message):
                                speak("I have sent the email, Bosse?.")
                                print(f"Your message: {message}")
                            else:
                                speak("Something went wrong. Please check the error log.")
                        else:
                            speak("I couldn't understand the subject or message.")

                    elif "give me news" in command:
                        command=command.replace("give me news","").strip()
                        ip_address=find_my_ip()
                        speak(f"I Am reading Out The latest headline of today,Bosse.")
                        print(get_news(),sep='\n')
                        speak(get_news())
                        
                    elif "weather" in command:
                        city = get_ip_location()
                        print("Detected City:", city)
                        speak(f"Getting weather report for {city}.") 
                        weather, temp, feels_like = weather_forecast(city)
                        if weather:
                            print(f"Description: {weather}\nTemperature: {temp}°C\nFeels Like: {feels_like}°C", sep='\n')
                            speak(f"Also, the weather report says: {weather}.")
                            speak(f"The current temperature is {temp}°C, but it feels like {feels_like}°C.")
                        else:
                            speak("Sorry, I couldn't fetch the weather report. Please try again.")

                    elif "movie" in command or "check movie" in command:
                        movies_db = imdb.IMDb()
                        speak("Please tell me the movie name, Bosse.")  
                        text = listen()
                        movies = movies_db.search_movie(text)
                        speak("Searching for " + text)
                        speak("I found these movies:")

                        for movie in movies[:3]:  
                            try:
                                title = movie["title"]
                                year = movie.get("year", "Year not available")  
                                
                                print(f"{title} - {year}")
                                speak(f"{title} - {year}")

                                info = movie.getID()
                                movie_info = movies_db.get_movie(info)

                                rating = movie_info.get("rating", "Not available")
                                cast = movie_info.get("cast", [])
                                actor_names = [actor["name"] for actor in cast[:5]] if cast else ["No cast info"]
                                plot = movie_info.get('plot outline', 'Plot summary not available')

                                movie_details = f"{title} was released in {year} with IMDb rating of {rating}. It has a cast of {', '.join(actor_names)}. The plot summary of the movie is: {plot}"
                                print(movie_details)
                                speak(movie_details)

                            except Exception as e:
                                print(f"Error fetching details for {movie}: {e}")
                    
                    elif "calculate" in command:
                        try:
                            speak("What would you like me to calculate?")
                            user_input = listen()  
                            app_id = "K94VQL-47L77T95LW"
                            client = wolframalpha.Client(app_id)
                            result = client.query(user_input)
                            
                            try:
                                ans = next(result.results).text
                                print("The Answer Is " + ans)
                                speak("The Answer Is " + ans)
                            except (StopIteration, AttributeError):
                                speak("I couldn't find that. Please try again, Bosse.")
                        except Exception:
                            speak("Wrong Input Bosse.")

                            
                    elif any(x in command.lower() for x in ["what is", "who is", "which is", "define", "definition"]):
                        command=command.replace("what is","").strip()
                        command=command.replace("who is","").strip()
                        command=command.replace("which is","").strip()
                        command=command.replace("define","").strip()
                        command=command.replace("definition","").strip()
                        app_id = "K94VQL-47L77T95LW"
                        client = wolframalpha.Client(app_id)

                        try:
                            match = re.search(r"(what is|who is|which is|define|definition)\s(.+)", command.lower())  
                            if match:
                                query_text = match.group(2)

                                result = client.query(query_text)
                                
                                try:
                                    ans = next(result.results).text
                                except (StopIteration, AttributeError):
                                    for pod in result.pods:
                                        if pod.title.lower() in ["definition", "basic information", "result"]:
                                            ans = pod.text
                                            break
                                    else:
                                        ans = "I couldn't find a proper definition."

                                print("The Answer is: " + ans)
                                speak("The Answer is: " + ans)

                            else:
                                speak("I couldn't find that.")

                        except Exception as e:
                            print("Error:", e)
                            speak("Something went wrong. Please try again.")
                    
                    elif "subscribe" in command:
                        speak("Please tell me the channel name you want to subscribe to.")
                        channel_name = listen()
                        subscribe_channel(channel_name)
                                    
                    elif"send whatsapp" in command or "send whatsapp message" in command:
                        send_whatsapp_message()
                        
                        
                    elif "time batao" in command or "time" in command:
                        now_time = datetime.datetime.now().strftime("%H:%M:%S")
                        print("Current Time is:-" + str(now_time))
                        speak(str(now_time))

                    elif "date batao" in command or "date" in command:
                        now_time = datetime.datetime.now().strftime("%d:%m:%Y")
                        print("Current date is:-" + str(now_time))
                        speak(str(now_time))
                                
                    
                    elif "add new task" in command:
                        task = command.replace("add new task", "").strip()
                        if task != "":
                            speak("Adding new task, Bosse")
                            with open("todo.txt", "a") as file:
                                file.write(task + "\n")
                            speak(f"Your Task ! '{task}' Bosse.")
                        else:
                            None
                    elif "speak task" in command:
                        with open("todo.txt", "r") as file:
                            speak(f"I Am Working Bosse.")
                            speak(f"Your Task ! is !'{file.read()}' Complete Your Task Bosse.")
                    
                    elif "show today work" in command or "aaj ka kam batao" in command:
                        with open("todo.txt", "r") as file:
                            tasks = file.read()
                        notification.notify(
                                title="Your Today's Work",
                                message=tasks 
                                )            
                                
                    elif "hello lucky" in command or "lucky" in command or "Lucky" in command or "laki" in command:
                        command=command.replace("hello lucky","").strip()
                        command=command.replace("lucky","").strip()
                        command=command.replace("Lucky","").strip()
                        command=command.replace("laki","").strip()
                        response_text=search_and_save(command)
                        speak(response_text)
                        
                        
                    elif "Check computer" in command or "computer" in command:
                        command=command.replace("Check computer","")
                        command=command.replace("computer","")
                        speak("what Check computer info")
                        check_query = listen()
                        print(f"Received query: {check_query}")
                        if check_query is None:
                            speak("No input detected. Please try again.")
                            check_query = listen() 
                        get_info(check_query)
                        
                    
                    elif "stop" in command or "goodbye" in command or "lucky stop" in command or "good night lucky" in command or "good night laki" in command:
                        hour = datetime.datetime.now().hour
                        if 21 <= hour or hour < 6:
                            speak("Good Night Bosse, take care!")
                        else:
                            speak("Have a good day, Bosse!")
                    continue
                
                
        greet_me()
        main()
        
        
        
        
    if __name__ == "__main__":
        all()
                  
except Exception as e:
    print(e)
    # while True:
    #     speak("I am not connected to the internet, please connect the Wi-Fi")      



