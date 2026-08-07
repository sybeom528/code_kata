-- 연간 평가점수에 해당하는 평가 등급 및 성과금 조회하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/284528
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 18:17:09

WITH CTE1 AS (
    SELECT EMP_NO, AVG(SCORE) AS SCORE
    FROM HR_GRADE
    GROUP BY EMP_NO
),
CTE2 AS (
    SELECT EMP_NO, 
    CASE
        WHEN SCORE >= 96 THEN 'S'
        WHEN SCORE >= 90 THEN 'A'
        WHEN SCORE >= 80 THEN 'B'
        ELSE 'C'
    END AS GRADE,
    CASE
        WHEN SCORE >= 96 THEN 0.2
        WHEN SCORE >= 90 THEN 0.15
        WHEN SCORE >= 80 THEN 0.10
        ELSE 0
    END AS RATE
    FROM CTE1
)
SELECT E.EMP_NO, E.EMP_NAME, C.GRADE, E.SAL * C.RATE AS BONUS
FROM HR_EMPLOYEES AS E
JOIN CTE2 AS C
ON E.EMP_NO = C.EMP_NO
ORDER BY E.EMP_NO