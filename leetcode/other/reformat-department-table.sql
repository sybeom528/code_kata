-- 1179. Reformat Department Table
-- LeetCode (미등록 문제)
-- 문제 링크: https://leetcode.com/problems/reformat-department-table/
-- 작성자: 서윤범
-- 작성일: 2026. 08. 09. 16:53:20

sum(CASE WHEN month = 'Apr' then revenue ELSE NULL END) as Apr_Revenue,
sum(CASE WHEN month = 'May' then revenue ELSE NULL END) as May_Revenue,
sum(CASE WHEN month = 'Jun' then revenue ELSE NULL END) as Jun_Revenue,
sum(CASE WHEN month = 'Jul' then revenue ELSE NULL END) as Jul_Revenue,
sum(CASE WHEN month = 'Aug' then revenue ELSE NULL END) as Aug_Revenue,
sum(CASE WHEN month = 'Sep' then revenue ELSE NULL END) as Sep_Revenue,
sum(CASE WHEN month = 'Feb' then revenue ELSE NULL END) as Feb_Revenue,
sum(CASE WHEN month = 'Mar' then revenue ELSE NULL END) as Mar_Revenue,
sum(CASE WHEN month = 'Jan' then revenue ELSE NULL END) as Jan_Revenue,
SELECT ID, 
# Write your MySQL query statement below
