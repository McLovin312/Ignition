(SELECT id AS "value"
, CONCAT('Equipment # ', id) AS "label"
FROM
batteries
WHERE 1 = :equipmentType)
UNION ALL
(SELECT id AS "value"
, CONCAT('Equipment # ', id) AS "label"
FROM
panels 
WHERE 2 = :equipmentType)