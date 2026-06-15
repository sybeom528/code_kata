-- 잡은 물고기 중 가장 큰 물고기의 길이 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/298515
-- 작성자: 서윤범
-- 작성일: 2026. 06. 15. 12:06:32

SELECT CONCAT(MAX(LENGTH), 'cm') AS MAX_LENGTH
FROM FISH_INFO