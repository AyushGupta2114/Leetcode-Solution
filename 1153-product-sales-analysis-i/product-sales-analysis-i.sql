/* Write your T-SQL query statement below */
Select product_name,year,price from Sales as s
left join Product as pd on pd.product_id=s.product_id

