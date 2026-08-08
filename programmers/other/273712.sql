-- 업그레이드 할 수 없는 아이템 구하기
-- 프로그래머스 (미등록 문제)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/273712
-- 작성자: 서윤범
-- 작성일: 2026. 08. 08. 14:31:10

SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY FROM ITEM_INFO AS I
LEFT JOIN ITEM_TREE AS T
ON I.ITEM_ID = T.PARENT_ITEM_ID
WHERE T.PARENT_ITEM_ID IS NULL
ORDER BY ITEM_ID DESC