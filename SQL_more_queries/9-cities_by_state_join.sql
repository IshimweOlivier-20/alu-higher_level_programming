-- Write a script that lists all cities contained in the database hbtn_0d_usa.
SELECT c.id, c.name, s.name
FROM FROM cities AS C
JOIN states AS S ON S.id = C.state_id
ORDER BY C.id;
