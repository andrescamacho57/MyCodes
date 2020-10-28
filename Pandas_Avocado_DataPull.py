# 2. Avocado price and demand (6 points)
# For this exercise, use our familiar avocado dataset.

# For the following cities, run a multiple regression that investigates the relationship between demand and price while simultaneously accounting for the effect
#  or regions and avocado types.

import os 
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

cities = ['Philadelphia', 'NewYork', 'BaltimoreWashington', 'Boston', 'Chicago', 'SanFrancisco']

df = pd.read_csv(r"C:\Users\us5608\OneDrive - NAGases\Desktop\Other\Brendan\avocado.csv")

# How to select rows from a DataFrame based on column values
# To select rows whose column value is in an iterable, some_values, use isin:
#df.loc[df['column_name'].isin(some_values)]
#https://stackoverflow.com/questions/17071871/how-to-select-rows-from-a-dataframe-based-on-column-values

df1 = df. loc[df['region'].isin(cities)]

#https://sodocumentation.net/matplotlib/topic/3279/multiple-plots
#  fig, axes = plt.subplots(3,1) #,figsize=(8, 6), sharey=True)

# axes[0,0].set_title("Average Price vs. Total Volume")
# axes[0,1].set_title("Average Price vs. Type")
# axes[1,0].set_title("Average Price vs. Region")

# axes[0,0].plot(df1['Total Volume'], df1.AveragePrice)
# axes[0,1].plot(df1.type, df1.AveragePrice)
# axes[1,0].plot(df1['region'], df1.AveragePrice)

# plt.show()

# plt.subplot(3,1,1)
# a = plt.scatter(df1['Total Volume'], df1.AveragePrice)
# plt.ylabel('Average Price')
# plt.xlabel = ('Total Volume')

# plt.subplot(3,1,2)
# b = plt.bar(df1.type, df1.AveragePrice.mean())
# plt.ylabel('Average Price')
# plt.xlabel = ('Type')

# plt.subplot(3,1,3)
# c = plt.bar(df1.region, df1.AveragePrice)
# plt.ylabel('Average Price')
# plt.xlabel = ('Region')



# plt.show()

# This produces a dataframe of correlations
# correlation = df.corr()
# print("Correlation: ", correlation)

# Specify the regression equation.

# Run the regression.

# A way to ‘quote’ variable names, especially ones that do not otherwise meet Python’s variable name rules.
# Patsy built in Q function
# https://patsy.readthedocs.io/en/latest/builtins-reference.html#patsy.builtins.Q

res = smf.ols('\nAveragePrice ~ Q("Total Volume") + type + region', data = df1).fit() # run the regressions 
print("\nRegression Summary: ", res.summary()) # display regression summary 

# Interpret the regression results (remember the 3 steps).

print("\nr-squared: ", res.rsquared) # r squared - Tells us the goodness of the fit. Value of 0 to 1
print("\nCoefficients: ", res.params) # coeficcients - slope and intercept. intercept tells you how much of dependent variable at independent variale = 0 , slope tells tells you result per increment
print("\nP-values: ", res.pvalues) # p-values thenull hypothesis for each coefficient is that it is zero. if pvalue <.05 then reject the null hypothsis  

print("\nDone")


# Additionally, answer the following questions:

# Which region seems to be most expensive? Least?

x = df1.groupby('region')['AveragePrice'].mean().plot(kind = 'bar')
plt.figure()

print('\nA) The most expensive region is San Fransisco and the least expensive is Boston')

# On average, how much more expensive are organic avocados (vs. conventional avocados)?

x2 = df1.groupby('type')['AveragePrice'].mean().plot(kind = 'bar')
plt.figure()

df2 = df1.groupby('type', as_index=False)['AveragePrice'].mean()
print(df2)

difference = round(1.8930-1.3689,2)
print('\nB) On average the Organic Avocados are $',difference,' more expensive.')
plt.show()