# Filename : WrapperMethods.py
# Author   : LR Steele
# Info     : Coding project/objective for "Feature Engineering II: Feature
#          : Selection Methods" section of Machine Learning Fundamentals
#          : course in Machine Learning/AI Engineer Career Path on Codecademy.
# Data     : see obesity_README.md for more information
####################################################################################
# NOTE: MLXTEND DOES NOT SUPPORT NUMPY 2.0.0. MUST DOWNGRADE TO 1.26.4 OR LOWER.
####################################################################################
import pandas as pd
from sklearn.linear_model import LogisticRegression
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.plotting import plot_sequential_feature_selection as plot_sfs
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFE

# Load and Investigate the data
Obesity_dataset = pd.read_csv("./MLAI_Career_Path/Feature Engineering II/WrapperMethods/obesity.csv")
# print(Obesity_dataset.head(10))
# print(Obesity_dataset.info())

# Note from obesity_README.md: Categorical variables were changed to numerical
# ones in order to facilitate analysis. 
# Most columns are int64
# These columns are float64:
#   Age, FCVC, NCP, CH20, FAF, TUE

# Split the data into predictor variables (features) and the outcome variable
X = Obesity_dataset.drop(["NObeyesdad"], axis=1) # pd DataFrame
y = Obesity_dataset["NObeyesdad"] # pd Series

# Create a Logistic Regression model
# Fr Codecademy: "Include the parameter max_iter=1000 to make sure that the
# model will converge when you try to fit it."
lr = LogisticRegression(max_iter=1000)

# Fit the model to X and y
lr.fit(X, y)

# Fr Codecademy: "A model’s accuracy is the proportion of classes that the
# model correctly predicts. Compute and print the accuracy of lr by using 
# the .score() method. What percentage of respondents did the model 
# correctly predict as being either obese or not obese?"
accuracy = lr.score(X,y)
print("Accuracy = " + str(round(accuracy*100,2)) + "%")

##########################################
# Sequential Forward Selection
##########################################
# Create a SFS model
sfs = SFS(
    estimator=lr, 
    forward=True,
    floating=False,
    k_features=9,
    scoring="accuracy",
    cv=0
)

# Fit the model to X and y
sfs.fit(X, y)

# Print the features that were chosen and check the model accuracy
# print(sfs.subsets_[9]) 
sfs_accuracy = round(sfs.subsets_[9]["avg_score"]*100,2)
sfs_features = sfs.subsets_[9]["feature_names"]
print("SFS Accuracy = " + str(sfs_accuracy) + "%")
print("SFS Features = " + str(sfs_features))

# Plot the model accuracy as a function of the number of features used
plot_sfs(sfs.get_metric_dict())
plt.show()

##########################################
# Sequential Backward Selection
##########################################
# Create a SBS model
sbs = SFS(
    estimator=lr,
    forward=False,
    floating=False,
    k_features=9,
    scoring="accuracy",
    cv=0
)

# Fit the model to X and y
sbs.fit(X, y)

# Print the features that were chosen and check the model accuracy
# print(sbs.subsets_[9]) 
sbs_accuracy = round(sbs.subsets_[9]["avg_score"]*100,2)
sbs_features = sbs.subsets_[9]["feature_names"]
print("SBS Accuracy = " + str(sbs_accuracy) + "%")
print("SBS Features = " + str(sbs_features))

# Plot the model accuracy as a function of the number of features used
plot_sfs(sbs.get_metric_dict())
plt.show()

##########################################
# Recursive Feature Elimination
##########################################
# Standardize the data
scaler = StandardScaler()
standardized_X = pd.DataFrame(scaler.fit_transform(X))

# Create a RFE model
rfe = RFE(lr, n_features_to_select=8)

# Fit the model to X and y
rfe.fit(standardized_X, y)

# Print the features that were chosen and check the model accuracy
rfe_features = [f for (f, support) in zip(standardized_X, rfe.support_) if support]
rfe_feature_names = []
for feature_index in rfe_features:
    rfe_feature_names.append(X.columns[feature_index])
rfe_accuracy = round(rfe.score(standardized_X, y)*100,2)
print("RFE Accuracy = " + str(rfe_accuracy) + "%")
print("RFE Features = " + str(rfe_feature_names))

##########################################
# Summary
##########################################
# Logistic Regression model accuracy............. 76.6%
# Sequential Forward Selection model accuracy.... 78.35% <-- best!
# Sequential Backward Selection model accuracy... 77.26%
# Recursive Feature Elimination model accuracy... 76.79%
 
# Sequential Forward Selection model features:
# Gender, Age, family_history_with_overweight, FAVC, CAEC, SCC, FAF, Bike, Walking

# Sequential Backward Selection model features:
# Age, family_history_with_overweight, FAVC, NCP, CAEC, CH20, SCC, FAF, Public_Transportation

# Recursive Feature Elimination model features:
# Age, family_history_with_overweight, FAVC, FCVC, CAEC, SCC, Automobile, Walking