import requests
from Lucky21 import speak

def get_random_advice():
    try:
        res = requests.get("https://api.adviceslip.com/advice").json()
        return res['slip']['advice']  # Fixed bracket issue
    except Exception as e:
        return "Sorry, I couldn't fetch advice."

# Get and speak advice
# advice = get_random_advice()
# speak(advice)
