import os 
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import pandas as pd

# 1) First, look at data. What is the average number of SafeGraph visitors to Temple University during the teaching days of the Fall 2019 semester? 
# Roughly what percent of the Temple student population is this?

df = pd.read_csv(r"C:\Users\us5608\OneDrive - NAGases\Desktop\Other\Brendan\temple_traffic.csv") #create dataframe 

df.date = pd.to_datetime(df.date) 
df.insert(0,"datenumber", df.date.dt.weekday)

# print(df.head(10))
# print(df.columns)
# print(df.visits)

df2 = df[["datenumber","date","temp","visits"]]
# print(df2.head(3))
df3 = df2[(df2["datenumber"]<5) & (df2["date"] >= "2019-08-26") & (df2["date"] <= "2019-11-24")]

avg_visitors = round(df3['visits'].mean(),2)
student_population = 39740
percentage = "{0:.2%}".format((avg_visitors/student_population)*100)

print("1) Average number of visitors during the fall 2019 semester:", avg_visitors, "visitors")
print("This is ",percentage," of the student population")

# print(df3.head(100))

plt.scatter(df3.temp, df3.visits)
plt.title('Visits vs. Temp')
plt.show()

# This produces a dataframe of correlations
correlation = df.corr()
# print("Correlation: ", correlation)


# 2) Specify (write out the regression equation), run, and interpret a regression that documents the relationship 
# between temperature and foot traffic (visits) on campus.

# The library statsmodel has a nice module for running regressions

res = smf.ols('visits ~ temp', data = df3).fit() # run the regressions 
print("Regression Summary: ", res.summary()) # display regression summary 

# Interpret with the following methods: 

print("r-squared: ", res.rsquared) # r squared - Tells us the goodness of the fit. Value of 0 to 1
print("Coefficients: ", res.params) # coeficcients - slope and intercept. intercept tells you how much of dependent variable at independent variale = 0 , slope tells tells you result per increment
print("P-values: ", res.pvalues) # p-values thenull hypothesis for each coefficient is that it is zero. if pvalue <.05 then reject the null hypothsis  

print("Done")