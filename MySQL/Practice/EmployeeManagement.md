
# 📁 `employee_management.sql`
```sql
/* ================================
   DATABASE
================================ */
DROP DATABASE IF EXISTS employee_management;
CREATE DATABASE employee_management;
USE employee_management;

/* ================================
   TABLE 1: DEPARTMENTS
   (One Department → Many Employees)
================================ */
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50)
);

INSERT INTO departments VALUES
(1, 'HR', 'Indore'),
(2, 'Engineering', 'Bangalore'),
(3, 'Sales', 'Mumbai'),
(4, 'Finance', 'Delhi'),
(5, 'IT Support', 'Pune');

/* ================================
   TABLE 2: ROLES
   (One Role → Many Employees)
================================ */
CREATE TABLE roles (
    role_id INT PRIMARY KEY,
    role_name VARCHAR(50),
    min_salary INT
);

INSERT INTO roles VALUES
(1, 'Intern', 15000),
(2, 'Junior Developer', 30000),
(3, 'Senior Developer', 60000),
(4, 'Team Lead', 80000),
(5, 'Manager', 100000),
(6, 'HR Executive', 35000),
(7, 'Sales Executive', 40000),
(8, 'Accountant', 45000),
(9, 'IT Support Engineer', 38000);

/* ================================
   TABLE 3: EMPLOYEES
   - Self Join (manager_id)
   - Many → One (Department, Role)
================================ */
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    gender CHAR(1),
    dept_id INT,
    role_id INT,
    manager_id INT,
    salary INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (role_id) REFERENCES roles(role_id),
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);

/* ================================
   EMPLOYEE DATA (≈45 Employees)
================================ */

-- Top Management
INSERT INTO employees VALUES
(1, 'Amit Sharma', 'M', 2, 5, NULL, 120000),
(2, 'Neha Verma', 'F', 3, 5, NULL, 115000),
(3, 'Rohit Mehta', 'M', 1, 5, NULL, 110000),
(4, 'Pooja Singh', 'F', 4, 5, NULL, 118000);

-- Team Leads
INSERT INTO employees VALUES
(5, 'Ankit Jain', 'M', 2, 4, 1, 85000),
(6, 'Sonal Gupta', 'F', 2, 4, 1, 82000),
(7, 'Karan Patel', 'M', 3, 4, 2, 80000),
(8, 'Meena Iyer', 'F', 1, 4, 3, 78000);

-- Senior Developers
INSERT INTO employees VALUES
(9, 'Rahul Das', 'M', 2, 3, 5, 65000),
(10, 'Sneha Roy', 'F', 2, 3, 5, 62000),
(11, 'Vikas Malhotra', 'M', 2, 3, 6, 64000),
(12, 'Nidhi Kapoor', 'F', 2, 3, 6, 63000);

-- Junior Developers
INSERT INTO employees VALUES
(13, 'Arjun Rana', 'M', 2, 2, 9, 35000),
(14, 'Simran Kaur', 'F', 2, 2, 9, 34000),
(15, 'Mohit Bansal', 'M', 2, 2, 10, 36000),
(16, 'Isha Chawla', 'F', 2, 2, 10, 33000),
(17, 'Ravi Kumar', 'M', 2, 2, 11, 32000),
(18, 'Pallavi Joshi', 'F', 2, 2, 12, 34000);

-- Interns
INSERT INTO employees VALUES
(19, 'Aakash Singh', 'M', 2, 1, 13, 18000),
(20, 'Divya Nair', 'F', 2, 1, 14, 17000),
(21, 'Suresh Yadav', 'M', 2, 1, 15, 16000);

-- HR
INSERT INTO employees VALUES
(22, 'Kavita Mishra', 'F', 1, 6, 8, 38000),
(23, 'Deepak Tiwari', 'M', 1, 6, 8, 36000),
(24, 'Ritu Saxena', 'F', 1, 6, 3, 37000);

-- Sales
INSERT INTO employees VALUES
(25, 'Manoj Kulkarni', 'M', 3, 7, 7, 42000),
(26, 'Shalini Rao', 'F', 3, 7, 7, 41000),
(27, 'Prateek Shah', 'M', 3, 7, 7, 43000),
(28, 'Anu Malhotra', 'F', 3, 7, 2, 40000);

-- Finance
INSERT INTO employees VALUES
(29, 'Sanjay Khanna', 'M', 4, 8, 4, 47000),
(30, 'Nupur Jain', 'F', 4, 8, 4, 46000),
(31, 'Ajay Arora', 'M', 4, 8, 4, 48000);

-- IT Support
INSERT INTO employees VALUES
(32, 'Ramesh Solanki', 'M', 5, 9, 1, 39000),
(33, 'Sunita Pawar', 'F', 5, 9, 1, 38000),
(34, 'Harish Nanda', 'M', 5, 9, 1, 40000);

-- Extra Staff
INSERT INTO employees VALUES
(35, 'Alok Tripathi', 'M', 2, 2, 11, 33000),
(36, 'Kirti Deshmukh', 'F', 2, 2, 12, 34000),
(37, 'Naveen Joshi', 'M', 3, 7, 7, 42000),
(38, 'Tanvi Kulkarni', 'F', 3, 7, 7, 41000),
(39, 'Gaurav Sethi', 'M', 4, 8, 4, 46000),
(40, 'Pankaj Verma', 'M', 5, 9, 1, 39500),
(41, 'Swati Agarwal', 'F', 1, 6, 8, 36000),
(42, 'Yogesh Patil', 'M', 2, 2, 10, 35000),
(43, 'Anjali Pandey', 'F', 2, 2, 9, 34500),
(44, 'Siddharth Roy', 'M', 2, 3, 5, 66000),
(45, 'Bhavya Jain', 'F', 2, 3, 6, 65000);

/* ================================
   TABLE 4: PROJECTS
   (One Project → One Manager)
   (One Manager → Many Projects)
================================ */
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(60),
    dept_id INT,
    manager_id INT,
    budget INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);

INSERT INTO projects VALUES
(1, 'AI Automation System', 2, 1, 500000),
(2, 'HR Digitalization', 1, 3, 200000),
(3, 'Sales CRM Upgrade', 3, 2, 350000),
(4, 'Financial Audit Tool', 4, 4, 300000),
(5, 'IT Infrastructure Upgrade', 5, 1, 250000),
(6, 'Mobile App Development', 2, 5, 450000),
(7, 'Data Analytics Platform', 2, 6, 400000);
```

