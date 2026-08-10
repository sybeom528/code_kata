-- 1148. Article Views I
-- LeetCode 입문 (⭐)
-- 문제 링크: https://leetcode.com/problems/article-views-i/
-- 작성자: 서윤범
-- 작성일: 2026. 08. 10. 15:08:24

# Write your MySQL query statement below
SELECT DISTINCT AUTHOR_ID AS ID FROM VIEWS
WHERE AUTHOR_ID = VIEWER_ID
ORDER BY ID
