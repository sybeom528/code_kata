-- Weather Observation Station 19
-- HackerRank 중급 (⭐⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/weather-observation-station-19/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 12:17:12

/*
Enter your query here.
*/

SELECT ROUND(SQRT(POWER((MAX(LAT_N) - MIN(LAT_N)),2) + POWER((MAX(LONG_W) - MIN(LONG_W)),2)),4)
FROM STATION