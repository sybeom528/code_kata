-- 한 해에 잡은 물고기 수 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/298516
-- 작성자: 서윤범
-- 작성일: 2026. 06. 15. 12:05:56

SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE YEAR(TIME) = 2021