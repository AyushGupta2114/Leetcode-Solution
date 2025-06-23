SELECT 
    pd.Project_id,
    ROUND(SUM(emd.Experience_years) * 1.0 / COUNT(pd.Project_id), 2) AS average_years
FROM Project pd
LEFT JOIN Employee emd ON emd.employee_id = pd.employee_id
GROUP BY pd.Project_id;
