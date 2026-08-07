-- 특정 물고기를 잡은 총 수 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/298518
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 16:28:47

SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO AS I
JOIN FISH_NAME_INFO AS N
ON I.FISH_TYPE = N.FISH_TYPE
WHERE N.FISH_NAME = 'BASS' OR N.FISH_NAME = 'SNAPPER'