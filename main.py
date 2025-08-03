import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from typing import List
from utils.document_reader import extract_text_from_pdf
from utils.vector_store import get_answer
from utils.auth import verify_token

app = FastAPI()

class Input(BaseModel):
    documents: str
    questions: List[str]

@app.post("/api/v1/hackrx/run")
async def run_query(data: Input, authorization: str = Header(...)):
    if not verify_token(authorization):
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        context = extract_text_from_pdf(data.documents)
        answers = [get_answer(q, context) for q in data.questions]
        return {"answers": answers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
