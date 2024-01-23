SELECT t.name AS teacher_name, sub.name AS subject_name
FROM Subjects sub
JOIN Teachers t ON sub.teacher_id = t.teacher_id
WHERE sub.teacher_id = 1;