-- 오랜 기간 보호한 동물(2)
-- 프로그래머스 기초 (⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59411
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 14:50:27

SELECT T.ANIMAL_ID, T.NAME
FROM (
    SELECT I.ANIMAL_ID, I.NAME, DATEDIFF(O.DATETIME, I.DATETIME) AS DIFF
    FROM ANIMAL_INS AS I
    JOIN ANIMAL_OUTS AS O
    ON I.ANIMAL_ID = O.ANIMAL_ID
) AS T
ORDER BY DIFF DESC
LIMIT 2