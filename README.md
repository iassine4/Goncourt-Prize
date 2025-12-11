# GoncourtPrize – Application console (Prix Goncourt 2025)

Application Python en mode console permettant de gérer et d’afficher les sélections du Prix Goncourt 2025, en s’appuyant sur une architecture multicouche (modèle, DAO, métier, application) et une base de données MySQL.

##  Objectif fonctionnel

Le prix Goncourt 2025 est attribué après **trois sélections successives** puis un **dernier tour de scrutin**.  
L’application doit permettre, de manière rétroactive :

- À **tout utilisateur** :
  - d’afficher les livres composant chaque sélection (1, 2, 3),
  - avec toutes les informations disponibles :  
    titre, résumé, auteur, éditeur, personnages principaux, date de parution, nombre de pages, ISBN, prix éditeur.

- Au **président du jury** :
  - d’indiquer les livres de la **deuxième** et de la **troisième** sélection,
  - de saisir le **nombre de voix** obtenues par chaque livre lors du dernier tour de scrutin.

- Dans le futur :
  - ajouter une authentification des membres du jury,
  - permettre à chaque membre de voter individuellement,
  - calculer automatiquement les résultats des sélections et du lauréat.

Les données initiales sont stockées dans une base MySQL `goncourt2025`.

---

##  Architecture générale

Le projet s’inspire de l’architecture “École” vue en **Python avancé** :

- **Couche modèle** (`Goncourt_Prize/models`  
  Dataclasses Python représentant les entités métier :
  - `Author`, `Publisher`, `Book`
  - `Selection`, `SelectionBook`
  - `Vote`
  - (futur) `JuryMember`

- **Couche DAO** (`Goncourt_Prize/daos`)  
  Accès à la base MySQL via des classes DAO spécialisées, héritant d’une classe abstraite générique `Dao[T]` :
  - `AuthorDao`
  - `BookDao`
  - `PublisherDao`
  - `SelectionDao`
  - `SelectionBookDao`
  - `VoteDao`

- **Couche métier (business)** (`Goncourt_Prize/business`)  
  Services orchestrant les DAO et contenant la logique métier :
  - `SelectionService` : affichage des sélections, construction des objets complets (books + author + publisher + personages…)
  - `VoteService` : gestion des votes finaux (saisie, mise à jour, consultation)
  - (évolutif) `JuryService` : gestion des membres et de l’authentification

- **Couche application / console**  
  - `Goncourt_Prize/console_app.py` : point d’entrée de l’application console
  - `main.py` à la racine du projet pour lancer `console_app.main()`

---

##  Modèle de données (résumé)

Base : `goncourt2025`

Tables principales :

- `author(id_author, name, biography)`
- `publisher(id_publisher, name)`
- `book(id_book, title, summary, publication_date, page_count, isbn, editor_price, fk_id_author, fk_id_publisher)`
- `personage(id_personage, name)`
- `book_personage(fk_id_book, fk_id_personage)` (N:N)
- `selection(id_selection, selection_number, selection_date)`
- `selection_book(fk_id_selection, fk_id_book)` (N:N)
- `vote(id_vote, fk_id_book, vote_count)`
- `jury_member(id_jury_member, name, username, password, is_president)`

Le script SQL de création et insertion de données se trouve dans :  
`/bdd/goncourt_prize.sql`.

---

