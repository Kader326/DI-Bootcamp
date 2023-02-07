CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)
--Création de la table FirsTab avec deux champs id et name

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')
--Insertion de 4 éléments dans la table FirsTab

SELECT * FROM FirstTab
--Sélection de tous les éléments de la table FirstTab

CREATE TABLE SecondTab (
    id integer 
)
--Création d'une seconde table nommée SecondTab

INSERT INTO SecondTab VALUES
(5),
(NULL)
--Insertion de deux éléments dans la seconde table

SELECT * FROM SecondTab
--Récupération de tous les éléments de la table
--Réponses aux questions posées suivant le défis

--Q1. quelle sera la sortie de l'instruction suivante?
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
--La sortie sera vide
--Q2. quelle sera la sortie de l'instruction suivante?
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
--La sortie sera 2
--Q3. quelle sera la sortie de l'instruction suivante?
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
--La sortie sera 2
--Q4. quelle sera la sortie de l'instruction suivante?
SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
--La sortie sera 4