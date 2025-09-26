CREATE DATABASE SchoolDB;
use SchoolDB; 

CREATE TABLE students(
    id INT auto_increment PRIMARY KEY,
    name varchar(50), -- VARCHAR IS A STRING WITH 50 CHARACTERS
    age INT,
    course varchar(50),
    marks int
);

INSERT INTO students(name,age,course,marks)
Values
("Priya",22,"ML",90),
("Dhruv",21,"Data science",78);

select * from students;

select name,age from students where marks>80;

select name,marks from students;

Update students
SET marks = 92 , course = 'Advanced AI'
where ID = 2;

DELETE from students where id = 3;


# task 
CREATE TABLE Employees(
    id INT auto_increment PRIMARY KEY,
    name varchar(50) NOT NULL, -- VARCHAR IS A STRING WITH 50 CHARACTERS
    age INT,
    department varchar(50),
    salary Decimal(10,2)
);

INSERT INTO Employees(name,age,department,salary)
Values
("Priya",22,"Consulting",90),
("Dhruv",21,"Auditing",78);

select name,salary from Employees;

Update Employees
SET salary = 92000 , department = 'Accounting'
where ID = 1;

DELETE from Employees where id = 3;

select name,salary from Employees;
