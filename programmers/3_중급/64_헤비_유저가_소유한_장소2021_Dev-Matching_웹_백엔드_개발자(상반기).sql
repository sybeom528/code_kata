-- 헤비 유저가 소유한 장소2021 Dev-Matching: 웹 백엔드 개발자(상반기)
-- 프로그래머스 중급 (⭐⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77487
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 18:25:09

# SELECT A.ID, A.NAME, A.HOST_ID
# FROM PLACES AS A
# WHERE A.HOST_ID IN (
#     SELECT B.HOST_ID
#     FROM PLACES AS B
#     GROUP BY B.HOST_ID
#     HAVING COUNT(*) >= 2
# )
# ORDER BY A.ID

# SELECT A.ID, A.NAME, A.HOST_ID
# FROM PLACES AS A
# WHERE EXISTS (
#     SELECT 1
#     FROM PLACES AS B
#     WHERE B.HOST_ID = A.HOST_ID -- 메인 쿼리의 HOST_ID와 서브쿼리의 HOST_ID를 연결
#     GROUP BY B.HOST_ID
#     HAVING COUNT(*) >= 2
# )
# ORDER BY A.ID;







SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(*) >= 2
)
ORDER BY ID





