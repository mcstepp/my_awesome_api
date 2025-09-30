from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="My Awesome API", version="1.0.0")

class Person(BaseModel):
    id: int
    name: str
    age: int
    email: str
    city: str
    
@app.get("/person", response_model=Person)
def get_person() -> Person:
    return Person(
        id=1,
        name="John Doe",
        age=30,
        email="john.doe@example.com",
        city="New York"
    )

@app.get("/status", response_model=bool)
def get_status() -> bool:
    return True