-- 가장 큰 물고기 10마리 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/298517
-- 작성자: 서윤범
-- 작성일: 2026. 06. 15. 12:05:04

# SELECT ID, COALESCE(LENGTH,10) AS LENGTH FROM FISH_INFO
# ORDER BY LENGTH DESC, ID ASC
# LIMIT 10


SELECT ID, COALESCE(LENGTH,10) AS LENGTH FROM FISH_INFO
ORDER BY LENGTH DESC, ID ASC
LIMIT 10







