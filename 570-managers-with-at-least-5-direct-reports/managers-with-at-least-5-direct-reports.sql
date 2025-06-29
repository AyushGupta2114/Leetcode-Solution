/* Write your T-SQL query statement below */
Select e1.name from Employee e1
left join Employee e2 on e1.id=e2.managerid
group by e1.name,e1.id
having count(e2.id)>=5

 