-- 1211. Queries Quality and Percentage
-- LeetCode 기초 (⭐⭐)
-- 문제 링크: https://leetcode.com/problems/queries-quality-and-percentage/
-- 작성자: 서윤범
-- 작성일: 2026. 08. 10. 15:14:27

# Write your MySQL query statement below
SELECT 
    QUERY_NAME, 
    ROUND(AVG(RATING / POSITION),2) AS QUALITY, 
FROM QUERIES
    ROUND(AVG(CASE WHEN RATING < 3 THEN 1 ELSE 0 END),4) * 100 AS POOR_QUERY_PERCENTAGE
GROUP BY QUERY_NAME
