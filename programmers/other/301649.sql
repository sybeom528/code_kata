-- 대장균의 크기에 따라 분류하기 2
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/301649
-- 작성자: 서윤범
-- 작성일: 2026. 08. 08. 15:46:16

WITH CTE AS (SELECT ID, NTILE(4) OVER(ORDER BY SIZE_OF_COLONY DESC) AS RNK
FROM ECOLI_DATA)
SELECT ID,
CASE
    WHEN RNK = 1 THEN 'CRITICAL'
    WHEN RNK = 2 THEN 'HIGH'
    WHEN RNK = 3 THEN 'MEDIUM'
    ELSE 'LOW'
END AS COLONY_NAME
FROM CTE
ORDER BY ID