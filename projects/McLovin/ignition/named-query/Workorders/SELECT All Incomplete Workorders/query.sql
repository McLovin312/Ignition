SELECT w.id as "workorderID"
FROM
	workorders w
INNER JOIN auth_users au ON w.assigned_to = au.id
WHERE
(w.status = 'Unstarted' OR w.status = 'In Progess')