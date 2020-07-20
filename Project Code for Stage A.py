#!/usr/bin/env python
# coding: utf-8

# Importation of libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
from scipy.stats import kurtosis,skew


# Importing dataset and converting it to excel format

# In[2]:


df = pd.read_csv("https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv")
df.to_excel('StageADataset.xlsx', index = False)


# Loading dataset from excel

# In[3]:


df = pd.read_excel('StageADataset.xlsx')


# In[4]:


df.info


# In[5]:


byfuelcode = df.groupby('fuel_type_code_pudl').mean()
byfuelcode


# The fuel type with the lowest average fuel_cost_per_unit_burned is Gas

# In[6]:


df.describe()


# In[7]:


print( 'The kurtosis of fuel quantity burned is: {}'.format( kurtosis(df['fuel_qty_burned']) ))
print( 'The skewness of fuel quantity burned is: {}'.format( skew(df['fuel_qty_burned']) ))


# Checking for missing data

# In[8]:


df.isna().sum()


# In[9]:


df.dtypes


# Checking for the type of object the column contains

# In[10]:


df['fuel_unit'].value_counts()


# Dealing with missing data using mode imputation

# In[11]:


df['fuel_unit'].fillna(df['fuel_unit'].mode()[0],inplace=True)


# In[12]:


df.isnull().any()


# In[13]:


plt.figure(figsize=(10,6)) # Set the size of the plot
sns.heatmap(df.corr(),annot=True) # Correlation Heatmap


# From the heatmap, the second and third lowest correlation value for fuel_cost_per_unit_burned is (-0.19) for fuel_qty_burned and (-0.01)fuel_mmbtu_per_unit

# In[14]:


df_aggregate= df.groupby(["report_year", "fuel_type_code_pudl"], as_index=False)["fuel_cost_per_unit_burned"].count()
print(df_aggregate)

coal_1994_percent = (475/1235) * 100
coal_1998_percent = (431/1107) * 100

percentage_change = coal_1998_percent - coal_1994_percent
print('The percentage change for fuel type coalin the cost per unit burned in 1998 compared to 1994 is:',percentage_change)


# In[15]:


byreport_year = df.groupby('report_year').mean()
byreport_year


# The year with the highest average for fuel_cost_per_unit_delivered is year 1997
