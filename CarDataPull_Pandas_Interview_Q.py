# With the attached data set, please show the Python script within a text file which would achieve the following:
 
#   1)   A unique list of Trim values (column d) separated from condition and description
#   2)   An array with average MSRP by Make and Year

import os 
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

# Step 1: Create Dataframe and format Column Header
    
df = pd.read_csv(r'C:\Users\us5608\OneDrive - NAGases\Desktop\Other\Interview_ProUnimited\Test Data.csv') # Import the CSV file using pandas library

#   1)   A unique list of Trim values (column d) separated from condition and description

df.rename(columns={'Condition_Trim (description)':'trim'}, inplace=True) # Replace a specific column header 

# Step 2: Slpit the element at the underscore to separate condition and description 

df["trim"]= df["trim"].str.split("_", n = 1, expand = False) # new data frame with split value columns 

xa = np.unique(df.trim.values) # numpy array of unique values
xl = np.ndarray.tolist(xa) # Convert numpy array to a list

print("\nOriginal Number of Values:",len(df.trim.values)) # Print Answer to Number 1
print("\n\nNumber of Unique Values:", len(xl))
print("\n\nThe final list asked for in Number 1 with condition separated from description:\n\n\n",xl)

#   2)   An array with average MSRP by Make and Year

# plt.figure().suptitle('Average MSRP by Make', fontsize=20)
# Make_MSRP_Plot = df.groupby('Make')['MSRP'].mean().plot(kind = 'bar')
# plt.ylabel('Average MSRP')
# plt.xlabel = ('Make')

# plt.figure().suptitle("Average MSRP by Year", fontsize=20)
# Year_MSRP_Plot = df.groupby('Year')['MSRP'].mean().plot(kind = 'bar')
# plt.ylabel('Average MSRP')
# plt.xlabel = ('Year')

# Make_MSRP = df.groupby('Make', as_index=False)['MSRP'].mean()
# print("\n\nAverage MSRP by Make:\n\n", Make_MSRP)

# Year_MSRP = df.groupby('Year', as_index=False)['MSRP'].mean()
# print("\n\nAverage MSRP by Year:\n\n", Year_MSRP)

plt.figure().suptitle('Average MSRP by Make and Year', fontsize=20)
Make_MSRP_Plot = df.groupby(['Make','Year'])['MSRP'].mean().plot(kind = 'bar')
plt.ylabel('Average MSRP')
plt.xlabel = ('Make/Year')

Year_MSRP = df.groupby(['Make','Year'], as_index=False)['MSRP'].mean()
print("\n\nAverage MSRP by Make and Year:\n\n", Year_MSRP)

plt.show()

