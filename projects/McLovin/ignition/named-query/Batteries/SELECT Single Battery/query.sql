SELECT
bt.model,
bt.type,
b.power_rating,
b.capacity,
b.date_purchased
FROM batteries b
LEFT JOIN battery_types bt ON b.model = bt.id
WHERE
b.id = :batteryID