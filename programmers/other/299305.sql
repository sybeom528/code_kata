-- 대장균들의 자식의 수 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/299305
-- 작성자: 서윤범
-- 작성일: 2026. 08. 08. 15:03:43

SELECT A.ID, COUNT(B.PARENT_ID) AS CHILD_COUNT
FROM ECOLI_DATA AS A
LEFT JOIN ECOLI_DATA AS B
ON A.ID = B.PARENT_ID
GROUP BY A.ID
ORDER BY ID