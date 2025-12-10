# Goncourt_Prize/models/book.py
from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Book:
	id_book: Optional[int]
	title: str
	summary: Optional[str]
	publication_date: Optional[date]
	page_count: Optional[int]
	isbn: Optional[str]
	editor_price: Optional[float]
	fk_id_author: int
	fk_id_publisher: int
