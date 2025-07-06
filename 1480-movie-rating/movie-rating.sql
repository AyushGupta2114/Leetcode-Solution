/* Write your T-SQL query statement below */
Select b.name as results from (
Select *,RANK() OVER (ORDER BY a.c desc ,name) as salary_rank from (
Select u.name,count(mr.movie_id) as c from 
MovieRating mr
left join movies m on m.movie_id=mr.movie_id
left join users u on u.user_id=mr.user_id
group by u.name) a ) b
where salary_rank=1

union all 

Select b.title from (
Select *,RANK() OVER (ORDER BY a.c desc,title) as salary_rank from (
Select m.title,avg(mr.rating*1.0) as c from 
MovieRating mr
left join movies m on m.movie_id=mr.movie_id
left join users u on u.user_id=mr.user_id
where month(mr.created_at)=2 and year(mr.created_at)=2020
group by m.title) a ) b
where salary_rank=1


