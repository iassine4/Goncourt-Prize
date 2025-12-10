
# Goncourt_Prize/business/selection_service.py

from typing import Any, Dict, List
from Goncourt_Prize.daos.book_dao import BookDao


class SelectionService:
    """Logique métier liée aux sélections du prix Goncourt."""

    def __init__(self) -> None:
        self.book_dao = BookDao()

    def get_selection_books(self, selection_number: int) -> List[Dict[str, Any]]:
        """
        Retourne les livres d'une sélection (1, 2 ou 3) avec
        titre, auteur, éditeur, date de sélection, etc.
        """
        if selection_number not in (1, 2, 3):
            # On pourrait lever une exception métier ici
            return []

        selection_rows = self.book_dao.find_by_selection_number(selection_number)
        return selection_rows
