-- ======================================================================
--   Base de données : Prix Goncourt 2025
--   Script de création conforme au MCD (BOOK, AUTHOR, PUBLISHER, PERSONAGE…)
-- ======================================================================

CREATE DATABASE IF NOT EXISTS goncourt2025
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE goncourt2025;

-- =====================================================
-- TABLE : AUTHOR
-- Un auteur peut écrire plusieurs livres
-- =====================================================
CREATE TABLE author (
    id_author INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    biography TEXT NULL
) ENGINE=InnoDB;

-- =====================================================
-- TABLE : PUBLISHER
-- Un éditeur peut publier plusieurs livres
-- =====================================================
CREATE TABLE publisher (
    id_publisher INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
) ENGINE=InnoDB;

-- =====================================================
-- TABLE : BOOK
-- Un livre a un auteur, un éditeur, et des métadonnées
-- =====================================================
CREATE TABLE book (
    id_book INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    summary TEXT,
    publication_date DATE,
    page_count INT,
    isbn VARCHAR(50),
    editor_price DECIMAL(10,2),

    -- Foreign keys (version demandée)
    fk_id_author INT NOT NULL,
    fk_id_publisher INT NOT NULL,

    CONSTRAINT fk_book_author
        FOREIGN KEY (fk_id_author) REFERENCES author(id_author)
        ON DELETE RESTRICT ON UPDATE CASCADE,

    CONSTRAINT fk_book_publisher
        FOREIGN KEY (fk_id_publisher) REFERENCES publisher(id_publisher)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =====================================================
-- TABLE : PERSONAGE
-- Personnages principaux d'un livre
-- =====================================================
CREATE TABLE personage (
    id_personage INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
) ENGINE=InnoDB;

-- =====================================================
-- TABLE D'ASSOCIATION : BOOK_PERSONAGE (N:N)
-- Un livre peut avoir plusieurs personnages
-- =====================================================
CREATE TABLE book_personage (
    fk_id_book INT NOT NULL,
    fk_id_personage INT NOT NULL,

    PRIMARY KEY (fk_id_book, fk_id_personage),

    CONSTRAINT fk_bc_book
        FOREIGN KEY (fk_id_book) REFERENCES book(id_book)
        ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT fk_bc_personage
        FOREIGN KEY (fk_id_personage) REFERENCES personage(id_personage)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =====================================================
-- TABLE : SELECTION
-- Trois sélections : 1, 2, 3
-- =====================================================
CREATE TABLE selection (
    id_selection INT AUTO_INCREMENT PRIMARY KEY,
    selection_number INT NOT NULL,
    selection_date DATE NOT NULL
) ENGINE=InnoDB;

-- =====================================================
-- TABLE D'ASSOCIATION : SELECTION_BOOK (N:N)
-- Un livre peut apparaître dans plusieurs sélections
-- =====================================================
CREATE TABLE selection_book (
    fk_id_selection INT NOT NULL,
    fk_id_book INT NOT NULL,

    PRIMARY KEY (fk_id_selection, fk_id_book),

    CONSTRAINT fk_sb_selection
        FOREIGN KEY (fk_id_selection) REFERENCES selection(id_selection)
        ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT fk_sb_book
        FOREIGN KEY (fk_id_book) REFERENCES book(id_book)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

-- =====================================================
-- TABLE : VOTE
-- Dernier tour de scrutin : 4 finalistes → nombre de voix
-- =====================================================
CREATE TABLE vote (
    id_vote INT AUTO_INCREMENT PRIMARY KEY,
    fk_id_book INT NOT NULL,
    vote_count INT NOT NULL,

    CONSTRAINT fk_vote_book
        FOREIGN KEY (fk_id_book) REFERENCES book(id_book)
        ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;
-- =====================================================
-- TABLE FUTURE : JURY_MEMBER (authentification)
-- Futur module : vote individuel + authentification
-- =====================================================
CREATE TABLE jury_member (
    id_jury_member INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    is_president BOOLEAN NOT NULL DEFAULT FALSE
) ENGINE=InnoDB;

