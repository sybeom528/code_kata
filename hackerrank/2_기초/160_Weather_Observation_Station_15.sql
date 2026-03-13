-- Weather Observation Station 15
-- HackerRank 기초 (⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/weather-observation-station-15/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 10:45:31

/*
Enter your query here.
*/
SELECT ROUND(LONG_W,4) FROM STATION
WHERE LAT_N < 137.2345
ORDER BY LAT_N DESC
LIMIT 1