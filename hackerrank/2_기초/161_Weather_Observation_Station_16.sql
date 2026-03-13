-- Weather Observation Station 16
-- HackerRank 기초 (⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/weather-observation-station-16/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 10:46:53

/*
Enter your query here.
*/
SELECT ROUND(MIN(LAT_N),4) FROM STATION
WHERE LAT_N > 38.7780