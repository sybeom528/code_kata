-- 596. Classes More Than 5 Students
-- LeetCode 기초 (⭐⭐)
-- 문제 링크: https://leetcode.com/problems/classes-with-at-least-5-students/
-- 작성자: 서윤범
-- 작성일: 2026. 08. 09. 16:35:22

# Write your MySQL query statement below
SELECT CLASS FROM Courses
GROUP BY CLASS
HAVING COUNT(*) >= 5
