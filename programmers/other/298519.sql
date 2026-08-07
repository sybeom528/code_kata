-- 특정 조건을 만족하는 물고기별 수와 최대 길이 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/298519
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 17:27:43

SELECT COUNT(*) AS FISH_COUNT, MAX(LENGTH) AS MAX_LENGTH, FISH_TYPE
FROM (
    SELECT ID, FISH_TYPE, COALESCE(LENGTH, 10) AS LENGTH FROM FISH_INFO
) AS S
GROUP BY FISH_TYPE
HAVING AVG(LENGTH) >= 33
ORDER BY FISH_TYPE