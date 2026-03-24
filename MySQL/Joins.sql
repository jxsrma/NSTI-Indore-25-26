Create database SoftwareCompany;
use SoftwareCompany;

-- Drop if exists (safe to rerun)
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

-- Departments
CREATE TABLE departments (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(50)
);

INSERT INTO departments (dept_id, dept_name) VALUES
(1, 'HR'),
(2, 'Engineering'),
(3, 'Marketing'),
(4, 'Sales'),
(5, 'Legal'); -- dept with NO employees (to demonstrate LEFT/RIGHT/FULL)

-- Employees
CREATE TABLE employees (
  emp_id INT PRIMARY KEY,
  emp_name VARCHAR(50),
  dept_id INT  -- FK to departments.dept_id (may be NULL)
);

INSERT INTO employees (emp_id, emp_name, dept_id) VALUES
(1, 'Alice', 2),   -- Engineering
(2, 'Bob', 2),     -- Engineering
(3, 'Carol', NULL),-- No department
(4, 'Dave', 3),    -- Marketing
(5, 'Erin', 99);   -- Orphan dept_id (no such department) to show unmatched rows

-- Projects (each project can have a manager which is an employee)
CREATE TABLE projects (
  proj_id INT PRIMARY KEY,
  proj_name VARCHAR(60),
  manager_id INT  -- FK to employees.emp_id (may be NULL or invalid)
);

INSERT INTO projects (proj_id, proj_name, manager_id) VALUES
(1, 'Website Revamp', 1),   -- managed by Alice
(2, 'Ad Campaign', 4),      -- managed by Dave
(3, 'Infrastructure', NULL),-- no manager assigned
(4, 'Secret Project', 99);  -- manager_id points to non-existent employee (orphan)

select * from departments;
select * from employees;
select * from projects;

-- 1) INNER JOIN: employees with their department (only matched rows)

Select e.emp_id,e.emp_name,d.dept_name from Employees as e
inner join departments as d
on e.dept_id = d.dept_id;

-- 2) LEFT JOIN: all employees, department if available

Select e.emp_id,e.emp_name,d.dept_name from Employees as e
left join departments as d
on e.dept_id = d.dept_id;

-- left Join using Right Join
Select e.emp_id,e.emp_name,d.dept_name from departments as d
right join Employees as e
on e.dept_id = d.dept_id;

-- 3) RIGHT JOIN: all departments, employees if available

Select d.dept_id,d.dept_name,e.emp_id,e.emp_name from Employees as e
right join departments as d
on e.dept_id = d.dept_id;

-- Right Join using left Join
Select d.dept_id,d.dept_name,e.emp_id,e.emp_name 
from departments as d
left join Employees as e
on e.dept_id = d.dept_id;

-- 4) FULL OUTER JOIN (MySQL): all employees and all departments, matched where possible

Select * from Employees as e
left join departments as d
on e.dept_id = d.dept_id
union
Select * from Employees as e
right join departments as d
on e.dept_id = d.dept_id;

-- 5) JOIN across three tables: projects with manager and manager's department
select e.emp_name as Name ,d.dept_name as Department,p.proj_name as Project from employees as e
join projects as p on e.emp_id = p.manager_id
join departments as d on e.dept_id = d.dept_id;

-- 6) CROSS JOIN: Cartesian product (use carefully)
select * from projects as p
cross join employees as e;


-- 7) NATURAL JOIN (automatically joins on identically named columns)
select * from departments
natural join employees;




DROP TABLE IF EXISTS categories;

CREATE TABLE categories (
  category_id INT PRIMARY KEY,
  category_name VARCHAR(100),
  parent_id INT NULL  -- references category_id of its parent
);

INSERT INTO categories (category_id, category_name, parent_id) VALUES
(1, 'Electronics', NULL),
(2, 'Mobiles', 1),
(3, 'Laptops', 1),
(4, 'Accessories', 1),
(5, 'Android Phones', 2),
(6, 'iPhones', 2),
(7, 'Gaming Laptops', 3),
(8, 'Ultrabooks', 3),
(9, 'Covers & Cases', 4),
(10, 'Chargers', 4);

-- 8) SELF JOIN: find Parents of categories

select * from categories;
select substring(upper(c1.category_name),1,3) as Name,
c2.category_name as "Sub Category" 
from categories as c1
join categories as c2
on c1.category_id = c2.parent_id;


use sakila;
select first_name,last_name, email,address_id from customer where address_id in (
select address_id from address where district = "California"
);
select address_id from address where district = "Uttar Pradesh";


use employee_management;
select * from employees as e
left join departments as d
on e.dept_id = d.dept_id;


select min_salary from roles where role_name = "Senior Developer";
-- 60000

select * from employees where salary < 60000; -- Hard Code X

select * from employees where 
salary < (select min_salary from roles 
	where role_name = "Senior Developer"); -- Sub Query
    
select * from employees where 
salary < (select min(min_salary) from roles); -- Sub Query