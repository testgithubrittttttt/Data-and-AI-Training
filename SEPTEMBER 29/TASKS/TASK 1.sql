#assigment
CREATE DATABASE SCHOOLDB;
USE SCHOOLDB;

CREATE TABLE Subjects(
     subject_id INT auto_increment primary key,
     subject_name VARCHAR(50)
);

create TABLE TEACHERS(
     teacher_id int auto_increment primary KEY,
     name VARCHAR(50),
     subject_id int
);

INSERT INTO Subjects (subject_name) VALUES
('Mathematics'),   -- id = 1
('Science'),       -- id = 2
('English'),       -- id = 3
('History'),       -- id = 4
('Geography');     -- id = 5 (no teacher yet)

INSERT INTO Teachers (name, subject_id) VALUES
('Rahul Sir', 1),   -- Mathematics
('Priya Madam', 2), -- Science
('Arjun Sir', NULL),-- No subject assigned
('Neha Madam', 3);  -- English

SELECT T.name, s.subject_name
from Teachers T
INNER JOIN Subjects s
on T.subject_id = s.subject_id;

SELECT T.name, s.subject_name
from Teachers T
LEFT JOIN Subjects s
on T.subject_id = s.subject_id;

SELECT T.name, s.subject_name
from Teachers T
RIGHT JOIN Subjects s
on T.subject_id = s.subject_id;

SELECT T.name, s.subject_name
from Teachers T
LEFT JOIN Subjects s
on T.subject_id = s.subject_id
UNION
SELECT T.name, s.subject_name
from Teachers T
RIGHT JOIN Subjects s
on T.subject_id = s.subject_id;
