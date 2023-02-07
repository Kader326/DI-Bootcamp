--La t&ble Client
CREATE TABLE customer (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(70) NOT NULL,
	last_name VARCHAR(70) NOT NULL
);

CREATE TABLE customer_profile (
	id SERIAL PRIMARY KEY,
	isLoggedIn BOOLEAN DEFAULT FALSE,
	customer_id INTEGER NOT NULL,
	FOREIGN KEY(customer_id) REFERENCES customer(id)
);

--Insertion de quelques clients
INSERT INTO customer (
	first_name,last_name
	) 
VALUES('John','Doe'),('Jerome','Lalu'),('Lea','Rive');
--Insertion de quelques profils de quelques clients
INSERT INTO customer_profile (
	isLoggedIn,customer_id
	) 
VALUES(
	TRUE,(
		SELECT id FROM customer WHERE first_name='John')
	),
(
	FALSE,(
		SELECT id FROM customer WHERE first_name='Jerome')
	);

-- Utilisons les types de jointures pertinents pour afficher :

-- Le prénom des clients connectés
SELECT first_name FROM customer  cu INNER JOIN customer_profile cp ON cu.id=cp.customer_id WHERE cp.isLoggedIn=TRUE;

-- Toutes les colonnes first_name et isLoggedIn des clients - même les clients qui n'ont pas de profil.
SELECT first_name ,isLoggedIn FROM customer  cu LEFT OUTER JOIN customer_profile cp ON cu.id=cp.customer_id;

-- Le nombre de clients non connectés
SELECT COUNT(first_name) FROM customer cu INNER JOIN customer_profile cp ON cu.id=cp.customer_id WHERE cp.isLoggedIn=FALSE;

--Deuxième partie
--Création d'un table nommée Book avec un certain nombre de colonne demandé par l'exercice.
CREATE TABLE Book (
	book_id SERIAL PRIMARY KEY,
	title VARCHAR(70) NOT NULL,
	author VARCHAR(40) NOT NULL
);

--Insertion de quelques livres
INSERT INTO Book (
	title,author
	) 
VALUES ('Alice In Wonderland','Lewis Carroll'),('Harry Potter','J.K Rowling'),('To kill a mockingbird','Harper Lee');
--Créez une table nommée Student , avec les colonnes : student_id SERIAL PRIMARY KEY, name NOT NULL UNIQUE, age. Assurez-vous que l'âge n'est jamais supérieur à 15 ans (Recherchez une méthode SQL) ;
CREATE TABLE Student (
	student_id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL UNIQUE,
	age INTEGER NOT NULL CHECK (age<=15)
);
--Insertion des étudiants demandés comme demandé par l'exercice
INSERT INTO Student (
	name,age
	) 
VALUES('John',12),('Lera',11),('Patrick',10),('Bob', 14);
--Créations d'une table nommée Library , avec les colonnes demandées par l'exercice
CREATE TABLE Library (
	book_fk_id INTEGER NOT NULL ,
	student_id INTEGER NOT NULL ,
	borrowed_date DATE,
	PRIMARY KEY(book_fk_id,student_id),
	FOREIGN KEY(book_fk_id) REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
	FOREIGN KEY(student_id) REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);
--Ajoutons 4 enregistrements dans la table de jonction, utilisez des sous-requêtes.
INSERT INTO Library (
	book_fk_id,student_id,borrowed_date
	) 
VALUES(
	(SELECT book_id FROM Book WHERE title='Alice In Wonderland'),
(SELECT student_id FROM Student WHERE name='John'),'2022-02-15'),
((SELECT book_id FROM Book WHERE title='To kill a mockingbird'),
(SELECT student_id FROM Student WHERE name='Bob'),'2021-03-03'),
((SELECT book_id FROM Book WHERE title='Alice In Wonderland'),
(SELECT student_id FROM Student WHERE name='Lera'),'2021-05-23'),
((SELECT book_id FROM Book WHERE title='Harry Potter'),
(SELECT student_id FROM Student WHERE name='Bob'),'2021-08-12');

--Affichage des données
-- Sélectionnons toutes les colonnes de la table de jonction
SELECT * FROM Library;
-- Sélectionnez le nom de l'élève et le titre des livres empruntés
SELECT s.name, b.title FROM Student s INNER JOIN Library l ON s.student_id=l.student_id INNER JOIN Book b ON b.book_id=l.book_fk_id;
-- Sélectionnez l'âge moyen des enfants qui ont emprunté le livre Alice au pays des merveilles
SELECT AVG(s.age) as Average FROM Student s INNER JOIN Library l ON s.student_id=l.student_id INNER JOIN Book b ON b.book_id=l.book_fk_id;
-- Supprimer un étudiant de la table des étudiants 
DELETE FROM Student WHERE name='John';