# Goncourt_Prize/models/author.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Author:
    id_author: Optional[int]
    name: str
    biography: Optional[str] = None
