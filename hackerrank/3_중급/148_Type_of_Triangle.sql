-- Type of Triangle
-- HackerRank 중급 (⭐⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/what-type-of-triangle/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 11:47:16

/*
Enter your query here.
*/

SELECT CASE
    WHEN (A + B <= C) OR (B + C <= A) OR (C + A <= B) THEN 'Not A Triangle'
    WHEN (A = B) AND (B = C) AND (C = A) THEN 'Equilateral'
    WHEN (A = B AND B = C) OR (B = C AND C = A) OR (C = A OR A = B) THEN 'Isosceles'
    ELSE 'Scalene'
END AS K
