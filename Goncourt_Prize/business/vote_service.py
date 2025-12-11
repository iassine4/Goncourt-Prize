# Goncourt_Prize/business/vote_service.py

from dataclasses import dataclass
from typing import Dict, List, Any

from Goncourt_Prize.daos.vote_dao import VoteDao


@dataclass
class VoteService:
    """
    Service métier pour gérer le dernier tour de scrutin.

    - Enregistrement des votes saisis par le président.
    - Lecture des résultats triés par nombre de voix.
    """

    vote_dao: VoteDao

    def __init__(self) -> None:
        self.vote_dao = VoteDao()

    def register_votes(self, votes_by_book_id: Dict[int, int]) -> None:
        """
        Enregistre tous les votes du dernier tour.

        Stratégie simple :
        - on supprime tout
        - on recrée à partir du dictionnaire fourni
        """
        self.vote_dao.delete_all_votes()
        for fk_id_book, vote_count in votes_by_book_id.items():
            self.vote_dao.upsert_vote_for_book(fk_id_book, vote_count)

    def get_vote_results(self) -> List[Dict[str, Any]]:
        """
        Retourne les résultats du vote (livres + auteurs + éditeurs + voix).
        """
        return self.vote_dao.find_vote_results_with_books()

    def format_results_for_console(self) -> str:
        """
        Construit une chaîne de texte prête à afficher dans le menu console.
        """
        rows = self.get_vote_results()
        if not rows:
            return "Aucun vote enregistré."

        lines: List[str] = []
        lines.append("Résultats du dernier tour")
        lines.append("-------------------------")

        rank = 1
        for row in rows:
            lines.append(
                f"{rank}. {row['title']} - {row['author_name']} "
                f"({row['publisher_name']}) : {row['vote_count']} voix"
            )
            rank += 1

        return "\n".join(lines)
