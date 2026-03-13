-- Weather Observation Station 14
-- HackerRank 기초 (⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/weather-observation-station-14/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 10:37:17

/*
Enter your query here.
*/

SELECT ROUND(MAX(LAT_N),4) FROM STATION
WHERE LAT_N < 137.2345