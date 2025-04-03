from webscout import PhindSearch
from datetime import datetime
import os

file_path = "samat_data.txt"
if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("# Search History\n")
def search_and_save(query):
    result = PhindSearch(query) 
    try:
        response = result.ask(query)
    except Exception as e:
        print(f"No Internet connection")
        return
    response_text = None
    if isinstance(response, dict) and "choices" in response:
        choices = response.get("choices", [])
        if choices and "delta" in choices[0] and "content" in choices[0]["delta"]:
            response_text = choices[0]["delta"]["content"]
    if not response_text:
        response_text = "No valid response found."
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # print(f"Answer: {response_text}")
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{timestamp} : {query}{response_text}")
    return response_text 
    
