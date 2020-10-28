#   3)   Pick at least two Scikit-learn classification models, set up each models using the provided training data with the idea of classifying future data by “Make”. 
#        Compare and contrast the results, then provide a recommendation on which model you prefer.

# Naive-Bayes
# Logistic Regression

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
import pandas as pd

# import some data to play with
# iris = datasets.load_iris()

make = pd.read_csv(r'C:\Users\us5608\OneDrive - NAGases\Desktop\Other\Interview_ProUnimited\Test Data.csv') # Import the CSV file using pandas library
make = make[["Make","Horsepower (rpm)","Torque (rpm)"]]
make = make.dropna()
make['Make'] = make['Make'].replace(['BMW','Ford','Toyota'],[0,1,2])

# print(make)

X = []
Y = []
i = 0

for iteration in make['Make'].values:
    
    X.append([make['Horsepower (rpm)'].values[i], make['Torque (rpm)'].values[i]])
    Y.append(make['Make'].values[i])
    i+=1

# print(type(X))
# print(type(Y))

X = np.array(X)
Y = np.array(Y)


logreg = LogisticRegression(C=1e5)

# Create an instance of Logistic Regression Classifier and fit the data.
logreg.fit(X, Y)

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, x_max]x[y_min, y_max].
x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

h = 2  # step size in the mesh

xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.figure(1, figsize=(4, 3))
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
plt.xlabel('Horsepower (rpm)')
plt.ylabel('Torque (rpm)')

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())

plt.show()