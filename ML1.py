#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pylab
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
from sklearn import preprocessing


# In[2]:


df = pd.read_csv('uber.csv')


# In[3]:


df.info()


# In[4]:


df.head()


# In[5]:


df.describe()


# In[6]:


df = df.drop(['Unnamed: 0', 'key'], axis=1)
df.isna().sum()


# In[7]:


df.dropna(axis=0,inplace=True)
df.dtypes


# In[8]:


df["pickup_datetime"] = pd.to_datetime(df["pickup_datetime"])


# In[9]:


df.dtypes


# In[10]:


df= df.assign(
second = df.pickup_datetime.dt.second,
minute = df.pickup_datetime.dt.minute,
hour = df.pickup_datetime.dt.hour,
day= df.pickup_datetime.dt.day,
month = df.pickup_datetime.dt.month,
year = df.pickup_datetime.dt.year,
dayofweek = df.pickup_datetime.dt.dayofweek
)
df = df.drop('pickup_datetime',axis=1)


# In[11]:


df.head()


# In[12]:


plt.scatter(df['pickup_latitude'], df['fare_amount'])
plt.xlabel("pickup_latitude")
plt.ylabel("fare_amount")


# In[13]:


plt.figure(figsize=(20,12))
sns.boxplot(data = df)


# In[14]:


corr = df.corr()
corr.style.background_gradient(cmap='BuGn')


# In[15]:


X=df.iloc[:, :df.shape[1]-1] #Independent Variables
y=df.iloc[:, -1]
from sklearn.model_selection import train_test_split

# Assuming you have already defined your features X and target y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


# In[16]:


from sklearn.linear_model import LinearRegression
regression = LinearRegression()


# In[17]:


regression.fit(X_train,y_train)
regression.intercept_
regression.coef_
prediction = regression.predict(X_train)


# In[18]:


print(prediction)


# In[19]:


y_test


# In[ ]:





# In[ ]:




