-- Weather Observation Station 13
-- HackerRank 기초 (⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/weather-observation-station-13/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 10:35:42

SELECT ROUND(SUM(LAT_N),4) FROM STATION
WHERE LAT_N BETWEEN 38.788 AND 137.2345