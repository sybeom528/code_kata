-- 우유와 요거트가 담긴 장바구니Summer/Winter Coding(2019)
-- 프로그래머스 중급 (⭐⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/62284
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 18:22:18

# SELECT DISTINCT(A.CART_ID) AS CART_ID
# FROM CART_PRODUCTS AS A
# WHERE NAME = 'Milk'
# AND EXISTS (
#     SELECT 1 
#     FROM CART_PRODUCTS AS B
#     WHERE NAME = 'Yogurt'
#     AND A.CART_ID = B.CART_ID
# )
# ORDER BY CART_ID






SELECT DISTINCT(C1.CART_ID) FROM CART_PRODUCTS AS C1
WHERE NAME = 'Milk'
AND EXISTS (
    SELECT 1
    FROM CART_PRODUCTS AS C2
    WHERE NAME = 'Yogurt'
    AND C1.CART_ID = C2.CART_ID
)
ORDER BY C1.CART_ID



