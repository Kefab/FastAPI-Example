from pydantic import BaseModel
from typing import Optional, List


class Champion(BaseModel):
    name: str
    rol: str
    position: str
    region: str
    release_year:int


class ChampionResponse(BaseModel):
    id: int
    name: str
    rol: str
    position: str
    region: str
    age: int
