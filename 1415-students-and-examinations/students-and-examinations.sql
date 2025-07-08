/* Write your T-SQL query statement below */
-- Select a.* from Students s
-- Left join (
-- Select s.student_id , e.subject_name ,count(subject_name) as attended_exams from
-- Students s
-- left join Examinations e on s.student_id=e.student_id 
-- group by  s.student_id , e.subject_name) a on a.student_id=s.student_id


Select s.student_id ,s.student_name ,b.subject_name ,COALESCE(attended_exams, 0) as attended_exams from Students s
cross join Subjects b
left join ( Select s.student_id , e.subject_name ,count(subject_name) as attended_exams from
Students s
left join Examinations e on s.student_id=e.student_id 
group by  s.student_id , e.subject_name) a on a.student_id=s.student_id and b.subject_name=a.subject_name
order by s.student_id,b.subject_name 