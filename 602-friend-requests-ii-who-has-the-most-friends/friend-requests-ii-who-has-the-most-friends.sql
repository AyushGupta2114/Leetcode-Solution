-- Combining both requester and accepter roles
SELECT TOP 1 requester_id AS id, COUNT(*) AS num
FROM (
    SELECT requester_id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS requester_id FROM RequestAccepted
) AS combined
GROUP BY requester_id
ORDER BY COUNT(*) DESC;
