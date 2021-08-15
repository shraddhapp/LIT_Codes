# Write your MySQL query statement below
select class
FROM courses
GROUP BY class
Having COUNT(DISTINCT student) >= 5