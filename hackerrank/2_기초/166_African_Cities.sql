-- African Cities
-- HackerRank 기초 (⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/african-cities/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 11:10:20

SELECT DISTINCT C1.NAME FROM CITY AS C1
JOIN COUNTRY AS C2
ON C1.COUNTRYCODE = C2.CODE
WHERE C2.CONTINENT = 'Africa'
