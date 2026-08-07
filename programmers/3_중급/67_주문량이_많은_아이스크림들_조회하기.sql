-- 주문량이 많은 아이스크림들 조회하기
-- 프로그래머스 중급 (⭐⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133027
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 18:00:08

WITH CTE AS (SELECT FLAVOR, TOTAL_ORDER FROM FIRST_HALF
UNION ALL
SELECT FLAVOR, TOTAL_ORDER FROM JULY)
SELECT FLAVOR
FROM CTE
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3