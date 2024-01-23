SELECT s.student_id, s.name, sub.name AS subject_name, AVG(g.grade) AS average_grade
FROM Students s
JOIN Grades g ON s.student_id = g.student_id
JOIN Subjects sub ON g.subject_id = sub.subject_id
WHERE g.subject_id = 2
GROUP BY s.student_id, s.name, sub.name
ORDER BY average_grade DESC
LIMIT 1;