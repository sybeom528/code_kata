-- 물고기 종류 별 잡은 수 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/293257
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 15:29:53

SELECT COUNT(*) AS FISH_COUNT, N.FISH_NAME
FROM FISH_INFO AS I
JOIN FISH_NAME_INFO AS N
ON I.FISH_TYPE = N.FISH_TYPE
GROUP BY I.FISH_TYPE
ORDER BY FISH_COUNT DESC