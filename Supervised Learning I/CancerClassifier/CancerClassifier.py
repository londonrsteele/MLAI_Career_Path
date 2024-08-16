# Filename : cancer_classifier.py
# Author   : LR Steele
# Info     : Coding project/objective for "Supervised Learning I: Regressors,
#          : Classifiers, and Trees" section of Machine Learning Fundamentals
#          : course in Machine Learning/AI Engineer Career Path on Codecademy.
# Data     : see breast_cancer_README.md for more information
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Load and Investigate Data
breast_cancer_data = load_breast_cancer()
print(breast_cancer_data.data[0])
print(breast_cancer_data.feature_names)
print(breast_cancer_data.target[0])
print(breast_cancer_data.target_names)

# Some notes about the dataset:
#   0 = malignant
#   1 = benign

# Splitting the data into Training and Validation sets
training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size=0.2, random_state=100)
# Note: we're splitting the data 20% training, 80% validation
# Note: random_state = 100 ensures that each time we run the code, 
# the data is split in the same way.

# Ensure split performed correctly - should have one label in training_labels
# for each data point in training_data
print("Training data length: " + str(len(training_data)))
print("Training data labels length:" + str(len(training_labels)))
# 455 for each - check!

# Running the Classifier
# running in a loop to determine best k
accuracies = []
k_list = range(1, 101)
for k in k_list:
    # note: n_neighbors == "k"
    classifier = KNeighborsClassifier(n_neighbors=k)

    # Train the classfier
    classifier.fit(training_data, training_labels)

    # Find classifier's accuracy (score) on validation set
    accuracies.append(classifier.score(validation_data, validation_labels))
    print("k of " + str(k) + " accuracy (score) on validation = " + str(accuracies[k-1])) # k-1 bc index is 0 and range is 1

# Graphing the results to determine best k
plt.plot(k_list, accuracies)
plt.title("Breast Cancer Classifier Accuracy")
plt.xlabel("k")
plt.ylabel("Validation Accuracy")
plt.show()

# best k appears to be at k=23!