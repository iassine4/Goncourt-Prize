from Goncourt_Prize.daos.author_dao import AuthorDao
from Goncourt_Prize.models.author import Author

author_dao = AuthorDao()

print("\n=== TEST READ ===")
author = author_dao.read(1)
print("Auteur ID 1 :", author)

#authors = author_dao.read_all()

# print("\n=== TEST CREATE ===")
# new_author = Author(id_author=None, name="Test DAO", biography="Ceci est un test")
# new_id = author_dao.create(new_author)
# print("ID inséré :", new_id)
#
# print("\n=== TEST UPDATE ===")
# new_author.id_author = new_id
# new_author.biography = "Biographie modifiée"
# updated = author_dao.update(new_author)
# print("Update OK ?", updated)
#
# print("\n=== TEST DELETE ===")
# deleted = author_dao.delete(new_author)
# print("Delete OK ?", deleted)
