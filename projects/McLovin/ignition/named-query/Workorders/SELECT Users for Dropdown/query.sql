SELECT au.id AS "value"
, au.username AS "label"
FROM auth_users au
INNER JOIN auth_user_rl aurl ON au.id = aurl.user_id
WHERE aurl.role_id IN (2, 3, 4, 6)