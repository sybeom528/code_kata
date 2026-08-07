-- 부서별 평균 연봉 조회하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/284529
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 15:03:04

SELECT D.DEPT_ID, D.DEPT_NAME_EN, E.AVG_SAL
FROM HR_DEPARTMENT AS D
JOIN (
    SELECT DEPT_ID, ROUND(AVG(SAL)) AS AVG_SAL FROM HR_EMPLOYEES
    GROUP BY DEPT_ID
) AS E
ON D.DEPT_ID = E.DEPT_ID
ORDER BY E.AVG_SAL DESC