-- LeetCode #1084 - Sales Analysis III
-- Pattern: Joins + GROUP BY + HAVING
-- Difficulty: Easy
-- Date Solved: Feb 2, 2026

-- Approach:
-- - JOIN Product and Sales on product_id
-- - GROUP BY product_id
-- - Use HAVING with MIN/MAX to ensure ALL sales fall within Q1 2019
-- - This "all records must satisfy" pattern uses MIN >= start AND MAX <= end

SELECT p.product_id, p.product_name
FROM Product p
LEFT JOIN Sales s
ON p.product_id = s.product_id
GROUP BY p.product_id
HAVING MIN(s.sale_date) >= '2019-01-01' AND MAX(s.sale_date) <= '2019-03-31';
