# Goncourt_Prize/business/selection_service.py

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from Goncourt_Prize.daos.book_dao import BookDao
from Goncourt_Prize.daos.selection_dao import SelectionDao
from Goncourt_Prize.daos.selection_book_dao import SelectionBookDao
from Goncourt_Prize.models.book import Book
from Goncourt_Prize.models.selection import Selection


@dataclass
class SelectionService:
    """
    Service métier pour gérer les sélections du Prix Goncourt.

    - Consultation des sélections (1, 2, 3) côté utilisateur.
    - Mise à jour des sélections 2 et 3 côté président du jury.
    """

    book_dao: BookDao
    selection_dao: SelectionDao
    selection_book_dao: SelectionBookDao

    def __init__(self) -> None:
        # Instanciation des DAO utilisés par le service
        self.book_dao = BookDao()
        self.selection_dao = SelectionDao()
        self.selection_book_dao = SelectionBookDao()

    # ------------------------------------------------------------------
    # 			 MÉTHODES DE LECTURE (UTILISATEUR)
    # ------------------------------------------------------------------

    def get_selection_books(self, selection_number: int) -> List[Dict[str, Any]]:
        """
        Retourne la liste des livres pour une sélection donnée (1, 2 ou 3).

        Chaque élément de la liste est un dictionnaire contenant :
        - id_book, title, summary, publication_date, page_count, isbn,
          editor_price, fk_id_author, fk_id_publisher
        - author_name, publisher_name
        - id_selection, selection_number, selection_date
        """
        if selection_number not in (1, 2, 3):
            return []

        # Délègue au BookDao la construction de la requête SQL.
        rows = self.book_dao.find_by_selection_number(selection_number)
        return rows

    def get_first_selection(self) -> List[Dict[str, Any]]:
        """Raccourci pour obtenir la 1ère sélection."""
        return self.get_selection_books(1)

    def get_second_selection(self) -> List[Dict[str, Any]]:
        """Raccourci pour obtenir la 2ème sélection."""
        return self.get_selection_books(2)

    def get_third_selection(self) -> List[Dict[str, Any]]:
        """Raccourci pour obtenir la 3ème sélection (finalistes)."""
        return self.get_selection_books(3)

    def get_book_details(self, id_book: int) -> Optional[Book]:
        """
        Retourne un objet Book pour un id_book donné.
        Permet par exemple d'afficher le détail d'un livre sélectionné.
        """
        return self.book_dao.read(id_book)

    def get_all_books(self) -> List[Book]:
        """
        Retourne tous les livres de la base.
        Utile, côté président, pour choisir quels livres mettre dans une sélection.
        """

        return self.book_dao.read_all()

    # ------------------------------------------------------------------
    # 			 MÉTHODES D'ÉCRITURE (PRÉSIDENT DU JURY)
    # ------------------------------------------------------------------

    def set_selection_books(self, selection_number: int, book_ids: List[int]) -> bool:
        """
        Met à jour complètement la liste des livres d'une sélection donnée.

        - On suppose que la sélection existe déjà (1, 2, 3).
        - On efface d'abord tous les liens pour cette sélection.
        - On insère ensuite les nouveaux couples (id_selection, id_book).

        Utilisation prévue pour la 2e et 3e sélection par le président.
        """
        if selection_number not in (2, 3):
            # On protège la 1ère sélection si on veut la considérer "fixe"
            return False

        selection: Optional[Selection] = self.selection_dao.get_by_number(selection_number)
        if selection is None:
            # Sélection absente en BD → incohérence de données
            return False

        id_selection = selection.id_selection

        # 1) On supprime tout ce qui existait pour cette sélection
        self.selection_book_dao.delete_all_for_selection(id_selection)

        # 2) On ajoute les nouveaux livres
        for id_book in book_ids:
            self.selection_book_dao.add_book_to_selection(id_selection, id_book)

        return True

    def add_single_book_to_selection(self, selection_number: int, id_book: int) -> bool:
        """
        Ajoute un seul livre à une sélection (sans tout réécrire).
        """
        selection: Optional[Selection] = self.selection_dao.get_by_number(selection_number)
        if selection is None:
            return False

        self.selection_book_dao.add_book_to_selection(selection.id_selection, id_book)
        return True

    def clear_selection(self, selection_number: int) -> bool:
        """
        Efface tous les livres d'une sélection donnée.
        Utile si le président veut repartir de zéro sur la 2e ou 3e sélection.
        """
        selection: Optional[Selection] = self.selection_dao.get_by_number(selection_number)
        if selection is None:
            return False

        self.selection_book_dao.delete_all_for_selection(selection.id_selection)
        return True

    # ------------------------------------------------------------------
    # 			 MÉTHODES D'AIDE POUR LA CONSOLE
    # ------------------------------------------------------------------

    def format_selection_for_console(self, selection_number: int) -> str:
        """
        Construit une chaîne de texte prête à afficher dans le menu console
        pour une sélection donnée.
        """
        rows = self.get_selection_books(selection_number)
        if not rows:
            return f"Aucun livre pour la sélection {selection_number}."

        lines: List[str] = []
        header = f"Sélection {selection_number}"
        selection_date = rows[0].get("selection_date")
        if selection_date is not None:
            header += f" (date : {selection_date})"
        lines.append(header)
        lines.append("-" * len(header))

        for row in rows:
            lines.append(f"[{row['id_book']}] {row['title']} - {row['author_name']} ({row['publisher_name']})")

        return "\n".join(lines)
