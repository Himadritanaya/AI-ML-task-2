# Task 2: Exploratory Data Analysis (EDA) – AI & ML Internship

## 📌 Objective

The goal of this task is to explore and analyze the Titanic dataset using statistical summaries and visualizations. This helps in identifying patterns, trends, and potential anomalies before building machine learning models.

---

## 📂 Dataset

- **Dataset Name:** Titanic Dataset  
- **Source:** [Kaggle - Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)

---

## ✅ Steps Performed

1. **Data Loading**
   - Loaded the dataset using `pandas` and checked for missing values and data types.

2. **Descriptive Statistics**
   - Used `.describe()` to get mean, median, std dev, etc.
   - Counted null values and observed data types with `.info()`.

3. **Visualizations**
   - **Histograms** for distribution of numerical features like `Age` and `Fare`.
   - **Boxplots** to detect outliers and compare groups (`Age` vs `Survived`).
   - **Correlation Matrix** with heatmap to understand feature relationships.
   - **Pairplot** to see pairwise relationships among multiple features.

4. **Insights**
   - Found data skewness in `Fare`.
   - Observed survival rates by age and gender.
   - Detected multicollinearity using correlation matrix.

---

## 🛠 Tools Used

- Python
- Pandas
- Seaborn
- Matplotlib
- Plotly (optional)

---

## 📈 Outcome

A deeper understanding of the Titanic dataset and its features was achieved. This analysis is critical for effective feature engineering and model selection in future steps.

---

## 📤 Submission

[Click here to submit the task](https://forms.gle/xSbMsLw2UwcVA3mJA)
