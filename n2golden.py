import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import numpy as np

# Load the dataset
df = pd.read_csv("C:\\Users\\HP\\Downloads\\email spam\\emails.csv")

# Visualize spam distribution with a pie chart
plt.figure(figsize=(6, 6))
df['spam'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'orange'])
plt.title('Spam Distribution')
plt.ylabel('')
plt.show()

# Prepare data
X = df['text'].astype(str)
y = df['spam'].replace({0: "Not Spam", 1: "Spam"}).astype("object")

# Plot box plot of email lengths
plt.figure(figsize=(8, 6))

plt.ylabel('Email Length')
plt.title('Box Plot of Email Lengths')
plt.grid(True)
plt.show()

# Plot violin plot of email lengths vs. spam
plt.figure(figsize=(8, 6))

plt.xlabel('Spam')
plt.ylabel('Email Length')
plt.title('Violin Plot of Email Lengths vs. Spam')
plt.grid(True)
plt.show()

# Train and evaluate Naive Bayes classifier
class NaiveBayes:
    def __init__(self):
        self.log_prior = {}
        self.log_likelihood = {}
    
    def fit(self, X, y):
        classes, counts = np.unique(y, return_counts=True)
        total_docs = len(y)
        for cls, count in zip(classes, counts):
            self.log_prior[cls] = np.log(count / total_docs)
            class_indices = np.where(y == cls)
            word_counts = X[class_indices].sum(axis=0)
            total_words = word_counts.sum()
            
    
    def predict(self, X):
        predictions = []
        for doc in X:
            posterior = {}
            for cls in self.log_prior:
                posterior[cls] = self.log_prior[cls] + np.dot(doc, self.log_likelihood[cls])
            predictions.append(max(posterior, key=posterior.get))
        return predictions

# Plot confusion matrix (not implemented in this modification)

# Test with custom messages (not implemented in this modification)
