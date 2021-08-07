# Write your MySQL query statement below
select p.FirstName, p.LastName, A.City, A.State 
From Person p Left Outer Join Address A
on p.PersonId = A.PersonId