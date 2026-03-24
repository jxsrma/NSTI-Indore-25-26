## 🧩 **Day 2 – Practical Assignment Sheet (Microsoft Excel Practice)**

**Date:** 22nd October 2025
**Timing:** 9:00 AM – 5:00 PM
**Objective:** Strengthen Excel skills through real-world tasks involving formulas, data management, and analysis.

---

### 🕘 **9:00 AM – 10:30 AM: Excel Basics – Data Entry & Formatting**

**Task 1: Student Marksheet Creation**

1. Create a new Excel file named **`Student_Marksheet.xlsx`**.
2. In **Sheet1**, enter the following columns:

   ```
   Roll No | Student Name | English | Maths | Science | Computer | Total | Average | Grade
   ```
3. Add **data for at least 15 students**.
4. Format the sheet:

   * Center align all text.
   * Apply alternate row colors using *Format as Table*.
   * Add borders and adjust column widths.
   * Bold the header row and freeze panes (top row).
5. Create a **heading** “Student Performance Report” merged across the top row with background color.

✅ *Save your file after completion.*

---

### 🕙 **10:30 AM – 11:45 AM: Excel Formulas – SUM, AVERAGE, IF**

**Task 2: Calculate Results Automatically**

1. In the *Total* column, use the `=SUM()` formula to calculate total marks.
2. In the *Average* column, calculate average marks for each student.
3. In the *Grade* column, use the following logic with **IF**:

   ```
   If Average >= 80 → "A"
   If Average >= 60 and <80 → "B"
   If Average >= 40 and <60 → "C"
   Else → "Fail"
   ```
4. Apply conditional formatting:

   * Highlight students with **Grade A** in light green.
   * Highlight **Fail** in red.
5. Auto-calculate class average using `=AVERAGE()` at the bottom.

✅ *Save progress as:* `Student_Marksheet_Formula.xlsx`

---

### 🕛 **11:45 AM – 1:00 PM: Excel Conditional Formatting & Sorting**

**Task 3: Performance Analysis**

1. Sort students by **Total Marks** in descending order.
2. Apply a **Top 3 Rule** to highlight the top 3 performers.
3. Use **Data Bars** to visually represent *Total Marks*.
4. Add a column **“Result Status”** with formula:

   ```
   =IF(Grade="Fail","Repeat","Promoted")
   ```
5. Use **Filter** to display only “Fail” students.

✅ *Save file as:* `Student_Performance_Analysis.xlsx`

---

### 🍽 **1:00 PM – 2:00 PM: Lunch Break**

---

### ES Session or:

### 🕑 **2:00 PM – 3:30 PM: Excel Data Handling – Sorting, Filtering, Validation**

**Task 4: Employee Salary Data**

1. Use the sheet named **`Employee_Data.csv`**.
2. Calculate:

   * **Gross Salary = Basic Pay + HRA + DA**
   * **Net Salary = Gross Salary – Deduction**
3. Apply **Data Validation** to:

   * Restrict “Department” entries to only *HR, IT, Sales, Admin*.
4. Create a **Filter** and display employees of “IT” department only.
5. Use **Sort** to arrange data by “Net Salary” (Highest to Lowest).

✅ *Save file as:* `Employee_Salary_Data.xlsx`

---

### 🕞 **3:30 PM – 5:00 PM: Mini Project – Excel Dashboard (Self Task)**

**Task 5: Create Your Own Excel Mini Project**
**Objective:** Apply everything learned today in one file.

**Instructions:**

1. Use the file named `Sales_Analysis_Project.csv`.
2. It has 1 sheets:

   * **Sheet1 – Sales Data**

     * Columns: Product, Category, Quantity Sold, Unit Price, Region, Month
     * Use formula to add Total:
       `Total = Quantity Sold * Unit Price`

   * add another **Sheet2 – Analysis**

     * Find:
       * Total Sales per Region (use `SUMIF`)
       * Highest Selling Product (`MAX`)
       * Average Quantity Sold (`AVERAGE`)
     * Use **Conditional Formatting** to highlight top-selling products.
3. Create **2 charts** (on Sheet2):

   * Bar Chart for “Sales by Region”
   * Pie Chart for “Product Category Contribution”
4. Format charts with titles and legends.
5. At the bottom, write your name and date.

✅ *Save final project as:* `Sales_Analysis_Project.xlsx`

---

### 📂 **Expected Submission Folder Structure**

<a href="https://edunetfoundationorg-my.sharepoint.com/:f:/g/personal/jsharma_edunetfoundation_org/Ep5hKWMJMGdGuqyGyaJ1xBEBPin4qoAIyZc-EJl0c9LgxA?e=4QAf5R" target="_blank">Day 2 - 22 Oct</a>

```
YourName_Day2_Practicals/
│
├── Student_Marksheet.xlsx
├── Student_Marksheet_Formula.xlsx
├── Student_Performance_Analysis.xlsx
├── Employee_Salary_Data.xlsx
└── Sales_Analysis_Project.xlsx
```
---
