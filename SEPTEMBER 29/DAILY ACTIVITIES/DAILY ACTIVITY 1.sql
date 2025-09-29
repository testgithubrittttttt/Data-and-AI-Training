CREATE database CompanyDB;
Use CompanyDB;

CREATE table Deapertments(
     dept_id INT auto_increment primary key,
     dept_name VARCHAR(50) NOT NULL
);
CREATE TABLE Employees(
     emp_id INT auto_increment primary key,
     name varchar(50),
     age int,
     salary decimal(10,2),
     dept_id INT,
     foreign key (dept_id) references Deapertments(dept_id)
);

INSERT INTO Deapertments(dept_name) values
('IT'),
('HR'),
('Fnance'),
('Sales');

INSERT INTO Employees (name, age, salary, dept_id) VALUES
('Rahul', 28, 55000, 1),   -- IT
('Priya', 32, 60000, 2),   -- HR
('Arjun', 25, 48000, 3),   -- Finance
('Neha', 30, 70000, 1),    -- IT
('Vikram', 35, 65000, 4);  -- Sales

ALTER TABLE Employees DROP FOREIGN KEY employees_ibfk_1;

TRUNCATE TABLE Employees;
TRUNCATE TABLE Deapertments;

-- #after removing the constrainit then only you can truncate, above the fporeign key is the constraint that why directly we cannot truncate it we have to drop it then truncate it. 

-- --inserting bad data   

INSERT INTO Employees (name, age, salary, dept_id) VALUES
('Rahul', 28, 55000, 1),   -- IT
('Priya', 32, 60000, 2),   -- HR
('Arjun', 25, 48000, NULL),-- 
('Neha', 30, 70000, 1),    -- IT
('Vikram', 35, 65000, 4);  -- Sales

SELECT e.name, e.salary, d.dept_name
from Employees e
INNER JOIN deapertments d
on e.dept_id = d.dept_id;

SELECT e.name, e.salary, d.dept_name
from Employees e
LEFT JOIN deapertments d
on e.dept_id = d.dept_id;

SELECT e.name, e.salary, d.dept_name
from Employees e
right JOIN deapertments d
on e.dept_id = d.dept_id;

SELECT e.name, e.salary, d.dept_name
from Employees e
LEFT JOIN deapertments d
on e.dept_id = d.dept_id
UNION
SELECT e.name, e.salary, d.dept_name
from Employees e
right JOIN deapertments d
on e.dept_id = d.dept_id;


