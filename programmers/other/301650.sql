-- 특정 세대의 대장균 찾기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/301650
-- 작성자: 서윤범
-- 작성일: 2026. 08. 08. 15:38:08

SELECT ID FROM ECOLI_DATA
WHERE PARENT_ID IN (
    SELECT ID FROM ECOLI_DATA
    WHERE PARENT_ID IN (
        SELECT ID FROM ECOLI_DATA
        WHERE PARENT_ID IS NULL
    )
)
ORDER BY ID


