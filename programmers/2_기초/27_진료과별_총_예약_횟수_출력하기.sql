-- 진료과별 총 예약 횟수 출력하기
-- 프로그래머스 기초 (⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132202
-- 작성자: 서윤범
-- 작성일: 2026. 08. 06. 16:52:09

SELECT MCDP_CD AS '진료과코드' , COUNT(*) AS '5월예약건수' FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD, '%Y-%m') = '2022-05'
GROUP BY MCDP_CD
ORDER BY 2,1

# WHERE STRFTIME('%Y-%m-%d',APNT_YMD) = '2022-05'