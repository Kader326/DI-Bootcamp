-- Exercie 1 Bootcamp
-- Création d'une base de données appelée Bootcamp
-- Création d'une table appelée étudiants
CREATE TABLE students(
	id_student SERIAL PRIMARY KEY,
	first_name VARCHAR(25) NOT NULL,
	last_name VARCHAR(60) NOT NULL,
	birth_date DATE NOT NULL
	);

-- Insertion des données dans la base de données

INSERT INTO students(
	first_name,last_name,birth_date
	) 
VALUES
	('Marc','Bénichou','02/11/1998'),
	('Yann','Cohen','03/12/2010'),
	('Léa','Bénichou','27/07/1987'),
	('Amélie','Dux','07/04/1996'),
	('David','Grez','14/06/2003'),
	('Omer','Simpson','03/10/1980');

-- Insertion de mon nom, prénom et date de naissance dans la table des étudiants
INSERT INTO students(
	first_name,last_name,birth_date
	) 
VALUES
	('Abdoul Kader','SAWADOGO','05/10/1999');

-- Les différentes sélections demandées par l'exercice
-- Récupérer toutes les données de la table.
SELECT * FROM students 
-- Récupérer tous les prénoms et noms de famille des étudiants .
SELECT first_name,last_name FROM students;

-- Pour les questions suivantes, récupérez uniquement les prénoms et noms de famille des élèves.
-- Récupérer l'étudiant dont l'id est égal à 2.
SELECT first_name,last_name FROM students WHERE id_student = 2;
-- Récupérez l'élève dont le nom est Benichou ET le prénom est Marc.
SELECT first_name,last_name FROM students WHERE last_name='Benichou' AND first_name='Marc';
-- Récupérez les étudiants dont le nom de famille est Benichou OU dont le prénom est Marc.
SELECT first_name,last_name FROM students WHERE last_name='Benichou' OR first_name='Marc';
-- Récupérez les étudiants dont les prénoms contiennent la lettre a .
SELECT first_name,last_name FROM students WHERE  first_name ILIKE '%a%';


-- Récupérez les étudiants dont le prénom commence par la lettre a .
SELECT first_name,last_name FROM students WHERE  first_name ILIKE 'a%';
-- Récupérer les étudiants dont les prénoms se terminent par la lettre a .
SELECT first_name,last_name FROM students WHERE  first_name ILIKE '%a';
-- Récupérer les étudiants dont l'avant-dernière lettre de leur prénom est a (Exemple : Le a h).
SELECT first_name,last_name FROM students WHERE  first_name ILIKE '%a-';
-- Récupérer les étudiants dont les identifiants sont égaux à 1 AND 3 .
SELECT first_name,last_name FROM students WHERE  id_student = 1 AND id_student = 3;
-- Récupérez les étudiants dont la date de naissance est égale ou postérieure au 01/01/2000. (afficher toutes leurs informations).
SELECT * FROM students WHERE  birth_date >= '01/01/2000';