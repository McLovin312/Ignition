SELECT *
FROM auth_roles
  INNER JOIN auth_user_rl ON auth_user_rl.role_id = auth_roles.id
  INNER JOIN auth_users ON auth_users.id = auth_user_rl.user_id
  INNER JOIN auth_user_ci ON auth_user_rl.user_id = auth_user_ci.user_id
  INNER JOIN auth_user_sa ON auth_user_rl.role_id = auth_user_sa.user_id
  INNER JOIN workorders ON workorders.assigned_to = auth_users.id AND
    workorders.assigned_by = auth_users.id
  INNER JOIN auth_user_ex ON auth_user_rl.user_id = auth_user_ex.user_id
  INNER JOIN panels ON workorders.equipment_id = panels.id
  INNER JOIN batteries ON workorders.equipment_id = batteries.id
  INNER JOIN battery_types ON batteries.type = battery_types.id
  INNER JOIN locations ON batteries.location = locations.id AND
    panels.location = locations.id
  INNER JOIN maintenance ON maintenance.workorder_id = workorders.id