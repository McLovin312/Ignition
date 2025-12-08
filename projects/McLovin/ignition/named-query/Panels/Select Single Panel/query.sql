SELECT pt.model
, stc
, ptc
, open_circuit_voltage
, efficiency
, format(date_purchased, 'MM/dd/yyyy') AS date_purchased
, l.name as location
FROM panels AS p
LEFT JOIN panel_types pt ON p.model = pt.id
LEFT JOIN locations AS l ON l.id = p.location
WHERE p.id = :panelID  