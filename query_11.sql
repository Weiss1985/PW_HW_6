SELECT AVG(g.grade) AS average_grade
FROM Grades g
JOIN Subjects sub ON g.subject_id = sub.subject_id
WHERE sub.teacher_id = 1 AND g.student_id = 1;
