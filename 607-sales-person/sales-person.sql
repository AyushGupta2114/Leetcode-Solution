/* Write your T-SQL query statement below */
 Select name
 from SalesPerson sp
 where sales_id not in (
 Select sales_id
 from  orders od
 left join Company cm on cm.com_id=od.com_id
 where cm.name='Red')