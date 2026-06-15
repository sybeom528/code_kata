-- 잡은 물고기의 평균 길이 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/293259
-- 작성자: 서윤범
-- 작성일: 2026. 06. 15. 12:07:47

SELECT ROUND(AVG(COALESCE(LENGTH,10)),2) AS AVERAGE_LENGTH FROM FISH_INFO