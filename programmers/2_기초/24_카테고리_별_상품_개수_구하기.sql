-- 카테고리 별 상품 개수 구하기
-- 프로그래머스 기초 (⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131529
-- 작성자: 서윤범
-- 작성일: 2026. 08. 06. 16:24:47

SELECT LEFT(PRODUCT_CODE,2) AS CATEGORY, COUNT(*) AS PRODUCTS 
FROM PRODUCT
GROUP BY LEFT(PRODUCT_CODE, 2)
ORDER BY 1