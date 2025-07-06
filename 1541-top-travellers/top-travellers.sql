/* Write your T-SQL query statement below */
Select name,COALESCE(dt,0) as travelled_distance from (
Select u.id,name,sum(distance) as dt
from Users u
left join Rides r on r.user_id=u.id
group by u.id,name) a
order by dt desc,name