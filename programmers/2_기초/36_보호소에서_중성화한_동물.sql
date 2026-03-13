-- 보호소에서 중성화한 동물
-- 프로그래머스 기초 (⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59045
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 18:36:41

SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME FROM ANIMAL_INS AS I
JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE LIKE '%Intact%' 
and (O.SEX_UPON_OUTCOME LIKE '%Spayed%' or O.SEX_UPON_OUTCOME LIKE '%Neutered%')
order by I.ANIMAL_ID

