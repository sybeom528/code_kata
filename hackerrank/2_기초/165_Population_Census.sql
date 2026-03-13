-- Population Census
-- HackerRank 기초 (⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/asian-population/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 11:03:49

SELECT SUM(C1.POPULATION) FROM CITY AS C1
JOIN COUNTRY AS C2
ON C1.COUNTRYCODE = C2.CODE
WHERE C2.CONTINENT = 'Asia'