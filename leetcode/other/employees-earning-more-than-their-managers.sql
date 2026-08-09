-- 181. Employees Earning More Than Their Managers
-- LeetCode (미등록 문제)
-- 문제 링크: https://leetcode.com/problems/employees-earning-more-than-their-managers/
-- 작성자: 서윤범
-- 작성일: 2026. 08. 09. 16:21:44

# Write your MySQL query statement below
SELECT e.name AS Employee
From Employee as e
JOIN Employee as e2
ON e.managerId = e2.id
AND e.salary > e2.salary
