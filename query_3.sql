SELECT gr.group_name, sub.name AS subject_name, AVG(g.grade) AS average_grade
FROM Groups gr
JOIN Students s ON gr.group_id = s.group_id
JOIN Grades g ON s.student_id = g.student_id
JOIN Subjects sub ON g.subject_id = sub.subject_id
WHERE g.subject_id = 3
GROUP BY gr.group_name, sub.name;