from pydantic import BaseModel

class PersonIn(BaseModel):
    name: str
    email: str
    telephone: str
    id: int 

class PlaceIn(BaseModel):
    name: str
    ubication: str
    type_place: str

class AutorizedPersonnelIn(BaseModel):
    name: str
    email: str
    telephone: str
    id: int
    rolname: str
    roltype: str
    rolcode: int

class EventIn(BaseModel):
    place: PlaceIn
    id: int
    timeIn: int
    timeOut: int
    date: str

class VisitorIn(BaseModel):
    responsible: AutorizedPersonnelIn
    event: EventIn
    name: str 
    email: str
    telephone: str
    id: int

class PackageIn(BaseModel):
    subject: VisitorIn
    name: str
    description: str
    code: int

class RegisterIn(BaseModel):
    subject: PersonIn
    zone: PlaceIn