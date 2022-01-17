/*
Zoo

You manage a zoo. Each animal in the zoo comes from a different country. A new animal has come in, with the following details:
name - "Slim", type - "Giraffe", country_id - 1
Add him to the Animals table.
2) You want to make a complete list of the animals for the zoo’s visitors. Write a query to output a new table with each animal's name, type and country fields, sorted by countries.
Recall INSERT and INNER JOIN keywords.
*/
INSERT into animals VALUES  ('Slim','Giraffe',1);

select Animals.name, Animals.type, Countries .country FROM Animals INNER JOIN Countries ON Animals.country_id = Countries.id ORDER BY Countries.country;
