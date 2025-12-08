SELECT CONCAT(et.type, ' ' ,w.equipment_id) AS "Equipment"
, w.description AS "Description"
, w.status AS "Status"
FROM
	workorders w
INNER JOIN equipment_types et ON w.equipment_type = et.id
WHERE 
	w.id = :workorderID