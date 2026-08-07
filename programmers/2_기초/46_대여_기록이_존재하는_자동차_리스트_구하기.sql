-- 대여 기록이 존재하는 자동차 리스트 구하기
-- 프로그래머스 기초 (⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/157341
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 14:41:29

SELECT DISTINCT(A.CAR_ID)
FROM (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE CAR_TYPE = '세단'
) AS A
JOIN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE MONTH(START_DATE) = 10
) AS B
ON A.CAR_ID = B.CAR_ID
ORDER BY CAR_ID DESC
