/* =======================================================================
   PRIX GONCOURT 2025 – Requêtes de vérification de cohérence
   Schéma utilisé :
     - book(fk_id_author, fk_id_publisher)
     - selection_book(fk_id_selection, fk_id_book)
     - vote(fk_id_book)
   ======================================================================= */

/* -----------------------------------------------------------------------
   1. Vérifier que les 3 sélections existent bien
   ----------------------------------------------------------------------- */
SELECT * FROM selection;

/* -----------------------------------------------------------------------
   2. Vérifier que chaque sélection contient le bon nombre de livres
      1ère sélection : 15 livres
      2e sélection : 8 livres
      3e sélection : 4 finalistes
   ----------------------------------------------------------------------- */
SELECT fk_id_selection AS id_selection, COUNT(*) AS nb_livres
FROM selection_book
GROUP BY fk_id_selection;

/* -----------------------------------------------------------------------
   3. Vérifier la liste complète des livres dans chaque sélection,
      avec leurs titres et auteurs (via fk_id_author).
   ----------------------------------------------------------------------- */

/* --- 1ère sélection ----------------------------------------------------- */
SELECT
    s.selection_number,
    b.id_book,
    b.title,
    a.name AS author
FROM selection_book sb
JOIN selection s
    ON s.id_selection = sb.fk_id_selection
JOIN book b
    ON b.id_book = sb.fk_id_book
JOIN author a
    ON a.id_author = b.fk_id_author
WHERE s.selection_number = 1
ORDER BY b.id_book;

/* --- 2e sélection -------------------------------------------------------- */
SELECT
    s.selection_number,
    b.id_book,
    b.title,
    a.name AS author
FROM selection_book sb
JOIN selection s
    ON s.id_selection = sb.fk_id_selection
JOIN book b
    ON b.id_book = sb.fk_id_book
JOIN author a
    ON a.id_author = b.fk_id_author
WHERE s.selection_number = 2
ORDER BY b.id_book;

/* --- 3e sélection (finalistes) ------------------------------------------ */
SELECT
    s.selection_number,
    b.id_book,
    b.title,
    a.name AS author
FROM selection_book sb
JOIN selection s
    ON s.id_selection = sb.fk_id_selection
JOIN book b
    ON b.id_book = sb.fk_id_book
JOIN author a
    ON a.id_author = b.fk_id_author
WHERE s.selection_number = 3
ORDER BY b.id_book;

/* -----------------------------------------------------------------------
   4. Vérifier que les livres finalistes sont bien ceux qui ont des votes
      (la table vote pointe sur book via fk_id_book).
   ----------------------------------------------------------------------- */
SELECT
    v.id_vote,
    b.id_book,
    b.title,
    v.vote_count
FROM vote v
JOIN book b
    ON b.id_book = v.fk_id_book
ORDER BY v.vote_count DESC;

/* -----------------------------------------------------------------------
   5. Vérifier que les votes correspondent bien au classement que tu as saisi
      (par ex. lauréat + 3 autres finalistes).
   ----------------------------------------------------------------------- */
SELECT
    b.title,
    v.vote_count
FROM vote v
JOIN book b
    ON b.id_book = v.fk_id_book
ORDER BY v.vote_count DESC;

/* -----------------------------------------------------------------------
   6. Vérifier l’intégrité : aucun livre en sélection ne doit être absent
      de la table BOOK (test de cohérence sur fk_id_book).
   ----------------------------------------------------------------------- */
SELECT
    sb.fk_id_selection,
    sb.fk_id_book
FROM selection_book sb
LEFT JOIN book b
    ON b.id_book = sb.fk_id_book
WHERE b.id_book IS NULL;

/* -----------------------------------------------------------------------
   7. Vérifier que tous les livres référencés par VOTE existent bien
      dans la table BOOK (test sur fk_id_book).
   ----------------------------------------------------------------------- */
SELECT
    v.fk_id_book
FROM vote v
LEFT JOIN book b
    ON b.id_book = v.fk_id_book
WHERE b.id_book IS NULL;

/* -----------------------------------------------------------------------
   8. Vérification avancée :
      Vue consolidée de toutes les sélections, avec :
      - numéro de sélection
      - livre
      - auteur
      - éditeur
      - nombre de voix (si finaliste)
   ----------------------------------------------------------------------- */
SELECT
    s.selection_number,
    b.id_book,
    b.title,
    a.name      AS author,
    p.name      AS publisher,
    v.vote_count
FROM selection_book sb
JOIN selection s
    ON s.id_selection = sb.fk_id_selection
JOIN book b
    ON b.id_book = sb.fk_id_book
JOIN author a
    ON a.id_author = b.fk_id_author
JOIN publisher p
    ON p.id_publisher = b.fk_id_publisher
LEFT JOIN vote v
    ON v.fk_id_book = b.id_book
ORDER BY s.selection_number, b.id_book;

/* -----------------------------------------------------------------------
   9. Vérification : pour chaque roman la liste de tous ses personnages
   ----------------------------------------------------------------------- */
SELECT b.id_book, b.title, p.name AS personage
FROM book_personage bp
JOIN book b ON bp.fk_id_book = b.id_book
JOIN personage p ON bp.fk_id_personage = p.id_personage
ORDER BY b.id_book, p.name;