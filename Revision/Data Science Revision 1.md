# Used Car Price Prediction - Practical Assignment

Data set: [Used Car Price Prediction Dataset](https://www.kaggle.com/datasets/sharmajicoder/used-car-price-prediction-dataset)

## Part 1: Data Understanding

### Q1. Load the Dataset

* Import the dataset using Pandas.
* Display:

  * Number of rows and columns
  * Column names
  * Data types
  * First 5 records

---

### Q2. Dataset Summary

* Generate descriptive statistics.
* Identify:

  * Numerical columns
  * Categorical columns
  * Target variable

---

## Part 2: Data Cleaning

### Q3. Missing Values Analysis

* Find all columns containing missing values.
* Calculate the percentage of missing values in each column.
* Decide how to handle them.

---

### Q4. Duplicate Records

* Check for duplicate rows.
* Remove duplicates if present.
* Compare dataset shape before and after cleaning.

---

### Q5. Outlier Detection

Using:

* Mileage/KM Driven
* Selling Price
* Vehicle Age

Identify potential outliers using:

* Boxplots

---

### Q6. Feature Engineering

Create new columns:

* Vehicle_Age = Current Year − Manufacturing Year
* Price_Per_KM (if applicable)
* Brand extracted from Car Name

---

# Part 3: Exploratory Data Analysis (EDA)

### Q7. Price Distribution

* Plot histogram of selling price.
* Comment on whether the distribution is normal or skewed.

---

### Q8. Brand Analysis

* Find the Top 10 car brands.
* Calculate average selling price for each brand.

---

### Q9. Fuel Type Analysis

* Compare average selling prices across:

  * Petrol
  * Diesel
  * CNG
  * Electric (if available)

---

### Q10. Transmission Analysis

* Compare average price of:

  * Manual cars
  * Automatic cars

---

### Q11. Ownership Analysis

* Analyze how number of previous owners impacts selling price.

---

### Q12. Vehicle Age Analysis

* Plot Vehicle Age vs Selling Price.
* Explain the trend observed.

---

# Part 4: Visualization

### Q13. Correlation Heatmap

* Create a correlation heatmap for numerical columns.
* Identify top 3 features most correlated with selling price.

---

### Q14. Top Brands Visualization

Create a bar chart showing:

* Top 10 brands
* Average selling price

---

### Q15. Fuel Type Visualization

Create:

* Count Plot
* Average Price Plot

for fuel types.

---

### Q16. Mileage vs Price

Create a scatter plot:

* X-axis = Mileage/KM Driven
* Y-axis = Selling Price

Interpret the relationship.

---

### Q17. Vehicle Age vs Price

Create:

* Scatter Plot
* Regression Plot

and explain the trend.

---

### Q18. Seller Type Analysis

Visualize:

* Individual Sellers
* Dealers
* Trustmark Dealers (if available)

Compare their average selling prices.

---

# Part 5: Machine Learning

### Q19. Feature Selection

Prepare features for ML:

* Remove unnecessary columns
* Encode categorical variables
* Select target variable

---

### Q20. Train-Test Split

Split the dataset:

* 80% Training
* 20% Testing

Explain why train-test split is important.

---

### Q21. Linear Regression Model

Build a Linear Regression model and calculate:

* MAE
* MSE
* RMSE
* R² Score

---

### Q22. Decision Tree Regressor

Train a Decision Tree Regressor and compare performance with Linear Regression.

---

### Q23. Random Forest Regressor

Train a Random Forest Regressor and evaluate using:

* MAE
* RMSE
* R² Score

Compare with previous models.

---

### Q24. Feature Importance

Using Random Forest:

* Extract feature importance
* Display Top 10 important features

---

### Q25. Model Comparison

Create a comparison table:

| Model             | MAE | RMSE | R² Score |
| ----------------- | --- | ---- | -------- |
| Linear Regression |     |      |          |
| Decision Tree     |     |      |          |
| Random Forest     |     |      |          |

Identify the best model.

---

# Mini Project Challenge

### Q26. Car Price Prediction System

Build a final model and predict the selling price for:

| Year | KM Driven | Fuel   | Transmission | Owner        |
| ---- | --------- | ------ | ------------ | ------------ |
| 2020 | 25000     | Petrol | Manual       | First Owner  |
| 2018 | 60000     | Diesel | Automatic    | Second Owner |

Display predicted prices and explain the factors affecting the predictions.

---