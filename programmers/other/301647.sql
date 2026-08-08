-- 부모의 형질을 모두 가지는 대장균 찾기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/301647
-- 작성자: 서윤범
-- 작성일: 2026. 08. 08. 16:43:20

SELECT A.ID, A.GENOTYPE, B.GENOTYPE AS PARENT_GENOTYPE 
FROM ECOLI_DATA AS A
JOIN ECOLI_DATA AS B
ON A.PARENT_ID = B.ID
AND A.GENOTYPE & B.GENOTYPE = B.GENOTYPE
ORDER BY ID