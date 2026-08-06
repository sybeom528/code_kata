-- 상품 별 오프라인 매출 구하기
-- 프로그래머스 기초 (⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131533
-- 작성자: 서윤범
-- 작성일: 2026. 08. 06. 17:18:56

SELECT P.PRODUCT_CODE, P.PRICE * O.TOTAL AS SALES
FROM PRODUCT AS P
JOIN (
    SELECT PRODUCT_ID, SUM(SALES_AMOUNT) AS TOTAL 
    FROM OFFLINE_SALE
    GROUP BY PRODUCT_ID
) AS O
ON P.PRODUCT_ID = O.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE