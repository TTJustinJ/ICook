import requests
# import json


url = "http://localhost:11434/api/chat"

def llama3(prompt):
    """sending prompt to local llama3 and get the response"""
    data = {
        "model": "llama3",
        "temperature": 2,
        "messages": [
            {
                "role": "user",
                "content": prompt

            }
        ],
        "stream": False,
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, json=data)

    # type: str
    response_text = response.json()["message"]["content"]
    return response_text

prompt = "what kind of dish can I cook with tomato and eggs, just give me 3 choices"

response = llama3(prompt= prompt)
print(response)
