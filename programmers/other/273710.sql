-- ROOT 아이템 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/273710
-- 작성자: 서윤범
-- 작성일: 2026. 08. 07. 15:42:59

SELECT I.ITEM_ID, I.ITEM_NAME
FROM ITEM_INFO AS I
JOIN ITEM_TREE AS T
ON I.ITEM_ID = T.ITEM_ID
WHERE T.PARENT_ITEM_ID IS NULL
ORDER BY ITEM_ID