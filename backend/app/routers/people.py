from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(tags=["Pessoas"])


class Person(BaseModel):
    id: int
    name: str
    role: str
    active: bool


class PersonCreate(BaseModel):
    name: str
    role: str


people = [
    Person(id=1, name="Ana Souza", role="funcionaria", active=True),
    Person(id=2, name="Bruno Lima", role="funcionario", active=True),
    Person(id=3, name="Carla Mendes", role="administradora", active=True),
]


@router.get("/people", response_model=list[Person])
def list_people():
    return people


@router.post(
    "/people",
    response_model=Person,
    status_code=status.HTTP_201_CREATED,
)
def create_person(person_data: PersonCreate):
    next_id = max(person.id for person in people) + 1

    new_person = Person(
        id=next_id,
        name=person_data.name,
        role=person_data.role,
        active=True,
    )

    people.append(new_person)
    return new_person