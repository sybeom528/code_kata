-- 3월에 태어난 여성 회원 목록 출력하기
-- 프로그래머스 입문 (⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131120
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 14:37:28

SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE TLNO IS NOT NULL AND MONTH(DATE_OF_BIRTH) = 3 AND GENDER = 'W'
ORDER BY MEMBER_ID