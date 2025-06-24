with CTE  as (/* Write your T-SQL query statement below */
SELECT *,row_number() over (partition by email order by id) as rn
from Person
) 

Delete from cte where rn>1;


