from typing import Literal

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter(tags=["Pessoas"])

Role = Literal["funcionario", "administrador"]


class Person(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=80)
    role: Role
    active: bool


class PersonCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    role: Role


class PersonStatusUpdate(BaseModel):
    active: bool


people = [
    Person(id=1, name="Ana Souza", role="funcionario", active=True),
    Person(id=2, name="Bruno Lima", role="funcionario", active=True),
    Person(id=3, name="Carla Mendes", role="administrador", active=True),
]


@router.get("/people", response_model=list[Person])
def list_people():
    return people


@router.get("/people/{person_id}", response_model=Person)
def get_person(person_id: int):
    for person in people:
        if person.id == person_id:
            return person

    raise HTTPException(
        status_code=404,
        detail="Pessoa não encontrada",
    )


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


@router.patch("/people/{person_id}/status", response_model=Person)
def update_person_status(
    person_id: int,
    status_data: PersonStatusUpdate,
):
    for person in people:
        if person.id == person_id:
            person.active = status_data.active
            return person

    raise HTTPException(
        status_code=404,
        detail="Pessoa não encontrada",
    )