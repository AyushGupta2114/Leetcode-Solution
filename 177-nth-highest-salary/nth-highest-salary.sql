CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
DECLARE @Result INT;
        /* Write your T-SQL query statement below. */
        with den as (
            Select Distinct Salary,
            dense_Rank() over (order by salary DESC) As RN
            from employee
        )
        Select @Result=Salary
        from den
        where RN=@N;
    RETURN @Result;
END