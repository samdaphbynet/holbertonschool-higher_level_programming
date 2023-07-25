-- Lists all records of the table second_table.
INSERT INTO second_table(id, name, score) VALUES (3, 'Aria', 18), (4, 'Aria', 12);
SELECT score, name FROM second_table ORDER BY score DESC;