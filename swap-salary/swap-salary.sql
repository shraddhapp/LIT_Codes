# Write your MySQL query statement bel

Update Salary
set sex = CASE sex
WHEN 'm' THEN 'f'
ELSE 'm'
END;