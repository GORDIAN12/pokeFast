from typing import List, Union, Optional
from enum import Enum
from pydantic import BaseModel, validator
from datetime import date
from sqlmodel import SQLModel, Field, Relationship
class GenreURLChoices(Enum):
    FUEGO='fuego'
    ELECTRICO='electrico'
    AGUA='agua'
    PLANTA='planta'



class EvolucionBase(SQLModel):
    subname: str
    fecha_aparicion: date
    poke_id: int | None=Field(foreign_key="pokemon.id")

class Evolucion(EvolucionBase, table=True):
    id: int=Field(default=None, primary_key=True)
    pokemon: "Pokemon" = Relationship(back_populates="evoluciones")

class PokeBase(SQLModel):
    name: str
    tipo1: Optional[str]
    tipo2: Optional[str]=None
    
class PokeCreate(PokeBase):
    tipo1: Optional[str]
    tipo2: Optional[str]=None
    evoluciones: list[EvolucionBase] | None = None

    @validator("tipo1","tipo2", pre=True)
    def check_tipo(cls, value):
        if isinstance(value, list):
            return ','.join(v.title() for v in value)
        return value.title() if isinstance(value, str) else value

class Pokemon(PokeBase, table=True):
    id: int=Field(default=None, primary_key=True)
    evoluciones: list[Evolucion]=Relationship(back_populates="pokemon")
    date_formed: date | None
