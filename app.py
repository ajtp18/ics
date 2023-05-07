"""
Income Control System V1.2
Jorge Andres Gandara Oliveros - T00065470
Robert Andres Pantoja Calderon - T00060394
Diego Andres Garcia Alvarez - T00064583
Angelo Alexander Howell Diaz - T00061114
"""

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from logic.crs.person import Person
from logic.crs.person_controller import PersonController

app = FastAPI()
st_object_person = PersonController()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"200": "Welcome To Income Control System API"}


@app.get("/api/person")
async def root_person():
    return st_object_person.show()


@app.post("/api/person")
async def add_person(name: str, email: str, telephone: str, id: int):
    person = Person(name=name, email=email, telephone=telephone, id=id)
    return st_object_person.add(person)


if __name__ == "__main__":
    uvicorn.run(app, port=33507)
