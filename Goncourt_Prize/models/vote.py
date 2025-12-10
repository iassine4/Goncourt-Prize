# Goncourt_Prize/models/vote.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class Vote:
	id_vote: Optional[int]
	vote_count: int
	fk_id_book: int
