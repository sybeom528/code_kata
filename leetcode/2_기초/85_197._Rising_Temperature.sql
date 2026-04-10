-- 197. Rising Temperature
-- LeetCode 기초 (⭐⭐)
-- 문제 링크: https://leetcode.com/problems/rising-temperature/
-- 작성자: 서윤범
-- 작성일: 2026. 04. 10. 18:07:11

# Write your MySQL query statement below
WITH CTE AS (SELECT ID, RECORDDATE, TEMPERATURE,
LAG(TEMPERATURE,1) OVER(ORDER BY RECORDDATE) AS TEMP2
FROM WEATHER)
SELECT ID FROM CTE
WHERE TEMPERATURE > TEMP2
