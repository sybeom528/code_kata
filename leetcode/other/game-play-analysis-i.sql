-- 511. Game Play Analysis I
-- LeetCode (미등록 문제)
-- 문제 링크: https://leetcode.com/problems/game-play-analysis-i/
-- 작성자: 서윤범
-- 작성일: 2026. 08. 09. 16:34:17

# Write your MySQL query statement below
SELECT player_id, min(event_date) as first_login FROM Activity
group by player_id
