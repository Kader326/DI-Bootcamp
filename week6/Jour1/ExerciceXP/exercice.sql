#Ajout de deux tables items et 
CREATE TABLE items (	
		id_items SERIAL PRIMARY KEY,
		elements VARCHAR (50) NOT NULL,
		prix INTEGER NOT NULL
	);

CREATE TABLE customers(
	id SERIAL PRIMARY KEY,
 	first_name VARCHAR (50) NOT NULL,
 	last_name VARCHAR (60) NOT NULL
);
#Ajout des éléments dans la table des éléments
INSERT INTO items(elements,prix)
VALUES
	('Petit bureau',100),
	('Grand bureau',300),
	('Ventilateur',80);
#Ajout de 05 nouveaux clients dans la table clients	
INSERT INTO customers(first_name,last_name)
VALUES
	('Greg','Jones'),
	('Sandra','Jones'),
	('Scott','Scott'),
	('Trevor','Vert'),
	('Mélanie','Johnson');

#Récupération des données de la base de données
#Tous les articles
SELECT * FROM items;
#Tous les articles dont le prix est supérieur à 80 (80 non inclus).
SELECT * FROM items WHERE price >80;
#Tous les articles dont le prix est inférieur à 300. (300 inclus)
SELECT * FROM items WHERE price <=300;
#Tous les clients dont le nom de famille est « Smith » (Quel sera votre résultat ?).
SELECT * FROM customers WHERE last_name='Smith'; #Aucune sortie
#Tous les clients dont le nom de famille est 'Jones'.
SELECT * FROM customers WHERE last_name = 'Jones'
#Tous les clients dont le prénom n'est pas 'Scott'.
SELECT * FROM customers WHERE first_name !='Scott'; 