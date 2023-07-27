
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bardapi import Bard


app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])



class Message(BaseModel):
    session_id: str
    message: str


@app.get("/")
def home():
    return "<b> It's works </b>"


@app.post("/ask")
async def ask(request: Request, message: Message) -> str:
    

    # Send an API request and get a response.
    response = Bard(message.session_id).get_answer(message.message) ['content']
    
    return response
    
