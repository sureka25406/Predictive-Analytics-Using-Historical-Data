# Predictive Analytics Using Historical Data

## 📌 Project Overview

This project demonstrates how Machine Learning can be used to analyze historical sales data and predict future sales trends. A Linear Regression model is trained on past sales records to forecast future sales values.

## 🎯 Objectives

* Analyze historical sales data
* Clean and preprocess the dataset
* Train a Linear Regression model
* Evaluate model performance
* Forecast future sales trends
* Visualize results using graphs

## 🛠 Technologies Used

* Python
* Pandas
* Matplotlib
* Scikit-Learn

## 📂 Dataset

The dataset contains the following columns:

| Column | Description          |
| ------ | -------------------- |
| Year   | Year of sales record |
| Sales  | Sales value          |

Sample Data:

| Year | Sales |
| ---- | ----- |
| 2015 | 120   |
| 2016 | 135   |
| 2017 | 150   |

## ⚙️ Project Workflow

### 1. Data Collection

Historical sales data is stored in a CSV file.

### 2. Data Preprocessing

* Load dataset using Pandas
* Check for missing values
* Prepare features and target variables

### 3. Model Training

A Linear Regression model is trained using historical sales data.

### 4. Model Evaluation

The model performance is evaluated using:

* Mean Absolute Error (MAE)
* R² Score

### 5. Future Forecasting

The model predicts future sales for upcoming years.

### 6. Visualization

Sales trends and predictions are visualized using Matplotlib.

## 📈 Results

### Model Performance

* MAE (Mean Absolute Error): 3.75
* R² Score: 0.9979

### Future Sales Predictions

| Year | Predicted Sales |
| ---- | --------------- |
| 2025 | 336.38          |
| 2026 | 360.95          |
| 2027 | 385.52          |
| 2028 | 410.09          |
| 2029 | 434.66          |

## ▶️ How to Run

### Install Required Libraries

```bash
pip install pandas matplotlib scikit-learn
```

### Run the Project

```bash
python predictive_model.py
```

## 📊 Output

The project generates:

* Dataset summary
* Missing value analysis
* Model evaluation metrics
* Future sales predictions
* Sales trend graph

## ✅ Conclusion

This project successfully demonstrates Predictive Analytics using Linear Regression. The model achieved high accuracy and effectively forecasted future sales trends based on historical data.

