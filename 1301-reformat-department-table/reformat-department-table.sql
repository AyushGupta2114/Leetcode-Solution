/* Write your T-SQL query statement below */
Select  id,
SUM(CASE WHEN month='Jan' then (revenue) end) as Jan_Revenue,
SUM(CASE WHEN month='Feb' then (revenue) end) as Feb_Revenue,
SUM(CASE WHEN month='Mar' then (revenue) end) as Mar_Revenue,
SUM(CASE WHEN month='Apr' then (revenue) end) as Apr_Revenue,
SUM(CASE WHEN month='May' then (revenue) end) as May_Revenue,
SUM(CASE WHEN month='Jun' then (revenue) end) as Jun_Revenue,
SUM(CASE WHEN month='Jul' then (revenue) end) as Jul_Revenue,
SUM(CASE WHEN month='Aug' then (revenue) end) as Aug_Revenue,
SUM(CASE WHEN month='Sep' then (revenue) end) as Sep_Revenue,
SUM(CASE WHEN month='Oct' then (revenue) end) as Oct_Revenue,
SUM(CASE WHEN month='Nov' then (revenue) end) as Nov_Revenue,
SUM(CASE WHEN month='Dec' then (revenue) end) as Dec_Revenue
from department
Group by id
order by id