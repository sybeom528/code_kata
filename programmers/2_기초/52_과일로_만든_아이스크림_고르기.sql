-- 과일로 만든 아이스크림 고르기
-- 프로그래머스 기초 (⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133025
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 15:26:10

WITH CTE AS (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL
FROM FIRST_HALF
GROUP BY FLAVOR
HAVING SUM(TOTAL_ORDER) >= 3000)
SELECT C.FLAVOR
FROM CTE AS C
JOIN ICECREAM_INFO AS I
ON C.FLAVOR = I.FLAVOR
WHERE I.INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL DESC