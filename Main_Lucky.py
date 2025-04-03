# import tkinter as tk
# from PIL import Image, ImageTk, ImageEnhance
# from Lucky21 import all
# # from text import listen
# import pygame
# import os
# import threading
# import random

# # Initialize pygame mixer
# pygame.mixer.init()

# # Function to play sound effects
# def play_sound(sound_file):
#     if os.path.exists(sound_file):
#         pygame.mixer.Sound(sound_file).play()
#     else:
#         print(f"Missing sound file: {sound_file}")

# # Function to rotate the logo with a glow effect
# def animate_logo():
#     global logo_tk
#     angle = 0
#     glow_intensity = 1.0
#     glow_direction = 1  # Increasing

#     def update():
#         nonlocal angle, glow_intensity, glow_direction
#         rotated = logo_original.rotate(angle)
#         enhancer = ImageEnhance.Brightness(rotated)
#         glowing_effect = enhancer.enhance(glow_intensity)

#         logo_tk = ImageTk.PhotoImage(glowing_effect)
#         logo_label.config(image=logo_tk)
#         logo_label.image = logo_tk

#         angle += 5  # Rotate step
#         glow_intensity += 0.05 * glow_direction  # Adjust glow
#         if glow_intensity >= 2.0:
#             glow_direction = -1  # Start dimming
#         elif glow_intensity <= 1.0:
#             glow_direction = 1  # Start glowing

#         root.after(50, update)  # Recursive animation using Tkinter's 'after()'

#     update()

# # Create full-screen Sci-Fi UI
# root = tk.Tk()
# root.title("LUCKY.2.3")
# root.geometry("800x600")
# root.attributes("-fullscreen", True)
# root.attributes("-transparentcolor", "black")  # Transparent background
# root.config(bg="black")  # Set background as transparent

# # Load and process the logo
# logo_path = "logo.png"
# if not os.path.exists(logo_path):
#     raise FileNotFoundError("Please add a 'logo.png' file in the script directory.")
# logo_original = Image.open(logo_path).resize((250, 250), Image.LANCZOS)
# logo_tk = ImageTk.PhotoImage(logo_original)

# # Logo Label (Hologram Effect)
# logo_label = tk.Label(root, image=logo_tk, bg="black", cursor="hand2")
# logo_label.place(relx=0.5, rely=0.5, anchor="center")

# # Create the frame for the file display
# file_display_frame = tk.Frame(root, bg="black", highlightthickness=3, highlightbackground="#00FFFF")
# file_display_frame.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-20)

# # Create the Text widget for the file display
# file_display = tk.Text(
#     file_display_frame,
#     bg="black",
#     fg="#00FFFF",
#     font=("Consolas", 14, "bold"),
#     height=6,
#     width=50,
#     wrap="word",
#     highlightthickness=0,
#     state=tk.DISABLED
# )
# file_display.pack()

# def update_text():
#     try:
#         with open("data.txt", "r") as file:
#             content = file.read()
#         file_display.config(state=tk.NORMAL)
#         file_display.delete(1.0, tk.END)
#         file_display.insert(tk.END, content)
#         file_display.config(state=tk.DISABLED)
        
#         # Change the border color based on hover effect
#         file_display_frame.config(highlightbackground="#00FF00" if file_display_frame.cget("highlightbackground") == "#00FFFF" else "#00FFFF")
    
#     except FileNotFoundError:
#         file_display.config(state=tk.NORMAL)
#         file_display.delete(1.0, tk.END)
#         file_display.insert(tk.END, "No file found!")
#         file_display.config(state=tk.DISABLED)
    
#     root.after(500, update_text)
# update_text()

# # def listen_and_save():
# #     while True:
# #         result = "Example Speech Output"  # Replace this with actual listen() function
# #         if result:
# #             with open("data.txt", "w") as file:
# #                 file.write(result)

# # Start listen_and_save function in a background thread
# # thread = threading.Thread(target=listen_and_save)
# # thread.start()

# def exit_fullscreen(event=None):
#     root.attributes("-fullscreen", False)
    
# root.bind("<Escape>", exit_fullscreen)

# # Start animations
# animate_logo()

# # Run the application
# all()
# root.mainloop()











import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageEnhance
from Lucky21 import all
import pygame
import os
import threading
import random

# ✅ Pygame mixer initialize karo
pygame.mixer.init()

# ✅ Sound play karne ka function
def play_sound():
    sound_file = "sound.mp3"
    if os.path.exists(sound_file):
        sound = pygame.mixer.Sound(sound_file)
        sound.set_volume(1.0)  # Full volume
        sound.play()
    else:
        print(f"❌ Missing sound file: {sound_file}")

# 🔹 Tkinter (LUCKY UI) setup
root = tk.Tk()
root.title("LUCKY.2.3")
root.geometry("800x600")
root.attributes("-fullscreen", True)
root.attributes("-transparentcolor", "black")
root.config(bg="black")

# 🔹 Load aur process karo logo
logo_path = "logo.png"
if not os.path.exists(logo_path):
    raise FileNotFoundError("Please add a 'logo.png' file in the script directory.")

logo_original = Image.open(logo_path).resize((250, 250), Image.LANCZOS)
logo_tk = ImageTk.PhotoImage(logo_original)

# 🔹 Logo Label (Hologram Effect)
logo_label = tk.Label(root, image=logo_tk, bg="black", cursor="hand2")
logo_label.place(relx=0.5, rely=0.5, anchor="center")

# ✅ Logo par click karne se sound chalega
logo_label.bind("<Button-1>", lambda e: play_sound())

# 🔹 Animated logo function
def animate_logo():
    global logo_tk
    angle = 0
    glow_intensity = 0.30
    glow_direction = 0.50

    def update():
        nonlocal angle, glow_intensity, glow_direction
        rotated = logo_original.rotate(angle)
        enhancer = ImageEnhance.Brightness(rotated)
        glowing_effect = enhancer.enhance(glow_intensity)

        logo_tk = ImageTk.PhotoImage(glowing_effect)
        logo_label.config(image=logo_tk)
        logo_label.image = logo_tk

        angle += 5
        glow_intensity += 0.05 * glow_direction
        if glow_intensity >= 1.0:
            glow_direction = -0.1
        elif glow_intensity <= 0.50:
            glow_direction = 1

        root.after(50, update)

    update()

# 🔹 Function to listen & save text to file
def listen():
    while True:
        result = "Example Speech Output"  # Speech Recognition ke liye actual function lagana hoga
        if result:
            with open("data.txt", "w") as file:
                file.write(result)

# 🔹 Speech Recognition ko background thread pe start karo
thread = threading.Thread(target=listen)
thread.start()

# 🔹 Exit fullscreen with Escape key
def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)

root.bind("<Escape>", exit_fullscreen)

# 🔹 Start UI animations
animate_logo()

# 🔹 Run UI
root.mainloop()

