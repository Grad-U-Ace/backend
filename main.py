from typing import Union

from fastapi import FastAPI
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = FastAPI()
client = OpenAI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/chat")
def answer():
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of the United States?"},
        ]
    )
    return completion.choices[0].message