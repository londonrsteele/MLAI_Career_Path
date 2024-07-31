# Filename : TennisAce.py
# Author   : LR Steele
# Info     : Coding project/objective for "Supervised Learning I: Regressors,
#          : Classifiers, and Trees" section of Machine Learning Fundamentals
#          : course in Machine Learning/AI Engineer Career Path on Codecademy.
# Data     : see tennis_stats_README.md for more information
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load and Investigate Data
Tennis_dataset = pd.read_csv("./TennisAce/tennis_stats.csv")
print(Tennis_dataset.head(10))
print(Tennis_dataset.info())

# Some notes about the dataset: 
#   The only "object" type column is Name (strings)
#   All other columns are numeric
#   Year is the only datetime related column
#   Ranking is the only ordinal column

# Perform Exploratory Analysis
# Looking at some Offensive Features and their associated Wins
wins = Tennis_dataset["Wins"]

aces = Tennis_dataset["Aces"]
plt.scatter(aces,wins)
plt.title("# Aces vs. # Wins")
plt.xlabel("# Aces")
plt.ylabel("# Wins")
plt.show()
plt.clf()
# Positive correlation

dbl_faults = Tennis_dataset["DoubleFaults"]
plt.scatter(dbl_faults, wins)
plt.title("# Double Faults vs. # Wins")
plt.xlabel("# Double Faults")
plt.ylabel("# Wins")
plt.show()
plt.clf()
# Positive correlation

first_serve = Tennis_dataset["FirstServe"]
plt.scatter(first_serve, wins)
plt.title("% First-Serve Attempts Made vs. # Wins")
plt.xlabel("% of First-Serve Attempts Made")
plt.ylabel("# of Wins")
plt.show()
plt.clf()
# Normal distribution?


# Create Single Feature Linear Regression model 
# Feature chosen: Aces
# Outcome chosen: Wins
# Split: 80% Train 20% Test
features = Tennis_dataset[["Aces"]]
outcomes = Tennis_dataset[["Wins"]]
# Split the data into training and test sets
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcomes, train_size=0.8)
# Instantiate the model
model = LinearRegression()
# Train the model using training sets
model.fit(features_train, outcome_train)
# Make outcome predictions based on the test input
outcome_predictions = model.predict(features_test)
# Find the R^2 score of the test data
model.score(features_test, outcome_test)
# Plot the test data scatter plot
plt.scatter(outcome_test, outcome_predictions, alpha=0.4)
plt.title("Predicted Wins vs. Actual Wins - 1 Feature (Aces)")
plt.show()
plt.clf()

# Another Single Feature Linear Regression model
# Feature chosen: Double Faults
# Outcome chosen: Wins
# Split: 80% Train 20% Test
features = Tennis_dataset[["DoubleFaults"]]
outcomes = Tennis_dataset[["Wins"]]
# Split the data into training and test sets
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcomes, train_size=0.8)
# Instantiate the model
model = LinearRegression()
# Train the model using training sets
model.fit(features_train, outcome_train)
# Make outcome predictions based on the test input
outcome_predictions = model.predict(features_test)
# Find the R^2 score of the test data
model.score(features_test, outcome_test)
# Plot the test data scatter plot
plt.scatter(outcome_test, outcome_predictions, alpha=0.4)
plt.title("Predicted Wins vs. Actual Wins - 1 Feature (Double Faults)")
plt.show()
plt.clf()

# Create Two Feature Linear Regression model
# Features chosen: Aces, Double Faults
# Outcome chosen: Wins
# Split: 80% Train 20% Test
features = Tennis_dataset[["Aces", "DoubleFaults"]]
outcomes = Tennis_dataset[["Wins"]]
# Split the data into training and test sets
features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcomes, train_size=0.8)
# Instantiate the model
model = LinearRegression()
# Train the model using training sets
model.fit(features_train, outcome_train)
# Make outcome predictions based on the test input
outcome_predictions = model.predict(features_test)
# Find the R^2 score of the test data
model.score(features_test, outcome_test)
# Plot the test data scatter plot
plt.scatter(outcome_test, outcome_predictions, alpha=0.4)
plt.title("Predicted Wins vs. Actual Wins - 2 Features (Aces and Double Faults)")
plt.show()
plt.clf()

# Below line keeps figure windows "alive" until closed
#input()