# Goncourt_Prize/console_app.py

from typing import Any, Dict, List
from Goncourt_Prize.business.selection_service import SelectionService


def main() -> None:
    selection_service = SelectionService()

    while True:
        print("\n=== Prix Goncourt 2025 ===")
        print("1. Afficher les livres d'une sélection")
        print("0. Quitter")

        choice = input("Votre choix : ").strip()

        if choice == "1":
            _handle_display_selection(selection_service)
        elif choice == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, merci de réessayer.")


def _handle_display_selection(selection_service: SelectionService) -> None:
    """Interaction console : affichage des livres d'une sélection."""

    raw_number = input("Numéro de sélection à afficher (1, 2 ou 3) : ").strip()

    if raw_number not in ("1", "2", "3"):
        print("Numéro de sélection invalide.")
        return

    selection_number = int(raw_number)
    rows: List[Dict[str, Any]] = selection_service.get_selection_books(selection_number)

    if not rows:
        print("Aucun livre trouvé pour cette sélection.")
        return

    print(f"\n=== Sélection {selection_number} ===")
    # On suppose que toutes les lignes ont la même date de sélection
    selection_date = rows[0].get("selection_date")
    if selection_date is not None:
        print(f"Date de la sélection : {selection_date}")

    for row in rows:
        print("-" * 60)
        print(f"Titre      : {row['title']}")
        print(f"Auteur     : {row['author_name']}")
        print(f"Éditeur    : {row['publisher_name']}")
        print(f"Pages      : {row['page_count']}")
        print(f"Prix éditeur : {row['editor_price']} €")
        print(f"ISBN       : {row['isbn']}")
        print("Résumé     :")
        print(row['summary'] or "(Pas de résumé renseigné)")
    print("-" * 60)
