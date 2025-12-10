# Goncourt_Prize/models/personage.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Personage:
    id_personage: Optional[int]
    name: str
