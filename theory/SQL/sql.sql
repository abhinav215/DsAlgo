-- https://onecompiler.com/mysql/3y9kv4cu2


CREATE TABLE bands(
  id INT NOT NULL AUTO_INCREMENT, -- automatically increase the index
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE albums (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  release_year INT,
  band_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (band_id) REFERENCES bands(id)
);

--for insert one element
INSERT INTO bands (name)
VALUE ('Iron Maiden');


--for insert many element
INSERT INTO bands(name)
VALUE ('Deuce'),('Avenged Sevenfold'),('Ankor');

-- print whole table
-- * means all
SELECT * FROM bands;

--limit the responcse ... sofirst 2 are only printed
SELECT * FROM bands LIMIT 2;

--print only the names (not id)
SELECT name FROM bands;

--print the table but with changed column name
SELECT id AS 'ID', name AS "Band Name"
FROM bands;

-- order the responce
SELECT * FROM bands ORDER BY name;
SELECT * FROM bands ORDER BY name DESC;
-- ASC is default


INSERT INTO albums (name,release_year,band_id)
VALUES ('THE NUMBER OF THE BEAST',1985,1),
('POWER SLAVE',1984,1),
("NIGHTMARE",2018,2),
("NIGHTMARE",2010,3),
("TEST",NULL,3);

SELECT * FROM albums;

--PRINT ALL NAMES ... but observe 2 nightmare will be printed
SELECT name FROM albums;

-- now only one nightmare will be printed
SELECT DISTINCT name FROM albums


--UPDATE THE ALBUS WITH ID 1
UPDATE albums
SET release_year = 1982
WHERE id=1;

SELECT * FROM albums;


--WHERE IS USED TO FILTER THE RESPONSE
SELECT * FROM albums
WHERE release_year>2000;

-- % MEAN ZERO OR MORE(MANY) CHARARCTER CAN BE THERE
SELECT * FROM albums
WHERE name LIKE "%ER%";

-- AND / OR
SELECT * FROM albums
WHERE name LIKE "%ER%" OR band_id=2;


SELECT * FROM albums
WHERE release_year BETWEEN 2000 AND 2019;

SELECT * FROM albums
WHERE release_year is NULL;

DELETE FROM albums WHERE id=5;

SELECT * FROM albums;


--JOIN AND INNER JOIN ARE SAME 
SELECT * FROM bands
JOIN albums ON bands.id = albums.band_id;

SELECT * FROM bands
INNER JOIN albums ON bands.id = albums.band_id;

-- PRINT ALL LEFT TABLE AND THEN ACCORDING TO THEM ... IF FOR SOME RIGHT LEFT DONT EXIST STILL PRINT .... BUT NOT VICE VERSA
SELECT * FROM bands
LEFT JOIN albums ON bands.id = albums.band_id;

SELECT * FROM bands
RIGHT JOIN albums ON bands.id = albums.band_id;



SELECT avg(release_year) FROM albums;
SELECT SUM(release_year) FROM albums;


SELECT band_id, COUNT(band_id) FROM albums
GROUP BY band_id;


SELECT b.name AS band_name, COUNT(a.id) AS num_albums
FROM bands AS b
LEFT JOIN albums AS a ON b.id = a.band_id
GROUP BY b.id;


SELECT b.name AS band_name, COUNT(a.id) AS num_albums
FROM bands AS b
LEFT JOIN albums AS a ON b.id = a.band_id
GROUP BY b.id
HAVING num_albums = 1;


