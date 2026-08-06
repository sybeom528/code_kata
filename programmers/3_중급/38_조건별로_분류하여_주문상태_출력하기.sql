-- 조건별로 분류하여 주문상태 출력하기
-- 프로그래머스 중급 (⭐⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131113
-- 작성자: 서윤범
-- 작성일: 2026. 08. 06. 17:34:44

SELECT ORDER_ID, PRODUCT_ID, OUT_DATE, 
CASE
    WHEN OUT_DATE IS NULL THEN '출고미정'
    WHEN DATE_FORMAT(OUT_DATE, '%Y-%m-%d') <= '2022-05-01' THEN '출고완료'
    ELSE '출고대기'
END AS '출고여부'
FROM FOOD_ORDER
ORDER BY ORDER_ID