from fastapi import FastAPI
import json

from services.createPerson import create_person
from models.models import PersonIn
from models.models import PlaceIn

app = FastAPI()


@app.get("/people")
async def get_people():
    with open("data.json", "r") as f:
        data = json.load(f)

    return data['people']

@app.get("/places")
async def get_place():
    with open("data.json", "r") as f:
        data = json.load(f)

    return data['places']

@app.post("/person")
async def create(person: PersonIn):
    createPerson = create_person(person)
    return {"Person": createPerson}


@app.post("/place")
async def create_place(place: PlaceIn):
    with open("data.json", "r") as f:
        data = json.load(f)

    data["places"].append(place.dict())

    with open("data.json", "w") as f:
        json.dump(data, f)

    return {"msg": "Place is created succefully"}


