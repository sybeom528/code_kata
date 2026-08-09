-- 175. Combine Two Tables
-- LeetCode (미등록 문제)
-- 문제 링크: https://leetcode.com/problems/combine-two-tables/
-- 작성자: 서윤범
-- 작성일: 2026. 08. 09. 16:07:44

# Write your MySQL query statement below
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person as p
LEFT JOIN Address as a
on p.personId = a.personId
