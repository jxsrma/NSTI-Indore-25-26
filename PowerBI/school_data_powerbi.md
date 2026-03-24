# 🏫 School Dataset (Power BI)

## 🎯 What this dataset is designed for

* Removing nulls
* Filling missing values
* Replacing values
* Changing data types
* Splitting columns
* Conditional columns
* Standardizing text
* Removing errors
* Creating new columns

---

# 🧹 Power BI Transformation & Imputation Tasks 

---

## 1️⃣ Data Type Fixing

**Task:**

* Convert:

  * Age → Whole Number
  * Attendance_Percent → Decimal Number
  * Scores → Whole Number


> “Power BI must understand data types before analysis.”

---

## 2️⃣ Text Standardization

**Task:**

* Convert `Gender` to **Proper Case**
* Replace:

  * male → Male
  * female → Female

---

## 3️⃣ Handling Missing Values (Imputation)

### Numeric Columns

**Task:**

* Replace nulls in:

  * Math_Score
  * Science_Score
  * Attendance_Percent
    with **Average value**



> “We don’t delete students just because data is missing.”

---

### Categorical Columns

**Task:**

* Replace nulls in:

  * Gender
  * Class
    with **"Unknown"**

---

## 4️⃣ Conditional Column (Very Important Demo)

**Create a new column: `Performance_Level`**

Condition:

* If Math_Score ≥ 75 → **Excellent**
* 50–74 → **Average**
* Below 50 → **Needs Improvement**



> “This is business logic, not coding.”

---

## 5️⃣ Replace Values

**Task:**

* Replace:

  * YES → Yes
  * NO → No
  * paid → Paid
  * unpaid → Unpaid

---

## 6️⃣ Remove Errors / Invalid Data

**Task:**

* Identify rows where:

  * Attendance > 100
  * Age is null
* Explain **Remove vs Replace**

---

## 7️⃣ Create Calculated Column

**New Column:** `Total_Score`

```
Math_Score + Science_Score
```

---

## 8️⃣ Binning (Grouping)

**Task:**
Create **Attendance Category**:

* Below 75 → Low
* 75–89 → Medium
* 90+ → High

---

## 9️⃣ Sorting & Filtering

**Task:**

* Sort by Attendance
* Filter students with:

  * Attendance > 80
  * Study_Hours ≥ 3

---

## 🔟 Final Load

**Task:**

* Close & Apply
* Use cleaned data for visuals

> “Data is never clean. Power BI’s real power is in fixing it.”

---