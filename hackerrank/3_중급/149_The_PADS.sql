-- The PADS
-- HackerRank 중급 (⭐⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/the-pads/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 12:05:18

/*
Enter your query here.
*/
SELECT CONCAT(NAME, '(', LEFT(OCCUPATION,1) ,')') FROM OCCUPATIONS
ORDER BY 1;

SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(OCCUPATION), 's.')
FROM OCCUPATIONS
GROUP BY OCCUPATION
ORDER BY COUNT(*), LOWER(OCCUPATION);