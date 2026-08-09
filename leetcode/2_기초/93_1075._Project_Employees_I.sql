-- 1075. Project Employees I
-- LeetCode 기초 (⭐⭐)
-- 문제 링크: https://leetcode.com/problems/project-employees-i/
-- 작성자: 서윤범
-- 작성일: 2026. 08. 09. 16:44:13

# Write your MySQL query statement below
SELECT P.PROJECT_ID, ROUND(AVG(E.EXPERIENCE_YEARS),2) AS AVERAGE_YEARS
FROM PROJECT AS P
JOIN EMPLOYEE AS E
ON P.EMPLOYEE_ID = E.EMPLOYEE_ID
GROUP BY PROJECT_ID

