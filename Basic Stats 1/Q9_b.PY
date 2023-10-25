#skewness, kurtosis and Inferences

import pandas as pd
df=pd.read_csv("Q9_b.csv")
df.shape
df
#Skewness, Kurtosis of speed
df['SP'].describe()
df['SP'].hist()
df['SP'].skew()
df['SP'].kurt()

#Skewness, Kurtosis of dist
df['WT'].describe()
df['WT'].hist()
df['WT'].skew()
df['WT'].kurt()

import matplotlib.pyplot as plt
plt.scatter(x=df['SP'], y=df['WT'])
plt.show()
df[['SP','WT']].corr()

'''
import matplotlib.pyplot as plt

# Create some data and plots
x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 7, 9]
plt.scatter(x, y)
plt.plot(x, y)

# Display the plots
plt.show()
'''