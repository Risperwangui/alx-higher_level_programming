-- this lists all the records with a score of equal or greater than 10

SELECT score, name
FROM second_table
WHERE score >= 10 ORDER BY score DESC;
