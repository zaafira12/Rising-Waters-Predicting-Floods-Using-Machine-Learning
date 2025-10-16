## Rising-Waters-Predicting-Floods-Using-Machine-Learning

# Overview

This project focuses on predicting the likelihood of floods based on environmental and climatic factors such as temperature, humidity, and annual rainfall. Using machine learning algorithms, it analyzes historical data to build a predictive model that can help forecast flood risks effectively.

# Objectives

Explore and visualize flood-related data.

Preprocess and normalize data for model training.

Train multiple machine learning models (e.g., Decision Tree, Random Forest, KNN, XGBoost).

Evaluate model performance using metrics like accuracy, confusion matrix, and classification report.

# Dataset

The project uses a dataset stored in Excel format (flood dataset.xlsx).
Typical features include:

Temp — Temperature

Humidity — Humidity levels

ANNUAL — Annual Rainfall

Flood — Binary target variable indicating flood occurrence

Ensure the dataset is placed in the same directory or update the file path in the notebook.

# Technologies Used

Python 3.x

pandas, numpy — Data manipulation

matplotlib, seaborn — Data visualization

scikit-learn — Model training and evaluation

xgboost — Advanced boosting algorithm

joblib — Model persistence

# Workflow

Data Loading: Import dataset from Excel.

Exploratory Data Analysis (EDA): Distribution plots and boxplots to understand variable patterns.

Preprocessing: Handle missing values, scaling, and encoding.

Model Training: Compare different ML algorithms.

Evaluation: Use metrics like accuracy, precision, recall, and F1-score.

Model Export: Save best-performing model for deployment.

# Visualizations


<img width="1010" height="682" alt="Distribution Of Annual RainFall" src="https://github.com/user-attachments/assets/0ea10118-af0a-439b-8863-fa60adc5b499" />


<img width="1273" height="799" alt="Corelational HeatMap" src="https://github.com/user-attachments/assets/ee6a9867-78db-4ef7-a661-35ad495c062b" />

<img width="585" height="728" alt="Evaluation Metrix" src="https://github.com/user-attachments/assets/b25abb87-0cb0-4b18-8ce9-56619ea919ad" />

# Output
<img width="605" height="103" alt="Output" src="https://github.com/user-attachments/assets/b5551f64-649e-4f37-8058-2a49a99bae18" />
