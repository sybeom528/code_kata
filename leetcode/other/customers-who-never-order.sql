-- 183. Customers Who Never Order
-- LeetCode (미등록 문제)
-- 문제 링크: https://leetcode.com/problems/customers-who-never-order/
-- 작성자: 서윤범
-- 작성일: 2026. 08. 09. 16:26:26

# Write your MySQL query statement below
select c.name as Customers from customers as c
left join orders as o
on c.id = o.customerId
where o.id is null
