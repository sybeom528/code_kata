-- FrontEnd 개발자 찾기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/276035
-- 작성자: 서윤범
-- 작성일: 2026. 08. 08. 16:12:17

SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM DEVELOPERS AS D
JOIN (   
    SELECT CODE
    FROM SKILLCODES
    WHERE CATEGORY = 'Front End'
) AS S
ON D.SKILL_CODE & S.CODE = S.CODE
ORDER BY ID