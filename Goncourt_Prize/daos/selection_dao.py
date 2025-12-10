# Goncourt_Prize/daos/selection_dao.py

from dataclasses import dataclass
from typing import Optional

from Goncourt_Prize.daos.dao import Dao
from Goncourt_Prize.models.selection import Selection


@dataclass
class SelectionDao(Dao[Selection]):
    """DAO pour la table selection."""

    def create(self, obj: Selection) -> int:  # pas utilisé pour l'instant
        raise NotImplementedError

    def read(self, id_selection: int) -> Optional[Selection]:
        sql = """
            SELECT id_selection, selection_number, selection_date
            FROM selection
            WHERE id_selection = %s
        """
        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (id_selection,))
            row = cursor.fetchone()
        return Selection(**row) if row else None

    def update(self, obj: Selection) -> bool:
        raise NotImplementedError

    def delete(self, obj: Selection) -> bool:
        raise NotImplementedError

    def get_by_number(self, selection_number: int) -> Optional[Selection]:
        """Retourne la sélection (1, 2, 3) à partir de son numéro."""
        sql = """
            SELECT id_selection, selection_number, selection_date
            FROM selection
            WHERE selection_number = %s
        """
        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (selection_number,))
            row = cursor.fetchone()
        return Selection(**row) if row else None
