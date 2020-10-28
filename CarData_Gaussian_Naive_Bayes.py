from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np



make = pd.read_csv(r'C:\Users\us5608\OneDrive - NAGases\Desktop\Other\Interview_ProUnimited\Test Data.csv') # Import the CSV file using pandas library
make = make[["Make","Horsepower (rpm)","Torque (rpm)"]]
make = make.dropna()
# make['Make'] = make['Make'].replace(['BMW','Ford','Toyota'],[0,1,2])

print(len(make))

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

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.5, random_state=0)
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print("Number of mislabeled points out of a total %d points : %d"

% (X_test.shape[0], (y_test != y_pred).sum()))
