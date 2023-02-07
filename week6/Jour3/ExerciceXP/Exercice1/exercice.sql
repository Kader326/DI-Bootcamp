--Obtention de la liste de toutes les langues du film
SELECT lang.name FROM language lang;

-- Obtenons une liste de tous les films joints avec leurs langues - sélectionnez les détails suivants : titre du film, description et nom de la langue. Essayez votre requête avec différentes jointures
-- Obtenons tous les films, même s'ils n'ont pas de langues.
SELECT f.title,f.description,l.name FROM language l RIGHT OUTER JOIN film f ON l.language_id=f.language_id;
-- Obtenez toutes les langues, même s'il n'y a pas de films dans ces langues.
SELECT f.title,f.description,l.name FROM language l LEFT OUTER JOIN film f ON l.language_id=f.language_id;
-- Créons une nouvelle table nommée new_film avec les colonnes suivantes : id, name. 
CREATE TABLE new_film(
	id SERIAL PRIMARY KEY NOT NULL,
	name VARCHAR(60) NOT NULL
);

--Ajout de quelques nouveaux films à la table.CREATE TABLE  new_film 
INSERT INTO new_film(name) VALUES('Vking'),('Black list'),('sherlock');
--Création d'une nouvelle table appelée customer_review en suivant les instructions données par l'exercice
CREATE TABLE  customer_review(
	review_id SERIAL PRIMARY KEY NOT NULL,
	film_id INTEGER NOT NULL,
	language_id INTEGER NOT NULL,
	title VARCHAR(50) NOT NULL,
	score INTEGER NOT NULL CHECK(score>=1 AND score<=10),
	review_text TEXT NOT NULL, 
	last_update DATE NOT NULL,
	FOREIGN KEY(film_id) REFERENCES new_film(id ) ON DELETE CASCADE,
	FOREIGN KEY(language_id) REFERENCES language(language_id)
);
-- Ajout de deux critiques de films en s'assurant de les lier à des objets valides dans les autres tables.
INSERT INTO customer_review(
	film_id,language_id,title,score,review_text,last_update
) 
VALUES(
	(
		SELECT id FROM new_film WHERE name='Vking'
		),
	(
		SELECT language_id FROM language WHERE name='English'
		),
	'Durée',5,'La série ne dure pas assez par épisode ',CURRENT_DATE
	),
		(
			(
				SELECT id FROM new_film WHERE name='Black list'
				),
			(
				SELECT language_id FROM language WHERE name='French'
				),
		'Appréciation',3,"C'est trop dingue cette série là",CURRENT_DATE
		);

--Suppression d' un film qui a une critique de la table new_film 
DELETE FROM new_film WHERE name='Vking';