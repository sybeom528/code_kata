-- 카테고리 별 도서 판매량 집계하기
-- 프로그래머스 기초 (⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/144855
-- 작성자: 서윤범
-- 작성일: 2026. 08. 06. 17:23:58

SELECT B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES
FROM BOOK AS B
JOIN BOOK_SALES AS S
ON B.BOOK_ID = S.BOOK_ID
WHERE DATE_FORMAT(S.SALES_DATE, '%Y-%m') = '2022-01'
GROUP BY B.CATEGORY
ORDER BY CATEGORY

# STRFTIME('%Y-%m', S.SALES_DATE) = '2022-01'
