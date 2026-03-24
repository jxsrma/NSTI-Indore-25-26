## 🧩 **Day 3 – Practical Assignment Sheet (Advanced Excel Practice)**

**Date:** 23rd October 2025
**Timing:** 9:00 AM – 5:00 PM
**Objective:** Develop intermediate-to-advanced Excel skills for data management, analysis, and reporting using lookup functions, validation, and visualization tools.

---

### 🕘 **9:00 AM – 10:30 AM: Excel – VLOOKUP & HLOOKUP**

**Task 1: Student Result Lookup**

1. Create two sheets in a new file named **`Result_Lookup_Practice.xlsx`**.

   * **Sheet1:** “Student_Data”

     ```
     Roll No | Name | English | Maths | Science | Total
     ```

     → Enter 10 student records with marks and total.
   * **Sheet2:** “Result_Summary”

     ```
     Roll No | Name | Total Marks | Grade
     ```
2. Use **VLOOKUP** to fetch student *Name* and *Total Marks* from `Student_Data` into `Result_Summary`.
3. In “Grade” column, Calculate Grade using formula
4. Test for at least 3 roll numbers manually.
5. Apply table borders and color formatting for clarity.

✅ *Save file as:* `Result_Lookup_Practice.xlsx`

---

### 🕙 **10:30 AM – 11:45 AM: Excel – Data Validation & Drop-downs**

**Task 2: Form Creation with Validation**

1. Use the file **`Data_Validation_Form.csv`**.
2. Use **Data Validation** to:

   * Restrict “Department” to: HR, IT, Sales, Admin (Drop down)
   * Restrict “Gender” to: Male, Female, Other (Drop down)
   * Restrict “Basic Salary” to between ₹10,000 and ₹1,00,000 only
3. Add **input message** and **error alert** for invalid entries.
4. Use cell color formatting (alternate row shades).
5. Create a “Summary” section at bottom using formulas:

   * Count of employees in each department using `COUNTIF`
   * Average salary using `AVERAGEIF`

✅ *Save file as:* `Data_Validation_Form.xlsx`

---

### 🕛 **11:45 AM – 1:00 PM: Excel Charts & Graphs**

**Task 3: Visual Data Analysis**

1. Open a new workbook named **`Charts_Practice.xlsx`**.
2. Create a table with data:

   ```
   Month | Sales | Expenses | Profit
   Jan | 50000 | 30000 | 20000
   Feb | 60000 | 35000 | 25000
   Mar | 70000 | 40000 | 30000
   Apr | 55000 | 28000 | 27000
   May | 80000 | 42000 | 38000
   ```
3. Create the following charts:

   * **Column Chart:** Compare Sales, Expenses, and Profit by month.
   * **Line Chart:** Show trend of Sales and Profit.
   * **Pie Chart:** Represent percentage contribution of each month’s profit.
4. Add chart titles, axis labels, and data labels.
5. Format with clean colors, borders, and legends.

✅ *Save file as:* `Charts_Practice.xlsx`

---

### 🍽 **1:00 PM – 2:00 PM: Lunch Break**

---

### 🕑 **2:00 PM – 3:30 PM: Pivot Tables & Pivot Charts**

**Task 4: Sales Data Analysis**

1. Use the file named **`Pivot_Analysis.csv`**.
3. Add Total column using formula: `Total = Quantity * Unit Price`.
4. Insert a **Pivot Table** to summarize:

   * Total Sales by Region
   * Total Sales by Salesperson
   * Total Quantity sold by Product
5. Create **Pivot Charts** for at least two analyses.
6. Create any Suitable Chart.

✅ *Save file as:* `Pivot_Analysis.xlsx`

---

### 🕞 **3:30 PM – 5:00 PM: Mini Project – Business Dashboard**

**Task 5: Excel Dashboard Project**
**Objective:** Combine your Excel learning to create a functional business summary.

**Instructions:**

1. Use the file named **`Business_Dashboard_Project.csv`**.
2. Sheet1: **Raw Data**

   * Columns: Region, Month, Product, Quantity, Sales Amount, Target
   * Calculate **Achievement % = (Sales / Target) * 100**
3. Sheet2: **Dashboard**

   * Insert 2–3 Pivot Tables for:

     * Monthly Sales
     * Region-wise Achievement
     * Product Performance
   * Create 3 charts:

     * Bar Chart for Monthly Sales
     * Donut Chart for Region-wise Achievement %
     * Column Chart for Product Performance
4. Make it visually neat: borders, background color, formatted headings.
5. Mention your name and date at the bottom.

✅ *Save file as:* `Business_Dashboard_Project.xlsx`

---

### 📂 **Expected Submission Folder Structure**

<a href="https://edunetfoundationorg-my.sharepoint.com/:f:/g/personal/jsharma_edunetfoundation_org/Ei3LNixSSClPlTnmnd38bp4BYkMTqBZrAqVopngBjMEEjg?e=QZThg9" target="_blank">Day 3 - 23 Oct</a>

```
YourName_Day3_Practicals/
│
├── Result_Lookup_Practice.xlsx
├── Data_Validation_Form.xlsx
├── Charts_Practice.xlsx
├── Pivot_Analysis.xlsx
└── Business_Dashboard_Project.xlsx
```
---
