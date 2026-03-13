-- Average Population of Each Continent
-- HackerRank 기초 (⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 11:17:37

-- Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.

-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

SELECT C2.CONTINENT, FLOOR(AVG(C1.POPULATION)) FROM CITY AS C1
JOIN COUNTRY AS C2
ON C1.COUNTRYCODE = C2.CODE
GROUP BY C2.CONTINENT