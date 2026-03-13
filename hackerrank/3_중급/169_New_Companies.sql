-- New Companies
-- HackerRank 중급 (⭐⭐⭐)
-- 문제 링크: https://www.hackerrank.com/challenges/the-company/problem
-- 작성자: 서윤범
-- 작성일: 2026. 03. 13. 12:49:19

LEFT JOIN MANAGER M ON S.SENIOR_MANAGER_CODE = M.SENIOR_MANAGER_CODE
LEFT JOIN EMPLOYEE E ON M.MANAGER_CODE = E.MANAGER_CODE
GROUP BY C.COMPANY_CODE, C.FOUNDER 
ORDER BY C.COMPANY_CODE;