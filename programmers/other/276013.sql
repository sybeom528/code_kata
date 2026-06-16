-- Python 개발자 찾기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/276013
-- 작성자: 서윤범
-- 작성일: 2026. 06. 16. 11:03:45

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE SKILL_1 = 'Python' or SKILL_2 = 'Python' or SKILL_3 = 'Python'
ORDER BY ID