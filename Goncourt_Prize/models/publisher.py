# Goncourt_Prize/models/publisher.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Publisher:
    id_publisher: Optional[int]
    name: str
    