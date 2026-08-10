-- 577. Employee Bonus
-- LeetCode 기초 (⭐⭐)
-- 문제 링크: https://leetcode.com/problems/employee-bonus/
-- 작성자: 서윤범
-- 작성일: 2026. 08. 10. 15:02:48

# Write your MySQL query statement below
SELECT E.NAME, B.BONUS
FROM EMPLOYEE AS E
LEFT JOIN BONUS AS B
ON E.EMPID = B.EMPID
WHERE B.BONUS  < 1000 OR B.BONUS IS NULL
