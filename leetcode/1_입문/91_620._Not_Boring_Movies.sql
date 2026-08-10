-- 620. Not Boring Movies
-- LeetCode 입문 (⭐)
-- 문제 링크: https://leetcode.com/problems/not-boring-movies/
-- 작성자: 서윤범
-- 작성일: 2026. 08. 10. 14:59:30

# Write your MySQL query statement below
SELECT * FROM Cinema
where id % 2 = 1 and not description = 'boring'
order by rating desc
