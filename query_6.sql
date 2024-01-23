SELECT s.name AS student_name, gr.group_name
FROM Students s
JOIN Groups gr ON s.group_id = gr.group_id
WHERE s.group_id = 1;
