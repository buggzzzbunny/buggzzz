#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn import preprocessing


# In[4]:


df = pd.read_csv('diabetes.csv')


# In[5]:


df.info()


# In[6]:


df.head()


# In[7]:


df.corr().style.background_gradient(cmap='BuGn')


# In[8]:


df.drop(['BloodPressure', 'SkinThickness'], axis=1, inplace=True)


# In[9]:


df.isna().sum()


# In[10]:


df.describe()


# In[11]:


hist = df.hist(figsize=(20,16))


# In[12]:


X=df.iloc[:, :df.shape[1]-1] #Independent Variables
y=df.iloc[:, -1] #Dependent Variable
X.shape, y.shape


# In[13]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# In[14]:


param_grid = {
 'n_neighbors': range(1, 51),
 'p': range(1, 4)
}
grid = GridSearchCV(estimator=KNeighborsClassifier(), param_grid=param_grid, cv=5)
grid.fit(X_train, y_train)
grid.best_estimator_, grid.best_params_, grid.best_score_


# In[20]:


knn(X_train, X_test, y_train, y_test, grid.best_params_['n_neighbors'], grid.best_params_['p'])


# In[ ]:




