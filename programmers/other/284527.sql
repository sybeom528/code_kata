-- 조건에 맞는 사원 정보 조회하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/284527
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 16:26:28

WITH CTE1 AS (SELECT EMP_NO, SUM(SCORE) AS TOTAL FROM HR_GRADE
WHERE YEAR = 2022
GROUP BY EMP_NO),
CTE2 AS (
    SELECT EMP_NO, TOTAL AS SCORE
    FROM CTE1
    WHERE TOTAL = (
        SELECT MAX(TOTAL) FROM CTE1
))
SELECT C.SCORE, C.EMP_NO, E.EMP_NAME, E.POSITION, E.EMAIL
FROM CTE2 AS C
JOIN HR_EMPLOYEES AS E
ON C.EMP_NO = E.EMP_NO
