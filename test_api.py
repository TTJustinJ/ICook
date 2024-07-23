url = "http://localhost:8066/chat"
import requests

data = {"prompt": "what kind of dish can I cook with tomato and eggs, just give me 3 choices"}

response = requests.post(url, json = data)

llm_message = response.json()
llm_message = llm_message["response"]
print(llm_message)