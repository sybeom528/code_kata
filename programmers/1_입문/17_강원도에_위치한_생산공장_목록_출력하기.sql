-- 강원도에 위치한 생산공장 목록 출력하기
-- 프로그래머스 입문 (⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131112
-- 작성자: 서윤범
-- 작성일: 2026. 08. 06. 16:37:24

SELECT FACTORY_ID, FACTORY_NAME, ADDRESS FROM FOOD_FACTORY
WHERE ADDRESS LIKE ('강원%')
ORDER BY FACTORY_ID