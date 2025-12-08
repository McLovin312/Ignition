SELECT
b.id AS "batteryID",
l.name AS "location"
FROM
batteries b
INNER JOIN locations l on b.location = l.id