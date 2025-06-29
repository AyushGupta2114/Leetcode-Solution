/* Write your T-SQL query statement below */
Select de.name as department,emp.name as Employee,Salary
from Employee emp
left join (
Select emp.departmentid,max(salary) as salarym  from Employee emp
Group by emp.departmentid) a on a.departmentid=emp.departmentid and emp.Salary=a.salarym
left join department de on de.id=emp.departmentid
where a.salarym is not null
