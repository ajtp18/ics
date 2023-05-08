from models.models import PersonIn
from services.constants import dataPath
import json

def create_person(person: PersonIn):
    with open(dataPath, "r") as f:
        data = json.load(f)

    data["people"].append(person.dict())

    with open(dataPath, "w") as f:
        json.dump(data, f)

    return {"msg": "Person created succefully"}
