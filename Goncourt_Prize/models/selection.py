# Goncourt_Prize/models/selection.py
from datetime import date
from dataclasses import dataclass
from typing import Optional

@dataclass
class Selection:
    id_selection: Optional[int]
    selection_number: int
    selection_date: date