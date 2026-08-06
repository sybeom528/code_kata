-- 조건에 맞는 사용자와 총 거래금액 조회하기
-- 프로그래머스 중급 (⭐⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/164668
-- 작성자: 서윤범
-- 작성일: 2026. 08. 06. 17:30:33

SELECT U.USER_ID, U.NICKNAME, SUM(B.PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD AS B
JOIN USED_GOODS_USER AS U
ON U.USER_ID = B.WRITER_ID
WHERE STATUS = 'DONE'
GROUP BY U.USER_ID
HAVING SUM(B.PRICE) >= 700000
ORDER BY TOTAL_SALES