---

## 🔗 Cardinality You Can Explain

| Relationship           | Cardinality             |
| ---------------------- | ----------------------- |
| Department → Employees | One-to-Many             |
| Role → Employees       | One-to-Many             |
| Employee → Manager     | Self Join (One-to-Many) |
| Manager → Projects     | One-to-Many             |
| Department → Projects  | One-to-Many             |

---

# Questions: 

## 🟢 EASY LEVEL (Basic SELECT, WHERE, ORDER BY, JOIN)

### 1️⃣ List all employees with their salary.

### 2️⃣ Display employee name and gender only.

### 3️⃣ Show all employees working in the **Engineering** department.

### 4️⃣ List employees whose salary is greater than 60,000.

### 5️⃣ Display all distinct departments available in the company.

### 6️⃣ Show all roles available in the organization.

### 7️⃣ List employees ordered by salary (highest to lowest).

### 8️⃣ Display employees whose name starts with **‘A’**.

### 9️⃣ Find employees whose salary is between **30,000 and 50,000**.

### 🔟 Show all female employees.

### 1️⃣1️⃣ List employees who do **not** have a manager.

### 1️⃣2️⃣ Display employees working in **Sales or HR** department.

### 1️⃣3️⃣ Show employee name along with department name.

### 1️⃣4️⃣ Display employee name and role name.

### 1️⃣5️⃣ List all projects and their budgets.

### 1️⃣6️⃣ Show project name along with department name.

### 1️⃣7️⃣ Display all employees working in **IT Support**.

### 1️⃣8️⃣ Find employees with role **Intern**.

### 1️⃣9️⃣ Show employees whose salary is less than the minimum salary of **Senior Developer** role.

### 2️⃣0️⃣ List employees along with their manager name (if any).

---

## 🟡 MEDIUM LEVEL (GROUP BY, HAVING, SUBQUERY, SELF JOIN)

### 2️⃣1️⃣ Count number of employees in each department.

### 2️⃣2️⃣ Find average salary per department.

### 2️⃣3️⃣ Show departments having more than **5 employees**.

### 2️⃣4️⃣ List managers and number of employees reporting to them.

### 2️⃣5️⃣ Display employees who earn more than their manager.

### 2️⃣6️⃣ Find department with highest number of employees.

### 2️⃣7️⃣ Show roles that have more than **3 employees**.

### 2️⃣8️⃣ List employees who are **not assigned to any project**.

### 2️⃣9️⃣ Find total project budget per department.

### 3️⃣0️⃣ Display managers who manage more than **one project**.

### 3️⃣1️⃣ Find employees whose salary is higher than the **average salary of their department**.

### 3️⃣2️⃣ List departments that do **not** have any project.

### 3️⃣3️⃣ Show employees who report to **Amit Sharma**.

### 3️⃣4️⃣ Display projects where the manager belongs to the **same department** as the project.

### 3️⃣5️⃣ Find roles with **average salary greater than 50,000**.

---

## 🔴 HARD LEVEL (Complex Subqueries, Logic, Analysis)

### 3️⃣6️⃣ Find the **second highest salary** in the company.

### 3️⃣7️⃣ Display employees who are the **only employee** in their department.

### 3️⃣8️⃣ Find managers whose **team average salary** is greater than the company average salary.

### 3️⃣9️⃣ List employees who indirectly report to **Amit Sharma** (manager’s manager).

### 4️⃣0️⃣ Find the department whose **total employee salary** is greater than the **total project budget** of that department.

---