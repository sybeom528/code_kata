-- 조건에 맞는 도서 리스트 출력하기
-- 프로그래머스 입문 (⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/144853
-- 작성자: 서윤범
-- 작성일: 2026. 08. 06. 17:26:29

SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') FROM BOOK
WHERE YEAR(PUBLISHED_DATE) = 2021
AND CATEGORY = '인문'
ORDER BY PUBLISHED_DATE

# SELECT BOOK_ID, STRFTIME('%Y-%m-%d', PUBLISHED_DATE) AS PUBLISHED_DATE
# FROM BOOK
# WHERE STRFTIME('%Y') = '2021'
# AND CATEGORY = '인문'
# ORDER BY PUBLISHED_DATE