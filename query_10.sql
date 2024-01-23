SELECT sub.name AS subject_name
FROM Subjects sub
JOIN Grades g ON sub.subject_id = g.subject_id
WHERE g.student_id = 16 AND sub.teacher_id = 2;