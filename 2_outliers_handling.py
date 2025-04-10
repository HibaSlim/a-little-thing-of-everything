import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Set random seed for reproducibility
np.random.seed(42)

#Generate 1,000 data points from a normal distribution (mean=50, std=10)
data = np.random.randn(1000) * 10 + 50

#Introduce some extreme values (outliers)
outliers = np.array([150, 160, -20, -30])
data_with_outliers = np.concatenate([data, outliers])

#Create a DataFrame
df = pd.DataFrame(data_with_outliers, columns=['value'])

#define the lower bound and the upper bound

q1= df['value'].quantile(0.25)
q3= df['value'].quantile(0.75)
iqr= q3-q1 # inter quantile range

lower_bound= q1 - 1.5*iqr
upper_bound= q3 + 1.5*iqr
#removing outliers
cleaned_df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]
print(cleaned_df)
print(df.describe())
#capping or winsorizing(the outliers get the values of the upper or lower bound)
df['value_capped']=np.where(df['value']>upper_bound,upper_bound,np.where(df['value']<lower_bound,lower_bound,df['value']))

print(df.describe())
