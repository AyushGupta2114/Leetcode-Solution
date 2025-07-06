Select top 1 a.customer_number from (
Select customer_number,count(order_number) as order_count from orders
group by customer_number) a 
order by order_count desc
