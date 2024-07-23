import requests
# import json
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()

url = "http://localhost:11434/api/chat"

class TextIn(BaseModel):
    """Define the HTTP request body"""
    prompt: str

@app.post("/chat")
async def llama3(reqeust : TextIn):
    """sending prompt to local llama3 and get the response"""
    prompt = reqeust.prompt
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

    # response = requests.post(url, headers=headers, json=data)

    # type: str
    # response_text = response.json()["message"]["content"]
    # return response_text
    try:
        response = requests.post(url, headers=headers, json=data)
        response_text = response.json()["message"]["content"]
        return {"response": response_text}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host = "localhost", port= 8066 )
