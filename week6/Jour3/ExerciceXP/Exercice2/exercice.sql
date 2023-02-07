	
-- Utilisons UPDATE pour changer la langue de certains films. Assurez-vous d'utiliser des langues valides.
UPDATE film SET language_id=(SELECT language_id FROM language WHERE name='French') WHERE film_id BETWEEN 1 AND 100;

-- Quelles clés étrangères (références) sont définies pour la table client ? 
-- Les clés étrangères définies pour la table client sont address_id pour la table adress et qtore_id pour la table store
-- Comment cela affecte-t-il la manière dont nous INSÉRONS dans la table client ?
--Nous pouvons insérer des valeurs valides avec ces clés dans la table client

-- Nous avons créé une nouvelle table appelée customer_review . Déposez ce tableau 
DROP TABLE customer_review; 
-- Découvrons combien de locations sont encore en suspens (c'est-à-dire qu'elles n'ont pas encore été retournées au magasin).
SELECT COUNT(r.rental_id) FROM rental r WHERE r.return_date IS NULL;

-- Trouvons les 30 films les plus chers qui sont exceptionnels (c'est-à-dire qui n'ont pas encore été retournés au magasin)
SELECT f.title ,f.rental_rate FROM rental r INNER JOIN inventory i ON i.inventory_id=r.inventory_id INNER JOIN film f ON f.film_id=i.film_id
WHERE r.return_date IS NULL AND f.rental_rate IN(SELECT MAX(rental_rate) FROM film)  LIMIT 30;

-- Mon ami est au magasin et décide de louer un film. Il sait qu'il veut voir 4 films, mais il ne se souvient pas de leurs noms. Pouvez-vous l'aider à trouver les films qu'il souhaite louer ?
-- Le 1er film : Le film parle d'un lutteur de sumo, et l'un des acteurs est Penelope Monroe.
SELECT f.title FROM film f INNER JOIN film_actor fa ON f.film_id=fa.film_id  WHERE description ILIKE '%a lutteur de sumo%' AND 
fa.actor_id=(SELECT actor_id FROM actor WHERE first_name='Penelope' AND last_name='Monroe');

-- Le 2ème film : Un court documentaire (moins d'1h), noté « R ».
SELECT f.title FROM film f INNER JOIN film_category fc ON f.film_id=fc.film_id  WHERE (f.length/60)<1 AND f.rating='R' 
AND fc.category_id=(SELECT category_id FROM category WHERE name ILIKE '%documentary%');

-- Le 3ème film : Un film que son ami Matthew Mahan a loué. Il a payé plus de 4,00 $ pour la location et il l'a rendue entre le 28 juillet et le 1er août 2005.
SELECT f.title FROM film f INNER JOIN inventory i ON f.film_id=i.film_id INNER JOIN rental r ON r.inventory_id=i.inventory_id WHERE f.rental_rate>4 AND r.return_date 
BETWEEN '2005-07-28' AND '2005-08-01' AND r.customer_id=(SELECT customer_id FROM customer WHERE first_name='Matthew' AND last_name='Mahan');

-- Le 4ème film : Son ami Matthew Mahan a également regardé ce film. Il y avait le mot «bateau» dans le titre ou la description, et il semblait que c'était un DVD très coûteux à remplacer.
SELECT f.title FROM film f INNER JOIN inventory i ON f.film_id=i.film_id INNER JOIN rental r ON r.inventory_id=i.inventory_id WHERE ((f.title ILIKE'%boat%') OR (f.description ILIKE'%boat%')) 
 AND r.return_date IS NOT NULL AND f.replacement_cost> (SELECT AVG(replacement_cost) FROM film) AND r.customer_id=(SELECT customer_id FROM customer WHERE first_name='Matthew' AND last_name='Mahan');