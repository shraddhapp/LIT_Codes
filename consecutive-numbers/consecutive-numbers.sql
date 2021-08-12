# Write your MySQL query statement below
select distinct Num as ConsecutiveNums from Logs
where (Id+1,Num) in (Select * from Logs) and (ID+2, Num) in (Select * from Logs)