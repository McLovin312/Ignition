SELECT p.id AS "panelID",
l.name AS "location"
FROM panels p
LEFT JOIN locations l ON p.location = l.id
WHERE p.location = :location  OR
(-1 = :location)