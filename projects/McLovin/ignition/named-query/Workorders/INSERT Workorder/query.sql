INSERT INTO
workorders
(description, equipment_id, equipment_type, status, assigned_by, assigned_to, date_placed, date_completed, date_started)
VALUES
(:description, :equipmentID, :equipmentType, 0, :assignedBy, :assignedTo, current_timestamp, NULL, NULL)