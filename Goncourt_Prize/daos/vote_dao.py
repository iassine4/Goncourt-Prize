# Goncourt_Prize/daos/vote_dao.py

from dataclasses import dataclass

from Goncourt_Prize.daos.dao import Dao


@dataclass
class VoteDao(Dao[object]):
    """DAO pour la table vote."""

    def create(self, obj: object) -> int:
        raise NotImplementedError

    def read(self, id_entity: int):
        raise NotImplementedError

    def update(self, obj: object) -> bool:
        raise NotImplementedError

    def delete(self, obj: object) -> bool:
        raise NotImplementedError

    def delete_all_votes(self) -> None:
        """Supprime tous les votes (avant une nouvelle saisie)."""
        sql = "DELETE FROM vote"
        with Dao.connection.cursor() as cursor:
            cursor.execute(sql)
            Dao.connection.commit()

    def insert_vote(self, id_book: int, vote_count: int) -> None:
        """Insère un nombre de voix pour un livre donné."""
        sql = """
            INSERT INTO vote (fk_id_book, vote_count)
            VALUES (%s, %s)
        """
        with Dao.connection.cursor() as cursor:
            cursor.execute(sql, (id_book, vote_count))
            Dao.connection.commit()
