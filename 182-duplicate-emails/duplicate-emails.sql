/* Write your T-SQL query statement below */
Select email
from Person
group by email
Having count(email)>1

