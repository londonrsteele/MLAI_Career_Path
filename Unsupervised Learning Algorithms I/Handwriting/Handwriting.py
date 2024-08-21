# Filename : TennisAce.py
# Author   : LR Steele
# Info     : Coding project/objective for "Unupervised Learning Algorithms I"
#          : section of Machine Learning Fundamentals course in the 
#          : Machine Learning/AI Engineer Career Path on Codecademy.
# Data     : see digits_README.md for more information
# Note     : Any comment in "quotes" is from Codecademy.
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

# Load and Inspect Data
Digits_dataset = datasets.load_digits()
# print(Digits_dataset.DESCR)
# print(Digits_dataset.data)
# print(Digits_dataset.target)

# "Let's visualize the image at index 100." 
# plt.gray()
# plt.matshow(Digits_dataset.images[100])
# plt.show()

# Note: 1797 instances of 64 attributes.
# Each instance is an 8x8 image of integer pixels in the range [0,16].
# The 8x8 image is stored in a 64x1 list.
# 0 is white, 16 is black.

# K Means Clustering
# "Because there are 10 digits, there should be 10 clusters. Set k = 10."
# "The random_state will ensure every time you run your code, the model is 
# built in the same way. This can be any number. We used 42."
kmeans_model = KMeans(n_clusters=10, random_state=42)
# Fit the data to the model
kmeans_model.fit(Digits_dataset.data)

# Visualizing after K Means
# "Let's visualize all the centroids! Because data samples live in a 64-d space,
# the centroids have values so they can be images!"
fig = plt.figure(figsize=(8,3))
fig.suptitle("Centriod Images", fontsize=14, fontweight="bold")
for i in range(10):
    # "Initizlize subplots in a grid of 2x5, at i+1th position"
    ax = fig.add_subplot(2,5,i+1)
    # "Display images"
    ax.imshow(kmeans_model.cluster_centers_[i].reshape((8,8)), cmap=plt.cm.binary)
plt.show()