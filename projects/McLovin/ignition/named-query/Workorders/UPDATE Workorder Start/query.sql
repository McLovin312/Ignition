UPDATE
	workorders
SET
	date_started = current_timestamp,
	status = 1
WHERE
	id = :workorderID  