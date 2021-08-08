# Write your MySQL query statement below

SELECT c.Name as Customers 
FROM Customers c
WHERE c.Id NOT IN
(SELECT CustomerId FROM Orders)