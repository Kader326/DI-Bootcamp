-- Dans la base de données dvdrental, écrivez une requête pour sélectionner toutes les colonnes de la table « client ».
SELECT * FROM customer;
-- Écrivez une requête pour afficher les noms ( first_name , last_name ) en utilisant un alias nommé « full_name ».
SELECT (first_name, last_name) as full_name FROM customer;
-- Permet d'obtenir toutes les dates auxquelles les comptes ont été créés. Écrivez une requête pour sélectionner tous les create_date de la table « client » (il ne doit pas y avoir de doublons).
SELECT DISTINCT create_date FROM customer;
-- Écrivez une requête pour obtenir tous les détails du client à partir de la table des clients, elle doit être affichée dans l'ordre décroissant de leur prénom.
SELECT * FROM customer ORDER BY first_name DESC;
-- Rédigez une requête pour obtenir l'ID du film, le titre, la description, l'année de sortie et le tarif de location par ordre croissant en fonction de leur tarif de location.
SELECT film_id,title,description,release_year,rental_rate FROM film ORDER BY rental_rate ASC;
-- Écrivez une requête pour obtenir l'adresse et le numéro de téléphone de tous les clients vivant dans le district du Texas, ces détails peuvent être trouvés dans le tableau "adresse".
SELECT address,phone FROM address WHERE district='Texas';
-- Écrivez une requête pour récupérer tous les détails du film où l'identifiant du film est 15 ou 150.
SELECT * FROM film WHERE film_id IN (15,150) ;
-- Écrivez une requête qui devrait vérifier si votre film préféré existe dans la base de données. Demandez à votre requête d'obtenir l'ID du film, le titre, la description, la durée et le tarif de location, ces détails peuvent être trouvés dans le tableau "film".
SELECT film_id,title,description,film.length,rental_rate FROM film WHERE title='African Egg';
-- Pas de chance de trouver votre film ? Peut-être avez-vous fait une erreur dans l'orthographe du nom. Écrivez une requête pour obtenir l'ID du film, le titre, la description, la durée et le tarif de location de tous les films commençant par les deux premières lettres de votre film préféré.
SELECT film_id,title,description,film.length,rental_rate FROM film WHERE title ILIKE 'Af%';
-- Écrivez une requête qui trouvera les 10 films les moins chers.
SELECT  film_id,title,description,film.length,rental_rate FROM film ORDER BY rental_rate ASC LIMIT 10;
-- Pas satisfait des résultats. Écrivez une requête qui trouvera les 10 prochains films les moins chers.
SELECT  film_id,title,description,film.length,rental_rate FROM film  ORDER BY rental_rate ASC  OFFSET 10 FETCH FIRST 10 ROWS ONLY;
-- Écrivez une requête qui joindra les données de la table des clients et de la table des paiements. Vous souhaitez obtenir le montant et la date de chaque paiement effectué par un client, classé par son identifiant (de 1 à…).
SELECT pa.amount, pa.payment_date FROM payment pa INNER JOIN customer cu ON pa.customer_id=cu.customer_id ORDER BY cu.customer_id ASC;
-- Vous devez vérifier votre inventaire. Écrivez une requête pour obtenir tous les films qui ne sont pas dans l'inventaire.
SELECT f.film_id,f.title,f.description,f.length,f.rental_rate FROM film f WHERE f.film_id NOT IN (SELECT film_id FROM inventory);
-- Rédigez une requête pour trouver quelle ville se trouve dans quel pays.
SELECT co.country, ci.city FROM country co INNER JOIN city ci ON ci.country_id=co.country_id;