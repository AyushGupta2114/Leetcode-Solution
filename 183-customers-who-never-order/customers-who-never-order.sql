/* Write your T-SQL query statement below */
Select Name  as Customers from Customers cs
left join orders  rd on rd.customerid=cs.id
where customerid is null

