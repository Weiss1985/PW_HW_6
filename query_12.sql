SELECT s.name AS student_name, g.grade
FROM Students s
JOIN Grades g ON s.student_id = g.student_id
JOIN Groups gr ON s.group_id = gr.group_id
WHERE gr.group_id = [group_id] AND g.subject_id = [subject_id]
AND g.date_received = (
    SELECT MAX(g2.date_received)
    FROM Grades g2
    WHERE g2.subject_id = [subject_id]
);
