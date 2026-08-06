-- 가격이 제일 비싼 식품의 정보 출력하기
-- 프로그래머스 입문 (⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131115
-- 작성자: 서윤범
-- 작성일: 2026. 08. 06. 16:05:29

SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_CD, CATEGORY, PRICE 
FROM FOOD_PRODUCT
WHERE PRICE = (
    SELECT MAX(PRICE) FROM FOOD_PRODUCT
)