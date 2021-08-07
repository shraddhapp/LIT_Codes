select a.name as Employee from employee a, employee b
where a.managerid=b.id
and 
a.salary>b.salary;