UPDATE
	workorders
SET
	date_completed = current_timestamp,
	status = 2
WHERE
	id = :workorderID  