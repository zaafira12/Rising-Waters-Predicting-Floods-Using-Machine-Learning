import pandas as pd

# Load the data from the Excel file
data = pd.read_excel('flood dataset.xlsx')

# Preprocess the data
X = data.drop('flood', axis=1)
y = data['flood']

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the preprocessed data for use in the models.py script
import joblib
joblib.dump(X_train, 'X_train.joblib')
joblib.dump(y_train, 'y_train.joblib')
