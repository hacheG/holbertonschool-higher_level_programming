-- script that creates the table id_not_null
SELECT id, name
FROM cities 
WHERE state_id = 
    (SELECT id
     FROM states
     WHERE name = "California");