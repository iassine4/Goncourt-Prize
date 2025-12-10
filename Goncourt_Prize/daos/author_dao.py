# -*- coding: utf-8 -*-

"""
Classe Dao[Author]
"""

# Goncourt_Prize/daos/author_dao.py
from typing import Optional, List
from dataclasses import dataclass
from .dao import Dao
from Goncourt_Prize.models.author import Author

@dataclass
class AuthorDao(Dao[Author]):

	def create(self, author: Author) -> int:
		sql = "INSERT INTO author (name, biography) VALUES (%s, %s)"
		with self.connection.cursor() as cursor:
			cursor.execute(sql, (author.name, author.biography))
			self.connection.commit()
			return cursor.lastrowid

	def read_all(self) -> list[Author]:
		sql = "SELECT * FROM author"
		with self.connection.cursor() as cursor:
			cursor.execute(sql)
			rows = cursor.fetchall()
			print("DEBUG rows =", rows)
			for r in rows:
				print("TYPE row =", type(r), r)
		return [Author(**row) for row in rows]

	def read(self, id_author: int) -> Optional[Author]:
		sql = "SELECT * FROM author WHERE id_author = %s"
		with self.connection.cursor() as cursor:
			cursor.execute(sql, (id_author,))
			row = cursor.fetchone()
		if row is None:
			return None
		#print("DEBUG row =", row, type(row))
		print("DEBUG dataclass fields =", Author.__annotations__)
		return Author(**row)

	def update(self, author: Author) -> bool:
		sql = "UPDATE author SET name=%s, biography=%s WHERE id_author=%s"
		with self.connection.cursor() as cursor:
			cursor.execute(sql, (author.name, author.biography, author.id_author))
			self.connection.commit()
			return cursor.rowcount == 1

	def delete(self, author: Author) -> bool:
		sql = "DELETE FROM author WHERE id_author=%s"
		with self.connection.cursor() as cursor:
			cursor.execute(sql, (author.id_author,))
			self.connection.commit()
			return cursor.rowcount == 1
