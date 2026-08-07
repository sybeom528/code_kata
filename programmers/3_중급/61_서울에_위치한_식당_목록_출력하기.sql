-- 서울에 위치한 식당 목록 출력하기
-- 프로그래머스 중급 (⭐⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131118
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 17:25:22

SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, ROUND(AVG(R.REVIEW_SCORE),2) AS SCORE
FROM REST_REVIEW AS R
JOIN (
    SELECT * FROM REST_INFO
    WHERE ADDRESS LIKE '서울%'
) AS I
ON R.REST_ID = I.REST_ID
GROUP BY I.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC