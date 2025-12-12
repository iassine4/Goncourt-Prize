-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : ven. 12 déc. 2025 à 09:52
-- Version du serveur : 8.4.7
-- Version de PHP : 8.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `goncourt2025`
--

-- --------------------------------------------------------

--
-- Structure de la table `author`
--

DROP TABLE IF EXISTS `author`;
CREATE TABLE IF NOT EXISTS `author` (
  `id_author` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `biography` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`id_author`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `author`
--

INSERT INTO `author` (`id_author`, `name`, `biography`) VALUES
(1, 'Nathacha Appanah', 'La journaliste et écrivaine Nathacha Appanah, née en mai 1973 à Mahébourg, est la fille d\'un père ingénieur et d\'une mère institutrice. Elle a un frère cadet.\n\nElle a le créole mauricien comme langue maternelle, Nathacha Devi Pathareddy Appanah, dont la famille descend d\'engagés indiens immigrés à Maurice de langue telougou, écrit en français'),
(2, 'Emmanuel CARRÈRE', 'Emmanuel Carrère, né en 1957 à Paris, est un écrivain, scénariste et réalisateur français. Ancien critique de cinéma, il est devenu l’une des grandes voix de la littérature française contemporaine grâce à des récits mêlant enquête, autobiographie et faits réels, comme \"L’Adversaire\", \"Limonov\" ou \"Le Royaume\".'),
(3, 'David DENEUFGERMAIN', 'David Deneufgermain est psychiatre et écrivain. Après avoir exercé en milieu carcéral, en hôpital psychiatrique et auprès de personnes sans abri, il se présente comme \"écrivain-médecin\". \"L’Adieu au visage\" est son premier roman, nourri par son expérience clinique.'),
(4, 'David DIOP', 'David Diop, né à Paris et élevé au Sénégal, est professeur de littérature du XVIIIᵉ siècle. Il s’est fait connaître avec \"Frère d’âme\", récompensé par de nombreux prix dont le International Booker Prize. Son œuvre explore l’histoire, la mémoire et les héritages coloniaux.'),
(5, 'Ghislaine DUNANT', 'Ghislaine Dunant, née en 1950 à Paris, est romancière et essayiste. Elle est notamment l’autrice de \"Charlotte Delbo, la vie retrouvée\", lauréat du prix Femina de l’essai. Son travail interroge la mémoire, l’amour et les traces laissées par l’histoire.'),
(6, 'Paul GASNIER', 'Paul Gasnier est un romancier français formé à la philosophie et aux sciences sociales. \"La Collision\", enquête littéraire autour d’un fait divers lyonnais, est salué pour son écriture précise et sa réflexion sur la société et le deuil.'),
(7, 'Yanick LAHENS', 'Yanick Lahens, née en 1953 en Haïti, est une grande figure de la littérature haïtienne. Enseignante, essayiste et romancière, elle explore l’histoire, la mémoire et les fractures sociales d’Haïti. Elle s’engage également pour la transmission culturelle dans son pays.'),
(8, 'Caroline LAMARCHE', 'Caroline Lamarche, née en 1955 en Belgique, est romancière, nouvelliste et poétesse. Lauréate du prix Goncourt de la nouvelle et du prix quinquennal de littérature, elle explore l’intime, la mémoire, les corps et les rapports de pouvoir dans une langue très travaillée.'),
(9, 'Hélène LAURAIN', 'Hélène Laurain, née en 1988 à Metz, est une autrice française. Diplômée en sciences politiques et en création littéraire, elle est aussi traductrice de l’allemand. Après \"Partout le feu\" (2022), \"Tambora\" confirme son intérêt pour les luttes écologistes et l’émancipation.'),
(10, 'Charif MAJDALANI', 'Charif Majdalani, né en 1960 à Beyrouth, est un écrivain libanais de langue française. Enseignant à l’Université Saint-Joseph, il construit une œuvre nourrie par l’histoire du Liban, ses guerres civiles et ses grandes familles. Ses romans mêlent sagas, mémoire et politique.'),
(11, 'Laurent MAUVIGNIER', 'Laurent Mauvignier, né en 1967, est un romancier français publié aux Éditions de Minuit. Ses livres abordent les silences familiaux, les traumatismes et la violence sociale. Son style introspectif et sensible est largement salué par la critique littéraire.'),
(12, 'Alfred de MONTESQUIOU', 'Alfred de Montesquiou est écrivain, grand reporter et documentariste. Lauréat du prix Albert-Londres, il a couvert de nombreux conflits à travers le monde. Ses livres et documentaires mêlent enquête historique, géopolitique et récits de terrain.'),
(13, 'Guillaume POIX', 'Guillaume Poix, né en 1986, est écrivain et dramaturge. Ancien élève de l’ENS et de l’ENSATT, il explore dans ses œuvres les questions sociales et politiques, mêlant travail documentaire et fiction. Il est l’auteur de pièces de théâtre et de plusieurs romans.'),
(14, 'Maria POURCHET', 'Maria Pourchet est romancière et sociologue. Docteure en sciences sociales, elle a travaillé sur les représentations littéraires dans les médias. Ses romans sondent le désir, les relations humaines, les classes sociales et les fragilités contemporaines.'),
(15, 'David THOMAS', 'David Thomas est un écrivain français spécialisé dans les micro-fictions et les récits courts. Lauréat du prix Goncourt de la nouvelle, il observe avec humour et sensibilité les vies ordinaires. \"Un frère\" explore la maladie psychique au sein d’une relation fraternelle.');

-- --------------------------------------------------------

--
-- Structure de la table `book`
--

DROP TABLE IF EXISTS `book`;
CREATE TABLE IF NOT EXISTS `book` (
  `id_book` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `summary` text COLLATE utf8mb4_unicode_ci,
  `publication_date` date DEFAULT NULL,
  `page_count` int DEFAULT NULL,
  `isbn` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `editor_price` decimal(10,2) DEFAULT NULL,
  `fk_id_author` int NOT NULL,
  `fk_id_publisher` int NOT NULL,
  PRIMARY KEY (`id_book`),
  KEY `fk_book_author` (`fk_id_author`),
  KEY `fk_book_publisher` (`fk_id_publisher`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `book`
--

INSERT INTO `book` (`id_book`, `title`, `summary`, `publication_date`, `page_count`, `isbn`, `editor_price`, `fk_id_author`, `fk_id_publisher`) VALUES
(1, 'La nuit au coeur', 'Trois recits de femmes confrontees a la violence masculine se repondent entre souvenirs intimes et faits divers, pour explorer la peur, la honte et la reconquete de soi.', '2025-08-21', 288, '9782073080028', 21.00, 1, 1),
(2, 'Kolkhoze', 'Emmanuel Carrere revient sur la figure de sa mere Helene Carrere d Encausse et sur l histoire familiale, en melant deuil, engagement intellectuel et regard critique sur la Russie et l Europe.', '2025-08-28', 560, '9782818061985', 24.00, 2, 2),
(3, 'L\'adieu au visage', 'Pendant le premier confinement de 2020, un psychiatre sillonne une ville vide et les services hospitaliers, cherchant comment continuer a soigner quand la peur, l isolement et la mort envahissent le quotidien.', '2025-08-20', 256, '9782381340647', 21.10, 3, 3),
(4, 'Où s\'adosse le ciel', 'Bilal, poete contemporain, entreprend un voyage vers l Afrique de l Ouest sur les traces d un ancien scribe, et interroge la memoire, la parole et les racines culturelles qui le fondent.', '2025-08-14', 368, '9782260057307', 22.50, 4, 4),
(5, 'Un amour infini', 'Sur l ile de Tenerife en 1964, la rencontre de Louise et Nathan, marques par l Histoire et la Shoah, devient une parenthese amoureuse intense qui confronte le present aux blessures du passe.', '2025-08-20', 170, '9782226498687', 19.90, 5, 5),
(6, 'La collision', 'A partir d un accident mortel de rodeo urbain a Lyon, le recit suit les vies entremellees de la victime, du jeune conducteur et de leurs proches, et montre comment un drame revele les fractures sociales.', '2025-08-21', 176, '9782073101228', 19.00, 6, 1),
(7, 'Passageres de nuit', 'En reliant Saint Domingue, Haiti et la Nouvelle Orleans, le roman retrace sur plusieurs generations le destin de femmes noires descendantes d esclaves, entre memoire familiale, resistance et violence de l histoire.', '2025-08-28', 232, '9782848055701', 20.00, 7, 6),
(8, 'Le bel obscur', 'Une ecrivaine bruxelloise enquete sur un ancetre mysterieux tout en revisitant son mariage avec un homme homosexuel ; en croisant ces deux figures masculines, elle cherche une voie d emancipation et de reconciliation avec elle même.', '2025-08-22', 240, '9782021603439', 22.00, 8, 7),
(9, 'Tambora', 'Une mere raconte ses grossesses compliquees, la perte d un enfant et la croissance de ses deux filles, sous le signe du volcan Tambora, qui devient la metaphore d un corps et d un monde toujours au bord de l eruption.', '2025-08-28', 192, '9782378562588', 18.50, 9, 8),
(10, 'Le nom des rois', 'A Beyrouth dans les annees 1970, un narrateur revient sur l histoire d une famille libanaise prise dans la guerre civile, et questionne ce que signifient la noblesse, le pouvoir et la fidelite a un pays en crise.', '2025-08-20', 288, '9782234097278', 20.00, 10, 9),
(11, 'La maison vide', 'Sur plus d un siecle, une vaste fresque suit plusieurs generations d une famille rurale francaise ; en rouvrant une maison abandonnee, le narrateur met au jour secrets, silences et traumatismes qui traversent l histoire collective.', '2025-08-01', 752, '9782707356741', 25.00, 11, 10),
(12, 'Le crepuscule des hommes', 'A Nuremberg en 1945, le roman suit plusieurs personnages dans l ombre du grand proces, et montre comment des individus ordinaires vivent la fin d un regime et la confrontation avec les crimes nazis.', '2025-08-28', 375, '9782221267660', 22.00, 12, 11),
(13, 'Perpetuite', 'En se placant du cote des surveillants penitentiaires, le livre explore le quotidien de la prison francaise, l usure psychologique du travail et les contradictions d une institution qui pretend rehabiliter tout en enfermant.', '2025-08-21', 331, '9782073105455', 22.00, 13, 12),
(14, 'Tressaillir', 'Apres une separation, Michelle sombre dans une depression severe et retourne sur les lieux de son enfance ; en fouillant ses peurs anciennes, le roman interroge la solitude, le desir et la difficulte de se reconstruire.', '2025-08-20', 336, '9782234097155', 21.90, 14, 9),
(15, 'Un frere', 'David Thomas dresse le portrait de son frere Edouard, atteint de schizophrenie, et raconte a la premiere personne l amour, la culpabilite et le deuil qui entourent cette relation fraternelle.', '2025-08-22', 144, '9782823623376', 19.50, 15, 13);

-- --------------------------------------------------------

--
-- Structure de la table `book_personage`
--

DROP TABLE IF EXISTS `book_personage`;
CREATE TABLE IF NOT EXISTS `book_personage` (
  `fk_id_book` int NOT NULL,
  `fk_id_personage` int NOT NULL,
  PRIMARY KEY (`fk_id_book`,`fk_id_personage`),
  KEY `fk_bc_personage` (`fk_id_personage`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `book_personage`
--

INSERT INTO `book_personage` (`fk_id_book`, `fk_id_personage`) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 4),
(2, 5),
(2, 6),
(2, 7),
(3, 8),
(3, 9),
(3, 10),
(3, 11),
(4, 12),
(4, 13),
(5, 14),
(5, 15),
(6, 16),
(6, 17),
(6, 18),
(7, 19),
(7, 20),
(7, 21),
(7, 22),
(8, 23),
(8, 24),
(8, 25),
(9, 26),
(9, 27),
(9, 28),
(9, 29),
(10, 30),
(10, 31),
(10, 32),
(11, 33),
(11, 34),
(11, 35),
(11, 36),
(12, 37),
(12, 38),
(12, 39),
(12, 40),
(12, 41),
(13, 42),
(13, 43),
(13, 44),
(13, 45),
(14, 46),
(14, 47),
(14, 48),
(14, 49),
(14, 50),
(15, 51),
(15, 52),
(15, 53),
(15, 54),
(15, 55);

-- --------------------------------------------------------

--
-- Structure de la table `jury_member`
--

DROP TABLE IF EXISTS `jury_member`;
CREATE TABLE IF NOT EXISTS `jury_member` (
  `id_jury_member` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_president` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id_jury_member`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Structure de la table `personage`
--

DROP TABLE IF EXISTS `personage`;
CREATE TABLE IF NOT EXISTS `personage` (
  `id_personage` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_personage`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `personage`
--

INSERT INTO `personage` (`id_personage`, `name`) VALUES
(1, 'Nathacha Appanah (narratrice)'),
(2, 'Chahinez Daoud'),
(3, 'Emma'),
(4, 'Hélène Carrère d\'Encausse'),
(5, 'Emmanuel Carrère'),
(6, 'Louis Carrère d\'Encausse'),
(7, 'Georges Zourabichvili'),
(8, 'Narrateur psychiatre'),
(9, 'Équipe mobile de soins'),
(10, 'Patients sans-abri'),
(11, 'Patients Covid'),
(12, 'Bilal Seck'),
(13, 'Ounifer'),
(14, 'Louise'),
(15, 'Nathan'),
(16, 'Narrateur fils endeuillé'),
(17, 'Mère du narrateur'),
(18, 'Saïd'),
(19, 'Élizabeth'),
(20, 'Régina'),
(21, 'Maurice Parmentier'),
(22, 'Général Léonard Corvaseau'),
(23, 'Narratrice écrivaine'),
(24, 'Edmond H.'),
(25, 'Vincent'),
(26, 'Narratrice mère'),
(27, 'Fille aînée'),
(28, 'Deuxième fille'),
(29, 'Enfant perdu'),
(30, 'Narrateur enfant'),
(31, 'Famille du narrateur'),
(32, 'Nawal'),
(33, 'Narrateur de la maison'),
(34, 'Père du narrateur'),
(35, 'Jules'),
(36, 'Marguerite'),
(37, 'Joseph Kessel'),
(38, 'Ilya Ehrenbourg'),
(39, 'Elsa Triolet'),
(40, 'Erika Mann'),
(41, 'Willy Brandt'),
(42, 'Surveillant de nuit 1'),
(43, 'Surveillante de nuit 2'),
(44, 'Surveillant de nuit 3'),
(45, 'Détenu célèbre'),
(46, 'Michelle Darras'),
(47, 'Sirius'),
(48, 'Fille de Michelle et Sirius'),
(49, 'Ariel Zaccaria'),
(50, 'Lycéenne'),
(51, 'David'),
(52, 'Édouard'),
(53, 'Deuxième frère'),
(54, 'Mère des frères'),
(55, 'Père des frères');

-- --------------------------------------------------------

--
-- Structure de la table `publisher`
--

DROP TABLE IF EXISTS `publisher`;
CREATE TABLE IF NOT EXISTS `publisher` (
  `id_publisher` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id_publisher`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `publisher`
--

INSERT INTO `publisher` (`id_publisher`, `name`) VALUES
(1, 'Gallimard'),
(2, 'P.O.L'),
(3, 'Marchialy'),
(4, 'Julliard'),
(5, 'Albin Michel'),
(6, 'Sabine Wespieser'),
(7, 'Seuil'),
(8, 'Verdier'),
(9, 'Stock'),
(10, 'Minuit'),
(11, 'Robert Laffont'),
(12, 'Verticales'),
(13, 'L\'Olivier');

-- --------------------------------------------------------

--
-- Structure de la table `selection`
--

DROP TABLE IF EXISTS `selection`;
CREATE TABLE IF NOT EXISTS `selection` (
  `id_selection` int NOT NULL AUTO_INCREMENT,
  `selection_number` int NOT NULL,
  `selection_date` date NOT NULL,
  PRIMARY KEY (`id_selection`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `selection`
--

INSERT INTO `selection` (`id_selection`, `selection_number`, `selection_date`) VALUES
(1, 1, '2025-09-03'),
(2, 2, '2025-10-07'),
(3, 3, '2025-10-28');

-- --------------------------------------------------------

--
-- Structure de la table `selection_book`
--

DROP TABLE IF EXISTS `selection_book`;
CREATE TABLE IF NOT EXISTS `selection_book` (
  `fk_id_selection` int NOT NULL,
  `fk_id_book` int NOT NULL,
  PRIMARY KEY (`fk_id_selection`,`fk_id_book`),
  KEY `fk_sb_book` (`fk_id_book`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `selection_book`
--

INSERT INTO `selection_book` (`fk_id_selection`, `fk_id_book`) VALUES
(1, 1),
(2, 1),
(3, 1),
(1, 2),
(3, 2),
(1, 3),
(2, 3),
(1, 4),
(2, 4),
(1, 5),
(2, 5),
(1, 6),
(2, 6),
(1, 7),
(1, 8),
(2, 8),
(3, 8),
(1, 9),
(1, 10),
(2, 10),
(1, 11),
(3, 11),
(1, 12),
(1, 13),
(1, 14),
(1, 15);

-- --------------------------------------------------------

--
-- Structure de la table `vote`
--

DROP TABLE IF EXISTS `vote`;
CREATE TABLE IF NOT EXISTS `vote` (
  `id_vote` int NOT NULL AUTO_INCREMENT,
  `fk_id_book` int NOT NULL,
  `vote_count` int NOT NULL,
  PRIMARY KEY (`id_vote`),
  KEY `fk_vote_book` (`fk_id_book`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `vote`
--

INSERT INTO `vote` (`id_vote`, `fk_id_book`, `vote_count`) VALUES
(5, 11, 6),
(6, 8, 3),
(7, 1, 1),
(8, 2, 0);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `fk_book_author` FOREIGN KEY (`fk_id_author`) REFERENCES `author` (`id_author`) ON DELETE RESTRICT ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_book_publisher` FOREIGN KEY (`fk_id_publisher`) REFERENCES `publisher` (`id_publisher`) ON DELETE RESTRICT ON UPDATE CASCADE;

--
-- Contraintes pour la table `book_personage`
--
ALTER TABLE `book_personage`
  ADD CONSTRAINT `fk_bc_book` FOREIGN KEY (`fk_id_book`) REFERENCES `book` (`id_book`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_bc_personage` FOREIGN KEY (`fk_id_personage`) REFERENCES `personage` (`id_personage`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `selection_book`
--
ALTER TABLE `selection_book`
  ADD CONSTRAINT `fk_sb_book` FOREIGN KEY (`fk_id_book`) REFERENCES `book` (`id_book`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_sb_selection` FOREIGN KEY (`fk_id_selection`) REFERENCES `selection` (`id_selection`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `vote`
--
ALTER TABLE `vote`
  ADD CONSTRAINT `fk_vote_book` FOREIGN KEY (`fk_id_book`) REFERENCES `book` (`id_book`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
