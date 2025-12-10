# Goncourt_Prize/daos/selection_book_dao.py

from dataclasses import dataclass

from Goncourt_Prize.daos.dao import Dao


@dataclass
class SelectionBookDao(Dao[object]):
    """DAO pour la table d'association selection_book."""

    # On n'utilise pas le CRUD générique ici, donc on les laisse vides.
    def create(self, obj: object) -> int:
        raise NotImplementedError

    def read(self, id_entity: int):
        raise NotImplementedError

    def update(self, obj: object) -> bool:
        raise NotImplementedError

    def delete(self, obj: object) -> bool:
        raise NotImplementedError

    def delete_all_for_selection(self, id_selection: int) -> None:
        """Supprime tous les liens d'une sélection donnée."""
        sql = "DELETE FROM selection_book WHERE fk_id_selection = %s"
        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (id_selection,))
            Dao.connection.commit()

    def add_book_to_selection(self, id_selection: int, id_book: int) -> None:
        """Ajoute un livre à une sélection."""
        sql = """
            INSERT INTO selection_book (fk_id_selection, fk_id_book)
            VALUES (%s, %s)
        """
        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (id_selection, id_book))
            Dao.connection.commit()
