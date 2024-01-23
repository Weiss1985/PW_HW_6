SELECT s.name AS student_name, g.grade
FROM Students s
JOIN Grades g ON s.student_id = g.student_id
JOIN Subjects sub ON g.subject_id = sub.subject_id
WHERE s.group_id = 1 AND g.subject_id = 2;