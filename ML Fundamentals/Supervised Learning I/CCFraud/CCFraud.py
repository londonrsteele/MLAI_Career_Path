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

# Create a Logistic Regression model with sklearn
LR_model = LogisticRegression()

# Fit the model onto the training data - this finds the best coefficients
# for our features so the model can more accurately predict our outcome (label)
LR_model.fit(features_train, outcome_train)

# Score the trainig data - this will process the training data through the
# trained model and will predict which transactions are fraud. The score
# returned is the % of correct classifications (the accuracy)
print(LR_model.score(features_train, outcome_train))

# Score the test data - the accuracy this time will reflect the success of
# the model!
print(LR_model.score(features_test, outcome_test))

# Our model was 85% accurate!

# Print the model coefficients to see how important each feature column was
# for prediction.
print(LR_model.coef_)

# The feature with the largest absolute magnitude (and thus importance) was
# column 0, "amount", followed by column 1, "isPayment". The least important
# feature was column 2, "isMovement".

# Predict with the model!
# New transaction data:
transaction1 = np.array([123456.78, 0.0, 1.0, 54670.1])
transaction2 = np.array([98765.43, 1.0, 0.0, 8524.75])
transaction3 = np.array([543678.31, 1.0, 0.0, 510025.5])

sample_transactions = np.stack((transaction1, transaction2, transaction3))

# Scale transactions
sample_transactions = std_scaler.transform(sample_transactions)

# Predict fraud on the new transactions
print(LR_model.predict(sample_transactions))

# Show probabilites on new transactions
print(LR_model.predict_proba(sample_transactions))

# None of the transactions were flagged for fraud! With > 65% accuracy!