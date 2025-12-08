SELECT et.type AS "EquipmentType"
, w.equipment_id AS "EquipmentID"
, w.description AS "WorkDescription"
, w.date_placed AS "DatePlaced"
, w.date_started AS "DateStarted"
, w.date_completed AS "DateCompleted"
, au.username AS "AssignedTo"
, au2.username AS "AssignedBy"
FROM workorders w
INNER JOIN equipment_types et ON w.equipment_type = et.id
INNER JOIN auth_users au ON w.assigned_to = au.id 
INNER JOIN auth_users au2 ON w.assigned_by = au2.id
WHERE
w.status = :status  
ORDER BY
w.date_placed DESC, w.date_started DESC