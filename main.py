from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from typing import Dict, Any, Optional
from unkey.py import Unkey
import os
from dotenv import load_dotenv

app = FastAPI(title="My Awesome API", version="1.0.0")

class Person(BaseModel):
    id: int
    name: str
    age: int
    email: str
    city: str

async def verify_api_key(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="API key required")
    
    # Extract key from "Bearer <key>" format
    if authorization.startswith("Bearer "):
        key = authorization[7:]
    else: key=authorization

    try:
        with Unkey(root_key=os.getenv("UNKEY_ROOT_KEY")) as unkey:
            res = unkey.keys.verify_key(key=key)

            if not res.valid:
                raise HTTPException(status_code=401, detail="Invalid API key")
            
            return res
    except Exception as e:
        raise HTTPException(status_code=500, detail="Key verification fails: {str(e)}")
    
@app.get("/person", response_model=Person)
def get_person(key_info = Depends(verify_api_key)) -> Person:
    return Person(
        id=1,
        name="John Doe",
        age=30,
        email="john.doe@example.com",
        city="New York"
    )

@app.get("/status", response_model=bool)
def get_status(key_info = Depends(verify_api_key)) -> bool:
    return True