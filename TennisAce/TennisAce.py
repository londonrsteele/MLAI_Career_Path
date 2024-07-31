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
fig1 = plt.figure(1)
plt.scatter(aces,wins)
plt.xlabel("# Aces")
plt.ylabel("# Wins")
fig1.show()
# Positive correlation

dbl_faults = Tennis_dataset["DoubleFaults"]
fig2 = plt.figure(2)
plt.scatter(dbl_faults, wins)
plt.xlabel("# Double Faults")
plt.ylabel("# Wins")
fig2.show()
# Positive correlation

first_serve = Tennis_dataset["FirstServe"]
fig3 = plt.figure(3)
plt.scatter(first_serve, wins)
plt.xlabel("% of First-Serve Attempts Made")
plt.ylabel("# of Wins")
fig3.show()
# Normal distribution?


# Create Single Feature Linear Regression model 
# Feature chosen: Aces
# Outcome chosen: Wins
# Split: 80% Train 20% Test
features = Tennis_dataset[["Aces"]]
outcomes = Tennis_dataset[["Wins"]]
feature_train, feature_test, outcome_train, outcome_test = train_test_split(features, outcomes, train_size=0.8)
model = LinearRegression()
model.fit(feature_train, outcome_train)
model.score(feature_test, outcome_test)
prediction = model.predict(feature_test)
fig4 = plt.figure(4)
plt.scatter(outcome_test, prediction, alpha=0.4)
fig4.show()

# Another Single Feature Linear Regression model
# Feature chosen: Double Faults
# Outcome chosen: Wins
# Split: 80% Train 20% Test
features = Tennis_dataset[["DoubleFaults"]]
outcomes = Tennis_dataset[["Wins"]]
feature_train, feature_test, outcome_train, outcome_test = train_test_split(features, outcomes, train_size=0.8)
model = LinearRegression()
model.fit(feature_train, outcome_train)
model.score(feature_test, outcome_test)
prediction = model.predict(feature_test)
fig5 = plt.figure(5)
plt.scatter(outcome_test, prediction, alpha=0.4)
fig5.show()

# Create Two Feature Linear Regression model
# Features chosen: Aces, Double Faults
# Outcome chosen: Wins
# Split: 80% Train 20% Test
features = Tennis_dataset[["Aces", "DoubleFaults"]]
outcomes = Tennis_dataset[["Wins"]]
feature_train, feature_test, outcome_train, outcome_test = train_test_split(features, outcomes, train_size=0.8)
model = LinearRegression()
model.fit(feature_train, outcome_train)
model.score(feature_test, outcome_test)
prediciton = model.predict(feature_test)
fig6 = plt.figure(6)
plt.scatter(outcome_test, prediction, alpha=0.4)
fig6.show()

# Below line keeps figure windows "alive" until closed
input()