# Filename: CCFraud.py
# Author  : LR Steele
# Info     : Coding project/objective for "Supervised Learning I: Regressors,
#          : Classifiers, and Trees" section of Machine Learning Fundamentals
#          : course in Machine Learning/AI Engineer Career Path on Codecademy.
# Data     : see transactions_README.md for more information
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load and Investigate Data
Transactions_dataset = pd.read_csv("./CCFraud/transactions_modified.csv")
print(Transactions_dataset.head(10))
print(Transactions_dataset.info())

# Some notes about the dataset:
#   The "object" type columns are: type, nameOrig, nameDest
#       These appear to be string type columns
#   There are 3 int64 columns that appear to be binary coded: 
#       isFraud, isPayment, and isMovement

# How many transactions are fraudulent? (According to isFraud)
fraud = Transactions_dataset["isFraud"].value_counts()[1]
print(str(fraud) + " Fraudulent Transactions Reported")

# Calculate summary statistics for amount column
print(Transactions_dataset["amount"].describe())

# What does the distribution look like?
plt.boxplot(Transactions_dataset["amount"].describe())
plt.show()
plt.clf()

# Create a isPayment column, where type="PAYMENT" | "DEBIT" -> 1
# else 0 otherwise
Transactions_dataset["isPayment"] = 0
Transactions_dataset["isPayment"][Transactions_dataset["type"].isin(["PAYMENT", "DEBIT"])] = 1

# Create a isMovement column, where type="CASH_OUT" | "TRANSFER" -> 1
# else 0 otherwise
Transactions_dataset["isMovement"] = 0
Transactions_dataset["isMovement"][Transactions_dataset["type"].isin(["CASH_OUT", "TRANSER"])] = 1

# Codecademy note: "With financial fraud, another key factor to investigate 
# would be the difference in value between the origin and destination account.
# Our theory, in this case, being that destination accounts with a 
# significantly different value could be suspect of fraud."

# Create a accountDiff column, where 
# absolute diff b/t oldbalanceDest - oldbalanceOrg
Transactions_dataset["accountDiff"] = np.abs(Transactions_dataset["oldbalanceDest"] - Transactions_dataset["oldbalanceOrg"])

# Create Features and Labels for Model
features = Transactions_dataset[["amount", "isPayment", "isMovement", "accountDiff"]]
label = Transactions_dataset[["isFraud"]]

# Split data into training and test
features_train, features_test, outcome_train, outcome_test = train_test_split(features, label, test_size=0.3)

# Codecademy note: Because sklearn's Logisitc Regression implementation
# uses Regularization, we need to scale our feature data.

# Create a scaler, fit it on the training set, and transform the test set
std_scaler = StandardScaler()
features_train = std_scaler.fit_transform(features_train)
features_test = std_scaler.transform(features_test)

