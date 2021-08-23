# Write your MySQL query statement below
Select FirstName, LastName, City, State 
From Address A RIGHT OUTER JOIN Person P ON
A.PersonId = P.PersonId