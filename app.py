# Gold Price Prediction using machine learning
# ------------------------------------------------
# Install required libraries:
# Pip install pandas numpy sckit - learn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, r2_score
import pyarrow as pa



# ------------------------------------------------
# Load Dataset
# -----------------------------------------------
# Download dataset from kaggle 
# Example file name: heart_disease_data(1).csv
sonar_dataset = pd.read_csv('sonar_data.csv', header=None)


# Display First 5 rows
print("\nHeart Dataset Preview: \n")
print(sonar_dataset.head())

# Separating data and Labels
X = sonar_dataset.drop(columns=60, axis=1)
Y = sonar_dataset[60]

# Split Training and Testing Data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.1, stratify=Y, random_state = 1)


# Train Model
model = LogisticRegression()

# Training the Logistic Regression model with training
model.fit(X_train, Y_train)



# Model Accuracy

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)



print("\nAccuracy on Training Data :", training_data_accuracy)


X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)



print("Accuracy on Test Data", test_data_accuracy)



# Predict Heart Disease from User input:
print("\nEnter Details:")

input_data = (
    0.0307,0.0523,0.0653,0.0521,0.0612,0.0577,0.0660,0.0666,0.0512,0.0394,
    0.0590,0.0649,0.1209,0.2467,0.3564,0.4459,0.4152,0.3952,0.4256,0.4135,
    0.4528,0.5326,0.7306,0.6193,0.2032,0.4636,0.4148,0.4292,0.5730,0.5399,
    0.3161,0.2285,0.6995,1.0000,0.7262,0.4724,0.5103,0.5459,0.2881,0.0981,
    0.1951,0.4181,0.4604,0.3217,0.2828,0.2430,0.1979,0.2444,0.1847,0.0841,
    0.0692,0.0528,0.0357,0.0085,0.0230,0.0046,0.0156,0.0031,0.0054,0.0105
)



# Convert input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
# Prediction
prediction = model.predict(input_data_reshaped)
print(prediction)

print("\nPrediction Result:")

if prediction[0] == 'R':
    print("The Object is a Rock")
else:
    print("The Object is a Mine")