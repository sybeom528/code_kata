-- Binary Tree Nodes
-- HackerRank 중급 (⭐⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/binary-search-tree-1/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 12:27:08

/*
Enter your query here.
*/
SELECT N, CASE
    WHEN P IS NULL THEN 'Root'
    WHEN N IN (SELECT P FROM BST) THEN 'Inner'
    ELSE 'Leaf'
END AS K
FROM BST
ORDER BY N