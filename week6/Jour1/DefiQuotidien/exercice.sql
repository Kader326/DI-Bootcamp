
SELECT COUNT(*) FROM actors;
-- Essayons d'ajouter un nouvel acteur avec des champs vides. 
INSERT INTO actors (
	first_name, last_name, age, number_oscars
	) 
VALUES
('','','', NULL
);
-- Que pensez-vous que le résultat sera?
-- Nous pensons que y'aura une erreur car nous avons spécifier lors de la création que les valeurs ne doivent pas être nulles.