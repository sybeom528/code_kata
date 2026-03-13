-- Weather Observation Station 18
-- HackerRank 중급 (⭐⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/weather-observation-station-18/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 12:13:47

/*
Enter your query here.
*/
SELECT ROUND(MAX(LAT_N) - MIN(LAT_N) + MAX(LONG_W) - MIN(LONG_W),4)
FROM STATION