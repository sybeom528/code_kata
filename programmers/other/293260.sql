-- 월별 잡은 물고기 수 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/293260
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 15:31:44

SELECT COUNT(*) AS FISH_COUNT, MONTH(TIME) AS MONTH
FROM FISH_INFO
GROUP BY MONTH(TIME)
ORDER BY MONTH