# Filename : FindTheFlag.py
# Author   : LR Steele
# Info     : Coding project/objective for "Supervised Learning I: Regressors,
#          : Classifiers, and Trees" section of Machine Learning Fundamentals
#          : course in Machine Learning/AI Engineer Career Path on Codecademy.
# Data     : see flags_README.md for more information
# Note     : any comments in "" is from Codecademy!
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Load and Investigate the Data
link_to_data = "https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data"
cols = ['name','landmass','zone', 'area', 'population', 'language','religion',
        'bars','stripes','colours', 'red','green','blue','gold','white',
        'black','orange','mainhue','circles', 'crosses','saltires','quarters',
        'sunstars','crescent','triangle','icon','animate','text','topleft','botright']
df= pd.read_csv(link_to_data, names = cols)

# "We will build a decision tree classifier to predict what continent a 
# particular flag comes from. Before that, we want to understand the 
# distribution of flags by continent."
# Calcluate the count of flags by landmass value.
# Print number of countries by landmass, or continent
print(df["landmass"].value_counts())

# "Rather than looking at all 6 continents, we will focus on just two,
# Europe and Oceania."
# Create a new dataframe with only flags from Europe and Oceania
df_36 = df[df["landmass"].isin([3,6])]

# "Given the list of predictors in the list var, print the average values
# of each for these two continents. Note which predictors have very different
# averages."
# Variable names to use as predictors
var = [ 'red', 'green', 'blue','gold', 'white', 'black', 'orange', 'mainhue','bars',
       'stripes', 'circles','crosses', 'saltires','quarters','sunstars','triangle','animate']
# Print the average values of the predictors for Europe and Oceania
# print(df_36.groupby("landmass")[var].mean().T)

# "We will build a classifier to distinguish flags for these two continents-
# but first, inspect the variable types for each of the predictors."
df_36 = df[df["landmass"].isin([3,6])]
# Print the variable types for the predictors
print(df_36[var].dtypes)

# Create labels for only Europe and Oceania
labels = df_36["landmass"]

# "Note that all the predictor variables are numeric except for mainhue.
# Transform the dataset of predictor variables to dummy variables and
# save this in a new dataframe called data."
# Create dummy variables for categorical predictors
data = pd.get_dummies(df_36[var])

# "Split the data into a train and test set."
# Split data into a train and test set
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, random_state=1, test_size=0.4)

# "We will explore tuning the decision tree model by testing the performance
# over a range of max_depth values. Fit a decision tree classifier for max_depth values
# from 1-20. Save the accuracy score for each depth in the list acc_depth."
# Fit a decision tree for max_depth values 1-20; save the accuracy score in acc_depth
depths = range(1, 21)
acc_depth = []
for i in depths:
    decision_tree = DecisionTreeClassifier(random_state=10, max_depth=i)
    decision_tree.fit(train_data, train_labels)
    acc_depth.append(decision_tree.score(test_data, test_labels))

# "Plot the accuracy of the decision tree models vs. the max_depth."
# Plot the accuracy vs depth
plt.plot(depths, acc_depth)
plt.xlabel("max_depth")
plt.ylabel("accuracy")
plt.show()

# "Find the largest accuracy of the decision tree models vs. the max_depth."
# Find the largest accuracy and the depth this occurs
max_acc = np.max(acc_depth)
best_depth = depths[np.argmax(acc_depth)]
print("Highest accuracy "+ str(round(max_acc,3)*100) + "% at depth " + str(best_depth))

# "Refit the decision tree model using the max_depth from above; plot the decision tree."
# Refit decision tree model with the highest accuracy and plot the decision tree
decision_tree = DecisionTreeClassifier(random_state=1, max_depth=best_depth)
decision_tree.fit(train_data,train_labels)
tree.plot_tree(decision_tree, feature_names=train_data.columns,
               class_names=["Europe", "Oceania"], filled=True)
plt.show()

# "Like we did with max_depth, we will now tune the tree by using the hyperparameter
# ccp_alpha, which is a pruning parameter. Fit a decision tree classifier for each
# value in ccp. Save the accuracy score in the list acc_pruned."
# Create a new list for the accuracy values of a pruned decision tree.  Loop through
# the values of ccp and append the scores to the list
acc_pruned = []
ccp = np.logspace(-3, 0, num=20)
for i in ccp:
    decision_tree_pruned = DecisionTreeClassifier(random_state = 1, max_depth = best_depth, ccp_alpha=i)
    decision_tree_pruned.fit(train_data, train_labels)
    acc_pruned.append(decision_tree_pruned.score(test_data, test_labels))

# Plot the accuracy of the decision tree models vs. the ccp_alpha"
# Plot the accuracy vs ccp_alpha
plt.plot(ccp, acc_pruned)
plt.xscale('log')
plt.xlabel('ccp_alpha')
plt.ylabel('accuracy')
plt.show()

# "Find the largest accuracy and the ccp_alpha value when this occurs."
# Find the largest accuracy and the ccp value this occurs
max_acc_pruned = np.max(acc_pruned)
best_ccp = ccp[np.argmax(acc_pruned)]

print("Highest accuracy " + str(round(max_acc_pruned,3)*100) + "% at ccp_alpha " + str(round(best_ccp,4)))

# "Fit a decision tree model with the values for max_depth and ccp_alpha found above.
# Plot the final decision tree."
# Fit a decision tree model with the values for max_depth and ccp_alpha found above
final_decision_tree = DecisionTreeClassifier(random_state=1, max_depth=best_depth, ccp_alpha=best_ccp)
final_decision_tree.fit(train_data, train_labels)

# Plot the final decision tree
tree.plot_tree(final_decision_tree, feature_names=train_data.columns,
               class_names=["Europe", "Oceania"], filled=True)
plt.show()