-- 물고기 종류 별 대어 찾기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/293261
-- 작성자: 서윤범
-- 작성일: 2026. 08. 08. 15:01:20

SELECT C.ID, I.FISH_NAME, C.LENGTH
FROM FISH_NAME_INFO AS I
JOIN (
    SELECT ID, FISH_TYPE, LENGTH
    FROM FISH_INFO
    WHERE (FISH_TYPE, LENGTH) IN (
        SELECT FISH_TYPE, MAX(LENGTH)
        FROM FISH_INFO
        GROUP BY FISH_TYPE
    )
) AS C
ON I.FISH_TYPE = C.FISH_TYPE
ORDER BY ID

