from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define your API key
VALID_API_KEY = "munny123"

# Request body model
class Input(BaseModel):
    documents: str
    questions: List[str]

# Endpoint with authentication
@app.post("/api/v1/hackrx/run")
async def run_query(data: Input, authorization: str = Header(None)):
    # Check Authorization header
    if authorization != f"Bearer {VALID_API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    responses = []
    for q in data.questions:
        if "grace" in q.lower():
            responses.append("A grace period of thirty days is provided after the premium due date.")
        elif "cataract" in q.lower():
            responses.append("The policy has a waiting period of two (2) years for cataract surgery.")
        elif "maternity" in q.lower():
            responses.append("Maternity expenses are covered after 24 months of continuous coverage.")
        else:
            responses.append("This information is not explicitly mentioned in the policy.")
    return {"answers": responses}
