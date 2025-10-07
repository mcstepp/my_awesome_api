from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import yaml

load_dotenv()

app = FastAPI(title="My Awesome API", version="1.0.0")

@app.on_event("startup")
async def generate_openapi_yaml():
    with open("openapi.yaml", "w") as f:
        yaml.dump(app.openapi(), f, default_flow_style=False, sort_keys=False)

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

@app.get("/openapi.yaml")
def get_openapi_yaml():
    from fastapi.responses import Response
    openapi_schema = app.openapi()
    yaml_content = yaml.dump(openapi_schema, default_flow_style=False, sort_keys=False)
    return Response(content=yaml_content, media_type="application/x-yaml")