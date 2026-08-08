-- 입양 시각 구하기(2)
-- 프로그래머스 고급 (⭐⭐⭐⭐)
-- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/59413
-- 작성자: 서윤범
-- 작성일: 2026. 08. 08. 15:50:23

with recursive time_table as (
    select 0 as hour
    union all
    select hour + 1 from time_table
    where hour < 23
)
select t.hour, count(animal_id) as count
from time_table as t
left join animal_outs as a
on t.hour = hour(datetime)
group by t.hour
order by t.hour
