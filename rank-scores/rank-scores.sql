# Write your MySQL query statement below

SELECT s1.Score,
(SELECT COUNT(DISTINCT Score) FROM Scores S2 WHERE S1.Score <= S2.Score) AS 'RANK'
FROM Scores s1
ORDER BY s1.Score DESC