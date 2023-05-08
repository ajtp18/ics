from models.models import PlaceIn
from services.constants import dataPath
import json


def create_place(place: PlaceIn):
    with open(dataPath, "r") as f:
        data = json.load(f)

    data["places"].append(place.dict())

    with open(dataPath, "w") as f:
        json.dump(data, f)

    return {"msg": "Place is created succefully"}
