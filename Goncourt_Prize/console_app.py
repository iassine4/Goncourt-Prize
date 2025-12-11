# Goncourt_Prize/console_app.py

from typing import List, Dict, Any, Optional

from Goncourt_Prize.business.selection_service import SelectionService
from Goncourt_Prize.models.book import Book
from Goncourt_Prize.business.vote_service import VoteService


def main() -> None:
	"""Point d'entrée de l'application console Prix Goncourt 2025."""
	selection_service = SelectionService()
	vote_service = VoteService()

	while True:
		print("\n=== Prix Goncourt 2025 ===")
		print("1. Mode consultation (utilisateur)")
		print("2. Mode président du jury")
		print("0. Quitter")

		choice = input("Votre choix : ").strip()

		if choice == "1":
			_run_user_mode(selection_service)
		elif choice == "2":
			_run_president_mode(selection_service, vote_service)
		elif choice == "0":
			print("Au revoir !")
			break
		else:
			print("Choix invalide, merci de réessayer.")


# ---------------------------------------------------------------------
# MODE CONSULTATION (UTILISATEUR)
# ---------------------------------------------------------------------

def _run_user_mode(selection_service: SelectionService) -> None:
	"""Boucle de menu pour le mode consultation (utilisateur)."""
	while True:
		print("\n--- Mode consultation ---")
		print("1. Afficher les livres d'une sélection (1, 2 ou 3)")
		print("2. Afficher le détail d'un livre par son id")
		print("0. Retour au menu principal")

		choice = input("Votre choix : ").strip()

		if choice == "1":
			_handle_display_selection(selection_service)
		elif choice == "2":
			_handle_display_book_details(selection_service)
		elif choice == "0":
			break
		else:
			print("Choix invalide.")


def _handle_display_selection(selection_service: SelectionService) -> None:
	"""Affiche une sélection en utilisant format_selection_for_console."""
	selection_number = _input_selection_number(allow_all=True)
	if selection_number is None:
		return

	text = selection_service.format_selection_for_console(selection_number)
	print()
	print(text)


def _handle_display_book_details(selection_service: SelectionService) -> None:
	"""Affiche le détail d'un livre à partir de son id_book."""
	raw_id = input("Id du livre à afficher : ").strip()
	if not raw_id.isdigit():
		print("Id invalide.")
		return

	id_book = int(raw_id)
	book: Optional[Book] = selection_service.get_book_details(id_book)
	if book is None:
		print("Aucun livre trouvé avec cet id.")
		return

	print("\n--- Détail du livre ---")
	print(f"Id          : {book.id_book}")
	print(f"Titre       : {book.title}")
	print(f"Résumé      : {book.summary or '(aucun résumé)'}")
	print(f"Date        : {book.publication_date}")
	print(f"Pages       : {book.page_count}")
	print(f"ISBN        : {book.isbn}")
	print(f"Prix édit.  : {book.editor_price}")
	print(f"id_author   : {book.fk_id_author}")
	print(f"id_publisher: {book.fk_id_publisher}")


# ---------------------------------------------------------------------
# MODE PRÉSIDENT DU JURY
# ---------------------------------------------------------------------

def _run_president_mode(selection_service: SelectionService, vote_service: VoteService) -> None:
	"""Boucle de menu pour le mode président du jury."""
	while True:
		print("\n--- Mode président du jury ---")
		print("1. Afficher les livres d'une sélection")
		print("2. Mettre à jour les livres de la 2e sélection")
		print("3. Mettre à jour les livres de la 3e sélection")
		print("4. Saisir les votes du dernier tour")
		print("5. Afficher les résultats du dernier tour")
		print("0. Retour au menu principal")

		choice = input("Votre choix : ").strip()

		if choice == "1":
			_handle_display_selection(selection_service)
		elif choice == "2":
			_handle_edit_selection(selection_service, 2)
		elif choice == "3":
			_handle_edit_selection(selection_service, 3)
		elif choice == "4":
			_handle_register_votes(vote_service)
		elif choice == "5":
			_handle_display_votes(vote_service)
		elif choice == "0":
			break
		else:
			print("Choix invalide.")

#----------------------------------------------------------------------
# 				handlers pour les selections
#----------------------------------------------------------------------
def _handle_edit_selection(selection_service: SelectionService, selection_number: int) -> None:
	"""
	Permet au président de définir complètement la liste des livres
	d'une sélection (2 ou 3) en appelant set_selection_books.
	"""
	print(f"\n--- Mise à jour de la sélection {selection_number} ---")

	# Affichage de l'état actuel
	print("Sélection actuelle :")
	current_text = selection_service.format_selection_for_console(selection_number)
	print(current_text)
	print()

	print("Entrez les id_book à mettre dans cette sélection,")
	print("séparés par des virgules. Exemple : 1,2,8,11")
	raw = input("Nouvelle liste d'id_book : ").strip()

	if not raw:
		print("Aucune valeur saisie, annulation.")
		return

	try:
		book_ids = [int(part.strip()) for part in raw.split(",") if part.strip()]
	except ValueError:
		print("Format incorrect (attendu : nombres séparés par des virgules).")
		return

	if not book_ids:
		print("Liste vide, annulation.")
		return

	ok = selection_service.set_selection_books(selection_number, book_ids)
	if ok:
		print("Sélection mise à jour avec succès.")
		# Afficher la nouvelle sélection
		print("\nNouvelle sélection :")
		new_text = selection_service.format_selection_for_console(selection_number)
		print(new_text)
	else:
		print("Erreur lors de la mise à jour de la sélection.")

#----------------------------------------------------------------------
# 				"handlers" gestionnaires pour les votes
#----------------------------------------------------------------------
def _handle_register_votes(vote_service: VoteService) -> None:
	"""
	Saisie des votes pour les finalistes (dernier tour).
	Exemple attendu : 11:6,8:4,1:0,2:0
	"""
	print("\n--- Saisie des votes (finalistes) ---")
	print("Entrez les paires (N° du livre:nombre de voix) séparées par des virgules.")
	print("Exemple : 11:6,8:4,1:0,2:0")
	raw = input("Votes : ").strip()

	if not raw:
		print("Aucune valeur saisie, annulation.")
		return

	votes: dict[int, int] = {}
	try:
		for part in raw.split(","):
			if not part.strip():
				continue
			book_str, votes_str = part.split(":")
			fk_id_book = int(book_str.strip())
			vote_count = int(votes_str.strip())
			votes[fk_id_book] = vote_count
	except ValueError:
		print("Format incorrect. Exemple attendu : 11:6,8:4,1:0,2:0")
		return

	vote_service.register_votes(votes)
	print("Votes enregistrés.")


def _handle_display_votes(vote_service: VoteService) -> None:
	"""Affiche les résultats du dernier tour."""
	text = vote_service.format_results_for_console()
	print()
	print(text)

# ---------------------------------------------------------------------
# FONCTIONS UTILITAIRES
# ---------------------------------------------------------------------

def _input_selection_number(allow_all: bool = False) -> Optional[int]:
	"""
	Demande un numéro de sélection à l'utilisateur.
	- Allow_all=True : autorise 1, 2 ou 3.
	- Allow_all=False : pour restreindre (par ex. 2 ou 3) ?!
	"""
	raw = input("Numéro de sélection (1, 2 ou 3) : ").strip()
	if raw not in ("1", "2", "3"):
		print("Numéro de sélection invalide.")
		return None

	number = int(raw)
	if not allow_all and number not in (2, 3):
		print("Cette sélection ne peut pas être modifiée dans ce contexte.")
		return None

	return number
