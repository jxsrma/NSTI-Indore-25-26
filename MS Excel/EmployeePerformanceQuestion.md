### 🧠 Tricky Excel Questions (30 Questions)

#### 🧩 **Formula & Logical Thinking**

1. Calculate each employee’s **Total Annual Salary** including bonus.
   *(Hint: =Salary × 12 + (Salary × Bonus% / 100 × 12))*
2. Use an **IF formula** to show "Eligible for Bonus" if experience ≥ 3 years, else "Not Eligible".
3. Calculate **Average Salary per Department** using `AVERAGEIF`.
4. Find which department has the **highest average salary** (combine MAX + AVERAGEIF).
5. Use `COUNTIFS` to count employees in **IT department** with **experience ≥ 5 years**.
6. Calculate **Total Projects per City** using `SUMIF`.
7. Find the **employee who joined earliest** using `MIN` on Joining Date.
8. Calculate each employee’s **Tenure in years** from Joining Date (use `DATEDIF`).
9. Use an `IF` with `AND` condition to highlight employees with **Salary > 80000** and **Bonus% > 15**.
10. Create a formula to categorize employees as:

    * “Senior” if Experience ≥ 8
    * “Mid-level” if Experience between 4–7
    * “Junior” if Experience < 4

---

#### 💡 **Text & Date Functions**

11. Extract only the **First Name** from the Name column using `LEFT` and `SEARCH`.
12. Extract the **Last Name** using `RIGHT` and `SEARCH`.
13. Display the **Joining Month** using `TEXT(Joining Date,"MMMM")`.
14. Combine Name and Department in one column (e.g., “Arjun Mehta - Sales”).
15. Use `PROPER` to ensure all names are in proper case.
16. Use `UPPER` to make all city names uppercase.
17. Count how many employees joined in **2020 or later** using `YEAR` with `COUNTIFS`.
18. Use `NETWORKDAYS` to calculate working days since joining (assuming today’s date).

---

#### 🎯 **Lookup & Reference**

19. Create a **lookup formula (VLOOKUP/XLOOKUP)** to get an employee’s Designation using their EmpID.
20. Create a **reverse lookup** using `INDEX` and `MATCH` to get Name when Department = “Finance”.
21. Use `HLOOKUP` to display Bonus% for a given employee horizontally.
22. Create a **dynamic formula** to fetch the department of an employee based on dropdown (Data Validation).

---

#### 🧮 **Data Analysis & Conditional Formatting**

23. Apply **conditional formatting** to highlight top 3 salaries in green.
24. Highlight employees who have **experience less than 4 years** in red.
25. Add **Data Validation** to restrict Bonus% entry between 0–20.
26. Identify employees with **Working Hours > 45** using formula-based formatting.
27. Create a formula to count employees who completed **more than 10 projects** and are **not Managers**.
28. Find the **average salary of employees who joined before 2018**.
29. Calculate **Bonus Amount per Month** for each employee.
30. Find how many employees’ **names start with ‘A’** (use `LEFT` + `COUNTIF`).

---