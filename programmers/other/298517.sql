-- 가장 큰 물고기 10마리 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/298517
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 17:45:42

SELECT ID, LENGTH
FROM FISH_INFO
ORDER BY LENGTH DESC, ID
LIMIT 10