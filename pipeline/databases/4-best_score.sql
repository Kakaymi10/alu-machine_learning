-- 4-list_high_scores.sql
SELECT name, score
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
