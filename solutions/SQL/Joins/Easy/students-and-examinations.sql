-- LeetCode #1280 - Students and Examinations
-- Pattern: CROSS JOIN + LEFT JOIN + COUNT
-- Difficulty: Easy
-- Date Solved: Feb 2, 2026

-- Approach:
-- - CROSS JOIN Students x Subjects to get all possible (student, subject) pairs
-- - LEFT JOIN Examinations on BOTH student_id AND subject_name to preserve 0 counts
-- - COUNT(e.student_id) instead of COUNT(*) to correctly return 0 for no matches
-- - GROUP BY all non-aggregated columns

SELECT s.student_id, s.student_name, sub.subject_name,
       COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e
ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;
