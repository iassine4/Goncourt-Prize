# Goncourt_Prize/daos/vote_dao.py

from dataclasses import dataclass
from typing import Optional, List, Dict, Any

from Goncourt_Prize.daos.dao import Dao
from Goncourt_Prize.models.vote import Vote


@dataclass
class VoteDao(Dao[Vote]):
	"""DAO pour la table vote."""

	# ---------------------------------------------------
	# Méthodes CRUD de base (exigées par la classe Dao)
	# ---------------------------------------------------

	def create(self, obj: Vote) -> int:
		"""Insère un vote et renvoie l'id généré."""
		sql = """
			INSERT INTO vote (fk_id_book, vote_count)
			VALUES (%s, %s)
		"""
		params = (obj.fk_id_book, obj.vote_count)
		with Dao.connection.cursor() as cursor:
			cursor.execute(sql, params)
			Dao.connection.commit()
			obj.id_vote = cursor.lastrowid
		return obj.id_vote or 0

	def read(self, id_vote: int) -> Optional[Vote]:
		"""Retourne un Vote à partir de son id."""
		sql = """
			SELECT id_vote, fk_id_book, vote_count
			FROM vote
			WHERE id_vote = %s
		"""
		with Dao.connection.cursor() as cursor:
			cursor.execute(sql, (id_vote,))
			row = cursor.fetchone()
		return Vote(**row) if row else None # type: ignore[arg-type] # à gérer aprés

	def read_all(self) -> List[Vote]:
		"""Retourne la liste de tous les votes."""
		sql = """
			SELECT id_vote, fk_id_book, vote_count
			FROM vote
			ORDER BY id_vote
		"""
		with Dao.connection.cursor() as cursor:
			cursor.execute(sql)
			rows = cursor.fetchall()
		return [Vote(**row) for row in rows] # type: ignore[arg-type] # à gérer aprés

	def update(self, obj: Vote) -> bool:
		"""Met à jour un vote existant."""
		if obj.id_vote is None:
			return False
		sql = """
			UPDATE vote
			SET fk_id_book = %s,
				vote_count = %s
			WHERE id_vote = %s
		"""
		params = (obj.fk_id_book, obj.vote_count, obj.id_vote)
		with Dao.connection.cursor() as cursor:
			affected = cursor.execute(sql, params)
			Dao.connection.commit()
		return affected == 1

	def delete(self, obj: Vote) -> bool:
		"""Supprime un vote."""
		if obj.id_vote is None:
			return False
		sql = "DELETE FROM vote WHERE id_vote = %s"
		with Dao.connection.cursor() as cursor:
			affected = cursor.execute(sql, (obj.id_vote,))
			Dao.connection.commit()
		return affected == 1

	# ---------------------------------------------------
	# Méthodes spécifiques au projet Goncourt
	# ---------------------------------------------------

	@staticmethod
	def delete_all_votes() -> None:
		"""Supprime tous les votes (avant une nouvelle saisie)."""
		sql = "DELETE FROM vote"
		with Dao.connection.cursor() as cursor:
			cursor.execute(sql)
			Dao.connection.commit()

	def upsert_vote_for_book(self, fk_id_book: int, vote_count: int) -> None:
		"""
		Crée ou met à jour le vote pour un livre donné.
		(utile si tu veux modifier les votes sans tout effacer)
		"""
		sql_select = """
			SELECT id_vote, fk_id_book, vote_count
			FROM vote
			WHERE fk_id_book = %s
		"""
		with Dao.connection.cursor() as cursor:
			cursor.execute(sql_select, (fk_id_book,))
			row = cursor.fetchone()

		if row is None:
			# Création
			vote = Vote(id_vote=None, fk_id_book=fk_id_book, vote_count=vote_count)
			self.create(vote)
		else:
			# Mise à jour
			vote = Vote(**row) # type: ignore[arg-type] # à gérer aprés
			vote.vote_count = vote_count
			self.update(vote)

	@staticmethod
	def find_vote_results_with_books() -> List[Dict[str, Any]]:
		"""
		Retourne les résultats du vote avec les infos livre, auteur et éditeur.
		"""
		sql = """
			SELECT
				v.id_vote,
				v.fk_id_book,
				v.vote_count,
				b.title,
				a.name AS author_name,
				p.name AS publisher_name
			FROM vote AS v
			JOIN book AS b
				ON v.fk_id_book = b.id_book
			JOIN author AS a
				ON b.fk_id_author = a.id_author
			JOIN publisher AS p
				ON b.fk_id_publisher = p.id_publisher
			ORDER BY v.vote_count DESC, b.title
		"""
		with Dao.connection.cursor() as cursor:
			cursor.execute(sql)
			rows: List[Dict[str, Any]] = cursor.fetchall() # type: ignore[arg-type] # à gérer aprés
		return rows
