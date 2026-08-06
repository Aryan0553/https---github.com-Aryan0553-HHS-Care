# 🏥 HHS Care Forecasting & Capacity Planning Dashboard

## 📌 Project Overview

The **HHS Care Forecasting & Capacity Planning Dashboard** is a data-driven analytics solution designed to support proactive decision-making for the Unaccompanied Alien Children (UAC) Program. The project leverages historical care, transfer, and discharge data to forecast future care demand, monitor capacity risks, and provide actionable insights for resource planning.

The dashboard transforms raw operational data into meaningful intelligence, enabling stakeholders to anticipate future trends, identify capacity constraints, and improve child welfare planning.

---

## 🎯 Business Problem

The UAC Program operates in a highly dynamic environment where fluctuations in border activity, policy changes, and humanitarian events can significantly impact the number of children entering federal care.

Traditional reporting provides historical insights but lacks the ability to answer critical forward-looking questions:

* How many children will be under HHS care in the coming weeks?
* Will discharge capacity offset incoming transfers?
* When should healthcare staff and shelters scale resources?
* What is the likelihood of future capacity stress?

This project addresses these challenges through predictive analytics and interactive visualization.

---

## 🎯 Project Objectives

### Primary Objectives

* Forecast future Children in HHS Care
* Estimate future imbalance between intake and exits
* Predict discharge demand trends
* Support capacity planning decisions

### Secondary Objectives

* Provide early warning indicators for capacity stress
* Quantify operational risk levels
* Compare historical trends with future forecasts
* Deliver executive-level insights through Power BI

---

## 📊 Dataset Description

The dataset contains daily operational records related to child intake, custody, transfers, care population, and discharges.

| Column                                         | Description                   |
| ---------------------------------------------- | ----------------------------- |
| Date                                           | Reporting Date                |
| Children apprehended and placed in CBP custody | Daily Intake Volume           |
| Children in CBP custody                        | Active CBP Care Load          |
| Children transferred out of CBP custody        | Flow into HHS System          |
| Children in HHS Care                           | Active HHS Care Population    |
| Children discharged from HHS Care              | Successful Sponsor Placements |

---

## 🛠 Data Preprocessing

The following preprocessing steps were performed:

* Date conversion and time-series indexing
* Missing value identification and treatment
* Data type correction
* Duplicate record verification
* Feature scaling and validation
* Time-series preparation

---

## ⚙ Feature Engineering

To improve forecasting performance, several derived features were created:

### Lag Features

* Lag 1 Day
* Lag 7 Days
* Lag 14 Days

### Rolling Statistics

* 7-Day Rolling Mean
* 14-Day Rolling Mean
* Rolling Variance

### Operational Metrics

* Net Pressure = Transfers − Discharges
* Capacity Risk Classification
* Month
* Day of Week

---

## 📈 Exploratory Data Analysis

EDA was conducted to understand historical patterns and operational behavior.

### Analysis Performed

* Population Trend Analysis
* Transfer Trend Analysis
* Discharge Trend Analysis
* Correlation Analysis
* Capacity Risk Distribution
* Forecast Pattern Evaluation

### Visualizations

* Line Charts
* Bar Charts
* Correlation Heatmaps
* Donut Charts
* Forecast Comparison Charts

---

## 🤖 Forecasting Models

The project evaluated multiple forecasting approaches:

### Baseline Models

* Naive Forecast
* Moving Average Forecast

### Statistical Models

* ARIMA
* SARIMA
* Exponential Smoothing

### Machine Learning Models

* Random Forest Regressor
* Gradient Boosting Regressor

---

## 📏 Model Evaluation Metrics

The forecasting models were evaluated using:

| Metric                | Purpose                        |
| --------------------- | ------------------------------ |
| MAE                   | Mean Absolute Error            |
| RMSE                  | Root Mean Squared Error        |
| MAPE                  | Mean Absolute Percentage Error |
| Forecast Accuracy (%) | Overall Prediction Reliability |

---

## 📊 Power BI Dashboard Features

### Executive KPIs

* Children in HHS Care
* Total Transfers
* Total Discharges
* Net Pressure
* High Risk Days

### Analytical Visuals

* HHS Care Population Trend
* Transfers vs Discharges Analysis
* Actual vs Forecast Comparison
* Capacity Risk Distribution
* Capacity Risk Summary Table

### Interactive Filters

* Year Filter
* Month Filter

---

## 🔑 Key Insights

* HHS Care population demonstrates significant temporal fluctuations.
* Transfer and discharge volumes directly influence future care demand.
* Net Pressure serves as an effective indicator of operational stress.
* Capacity Risk monitoring enables proactive intervention.
* Forecasting models provide valuable support for workforce and resource planning.

---

## 🚀 Technologies Used

### Programming & Analytics

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn

### Forecasting

* ARIMA
* Random Forest Regressor
* Gradient Boosting Regressor

### Business Intelligence

* Microsoft Power BI

---

## 📂 Project Deliverables

* Data Cleaning & Preparation
* Exploratory Data Analysis (EDA)
* Forecasting Model Development
* Model Evaluation Report
* Interactive Power BI Dashboard
* Executive Summary & Recommendations

---

## 🏆 Project Outcome

This project successfully transforms historical UAC operational data into predictive intelligence. By combining time-series forecasting, machine learning techniques, and interactive Power BI visualizations, the solution enables stakeholders to anticipate care demand, optimize resource allocation, and improve strategic planning capabilities.

---

## 👨‍💻 Author

**Aryan Nigam**

Data Analytics & Business Intelligence Enthusiast

Power BI | Python | Machine Learning | Forecasting Analytics