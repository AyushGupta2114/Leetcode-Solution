/* Write your T-SQL query statement below */
/* Write your T-SQL query statement below */

Select Department,Employee,Salary from 
(
Select de.name as Department,emp.name as Employee,emp.Salary,dense_rank() over (partition by emp.departmentid order by Salary desc) as Rnk  
from Employee emp
left join department de on de.id=emp.departmentid
) a where a.rnk<=3

