-- Weather Observation Station 20
-- HackerRank 중급 (⭐⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/weather-observation-station-20/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 12:55:58

/*
Enter your query here.
*/
WITH CTE AS (SELECT LAT_N, ROW_NUMBER() OVER(ORDER BY LAT_N) AS RNK
FROM STATION)
SELECT ROUND(LAT_N,4) FROM CTE
WHERE RNK = (
    SELECT ROUND((MIN(RNK) + MAX(RNK)) / 2) FROM CTE
)
