-- 특정 형질을 가지는 대장균 찾기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/301646
-- 작성자: 서윤범
-- 작성일: 2026. 08. 08. 18:00:05

SELECT COUNT(*) AS COUNT
FROM ECOLI_DATA
WHERE SUBSTR(LPAD(BIN(GENOTYPE),200,'0'),-2,1) = '0'
AND (SUBSTR(LPAD(BIN(GENOTYPE),200,'0'),-1,1) = '1' OR SUBSTR(LPAD(BIN(GENOTYPE),200,'0'),-3,1) = '1')

# SELECT COUNT(*) AS COUNT
# FROM ECOLI_DATA
# WHERE GENOTYPE & 2 = 0 AND (GENOTYPE & 1 OR GENOTYPE & 4)