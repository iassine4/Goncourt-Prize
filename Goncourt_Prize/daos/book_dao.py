# Goncourt_Prize/daos/book_dao.py

from dataclasses import dataclass
from typing import Optional, Any, Dict, List

from Goncourt_Prize.models.book import Book
from Goncourt_Prize.daos.dao import Dao  # classe générique déjà définie

@dataclass
class BookDao(Dao[Book]):
	"""DAO responsable des accès à la table book."""

	# ------------------------
	# Méthodes CRUD de base
	# ------------------------

	def create(self, book: Book) -> int:
		"""Crée en BD l'entité Book correspondant à l'objet book."""
		sql = """
			INSERT INTO book (
				title, summary, publication_date, page_count,
				isbn, editor_price, fk_id_author, fk_id_publisher
			)
			VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
		"""
		params = (
			book.title,
			book.summary,
			book.publication_date,
			book.page_count,
			book.isbn,
			book.editor_price,
			book.fk_id_author,
			book.fk_id_publisher,
		)
		with Dao.connection.cursor() as cursor:
			cursor.execute(sql, params)
			Dao.connection.commit()
			book.id_book = cursor.lastrowid
		return book.id_book or 0

	def read(self, id_book: int) -> Optional[Book]:
		"""Renvoie le Book correspondant à id_book (ou None s'il n'existe pas)."""
		sql = "
			SELECT
				id_book, title, summary, publication_date, page_count,
				isbn, editor_price, fk_id_author, fk_id_publisher
			FROM book
			WHERE id_book = %s
		"""
		with Dao.connection.cursor() as cursor:
			cursor.execute(sql, (id_book,))
			row = cursor.fetchone()
		return Book(**row) if row else None

	def update(self, book: Book) -> bool:
		#Met à jour en BD l'entité Book correspondant à book."""
		if book.id_book is None:
			return False  # pas de mise à jour possible sans id

		sql = """
			UPDATE book
			SET
				title = %s,
				summary = %s,
				publication_date = %s,
				page_count = %s,
				isbn = %s,
				editor_price = %s,
				fk_id_author = %s,
				fk_id_publisher = %s
			WHERE id_book = %s
		"""
		params = (
			book.title,
			book.summary,
			book.publication_date,
			book.page_count,
			book.isbn,
			book.editor_price,
			book.fk_id_author,
			book.fk_id_publisher,
			book.id_book,
		)
		with Dao.connection.cursor() as cursor:
			affected = cursor.execute(sql, params)
			Dao.connection.commit()
		return affected == 1

	def delete(self, book: Book) -> bool:
		"""Supprime en BD l'entité Book correspondant à book."""
		if book.id_book is None:
			return False
		sql = "DELETE FROM book WHERE id_book = %s"
		with Dao.connection.cursor() as cursor:
			affected = cursor.execute(sql, (book.id_book,))
			Dao.connection.commit()
		return affected == 1

	# ------------------------
	# Méthodes de recherche génériques
	# ------------------------

	@staticmethod
	def find_all() -> list[Book]:
		"""Renvoie la liste de tous les livres."""
		sql = """
			SELECT
				id_book, title, summary, publication_date, page_count,
				isbn, editor_price, fk_id_author, fk_id_publisher
			FROM book
			ORDER BY title
		"""
		with Dao.connection.cursor() as cursor:
			cursor.execute(sql)
			rows = cursor.fetchall()
		return [Book(*row) for row in rows]

	# ---------------------------------------
	# Requêtes spécifiques pour les sélections
	# ---------------------------------------

	@staticmethod
	def find_by_selection_number(selection_number: int) -> list[Dict[str, Any]]:
		"""
		Renvoie tous les livres d'une sélection donnée (1, 2 ou 3),
		avec les infos auteur, éditeur et la date de sélection.

		Retour : liste de dictionnaires (clés = colonnes SQL).
		"""
		sql = """
			SELECT
				b.id_book,
				b.title,
				b.summary,
				b.publication_date,
				b.page_count,
				b.isbn,
				b.editor_price,
				b.fk_id_author,
				b.fk_id_publisher,
				a.name AS author_name,
				p.name AS publisher_name,
				s.id_selection,
				s.selection_number,
				s.selection_date
			FROM selection AS s
			JOIN selection_book AS sb
				ON s.id_selection = sb.fk_id_selection
			JOIN book AS b
				ON sb.fk_id_book = b.id_book
			JOIN author AS a
				ON b.fk_id_author = a.id_author
			JOIN publisher AS p
				ON b.fk_id_publisher = p.id_publisher
			WHERE s.selection_number = %s
			ORDER BY a.name, b.title
		"""
		with Dao.connection.cursor() as cursor:
			cursor.execute(sql, (selection_number,))
			rows: List[Dict[str, Any]] = cursor.fetchall()
		return rows

	def find_first_selection(self) -> list[Dict[str, Any]]:
		"""Raccourci pour la première sélection (1)."""
		return self.find_by_selection_number(1)

	def find_second_selection(self) -> list[Dict[str, Any]]:
		"""Raccourci pour la deuxième sélection (2)."""
		return self.find_by_selection_number(2)

	def find_third_selection(self) -> list[Dict[str, Any]]:
		"""Raccourci pour la troisième sélection (3) = finalistes."""
		return self.find_by_selection_number(3)

	@staticmethod
	def find_finalists_with_votes() -> list[Dict[str, Any]]:
		"""
		Renvoie les finalistes avec le nombre de voix obtenues
		au dernier tour de scrutin.
		"""
		sql = """
			SELECT
				b.id_book,
				b.title,
				b.summary,
				b.publication_date,
				b.page_count,
				b.isbn,
				b.editor_price,
				b.fk_id_author,
				b.fk_id_publisher,
				a.name AS author_name,
				p.name AS publisher_name,
				v.vote_count
			FROM vote AS v
			JOIN book AS b
				ON v.fk_id_book = b.id_book
			JOIN author AS a
				ON b.fk_id_author = a.id_author
			JOIN publisher AS p
				ON b.fk_id_publisher = p.id_publisher
			ORDER BY v.vote_count DESC
		"""
		with Dao.connection.cursor() as cursor:
			cursor.execute(sql)
			rows: List[Dict[str, Any]] = cursor.fetchall()
		return rows

	def read_all(self) -> List[Book]:
		return self.find_all()