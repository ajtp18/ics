from models.models import PersonIn
import json


def create_person(person: PersonIn):
    with open("data.json", "r") as f:
        data = json.load(f)

    data["people"].append(person.dict())

    with open("data.json", "w") as f:
        json.dump(data, f)

    return {"msg": "Person created succefully"}
