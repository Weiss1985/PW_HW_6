SELECT DISTINCT sub.name AS subject_name
FROM Grades g
JOIN Subjects sub ON g.subject_id = sub.subject_id
WHERE g.student_id = 6;