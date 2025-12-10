# Goncourt_Prize/business/selection_service.py

from typing import Any, Dict, List

from Goncourt_Prize.daos.book_dao import BookDao
from Goncourt_Prize.daos.selection_dao import SelectionDao
from Goncourt_Prize.daos.selection_book_dao import SelectionBookDao


class SelectionService:
    """Logique métier liée aux sélections du prix Goncourt."""

    def __init__(self) -> None:
        self.book_dao = BookDao()
        self.selection_dao = SelectionDao()
        self.selection_book_dao = SelectionBookDao()

    # ---------- LECTURE (pour tout utilisateur) ----------

    def get_selection_books(self, selection_number: int) -> List[Dict[str, Any]]:
        """
        Retourne les livres d'une sélection (1, 2 ou 3) avec auteur, éditeur, etc.
        """
        if selection_number not in (1, 2, 3):
            return []
        return self.book_dao.find_by_selection_number(selection_number)

    # ---------- ECRITURE (pour le président du jury) ----------

    def set_selection_books(self, selection_number: int, book_ids: List[int]) -> bool:
        """
        Met à jour la liste des livres d'une sélection donnée.
        Utilisé par le président pour enregistrer les sélections 2 et 3.

        :param selection_number: 2 ou 3
        :param book_ids: liste d'id_book choisis pour cette sélection
        """
        if selection_number not in (2, 3):
            # Par sécurité, on empêche de modifier la 1ère sélection
            return False

        selection = self.selection_dao.get_by_number(selection_number)
        if selection is None:
            return False

        id_selection = selection.id_selection
        # On supprime d'abord tout ce qui existait pour cette sélection...
        self.selection_book_dao.delete_all_for_selection(id_selection)
        # ...puis on réinsère proprement les nouveaux livres
        for id_book in book_ids:
            self.selection_book_dao.add_book_to_selection(id_selection, id_book)

        return True
