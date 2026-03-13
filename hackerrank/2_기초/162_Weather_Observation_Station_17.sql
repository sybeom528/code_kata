-- Weather Observation Station 17
-- HackerRank 기초 (⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/weather-observation-station-17/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 10:59:36

/*
Enter your query here.
*/
SELECT ROUND(LONG_W,4) FROM STATION
WHERE LAT_N > 38.7780
ORDER BY LAT_N
LIMIT 1