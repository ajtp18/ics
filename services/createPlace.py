from models.models import PlaceIn
import json


def create_person(place: PlaceIn):
    with open("data.json", "r") as f:
        data = json.load(f)

    data["people"].append(place.dict())

    with open("data.json", "w") as f:
        json.dump(data, f)

    return {"msg": "Person created succefully"}