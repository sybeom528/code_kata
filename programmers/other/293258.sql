-- 잔챙이 잡은 수 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/293258
-- 작성자: 서윤범
-- 작성일: 2026. 06. 16. 11:02:07

select count(*) as fish_count from fish_info
where isnull(length)