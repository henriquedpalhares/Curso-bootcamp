# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, model_selection

# Define some sample data
# In this example, we're trying to predict whether a fruit is an apple or an orange based on its weight and texture.
# '0' represents smooth, and '1' represents bumpy texture.
features = [[140, 0], [130, 0], [150, 1], [170, 1]]
labels = [0, 0, 1, 1]  # 0 represents apple, 1 represents orange

# Create a decision tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier on the data
clf = clf.fit(features, labels)

# Make predictions
# Here, we're trying to predict the type of fruit for a fruit with weight 160 and bumpy texture (1).
prediction = clf.predict([[160, 1]])

# Interpret the prediction
if prediction[0] == 0:
    print("It's an apple!")
else:
    print("It's an orange!")