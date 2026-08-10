-- 1327. List the Products Ordered in a Period
-- LeetCode 기초 (⭐⭐)
-- 문제 링크: https://leetcode.com/problems/list-the-products-ordered-in-a-period/
-- 작성자: 서윤범
-- 작성일: 2026. 08. 10. 15:20:08

# Write your MySQL query statement below
SELECT P.PRODUCT_NAME, SUM(O.UNIT) AS UNIT
FROM PRODUCTS AS P
JOIN ORDERS AS O
ON P.PRODUCT_ID = O.PRODUCT_ID
WHERE DATE_FORMAT(O.ORDER_DATE,'%Y-%m') = '2020-02'
GROUP BY P.PRODUCT_ID
HAVING SUM(O.UNIT) >= 100
