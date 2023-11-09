#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn import preprocessing


# In[2]:


df = pd.read_csv('emails.csv')


# In[3]:


df.info()


# In[4]:


df.head()


# In[5]:


df.dtypes


# In[6]:


df.drop(columns=['Email No.'], inplace=True)


# In[7]:


df.isna().sum()


# In[8]:


df.describe()


# In[9]:


X=df.iloc[:, :df.shape[1]-1] #Independent Variables
y=df.iloc[:, -1] #Dependent Variable
X.shape, y.shape


# In[10]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)


# In[11]:


models = {
"K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=2),
"Linear SVM":LinearSVC(random_state=8, max_iter=900000),
"Polynomical SVM":SVC(kernel="poly", degree=2, random_state=8),
"RBF SVM":SVC(kernel="rbf", random_state=8),
"Sigmoid SVM":SVC(kernel="sigmoid", random_state=8)
}


# In[13]:


X_test = np.array(X_test)
X_train = np.array(X_train)


# In[14]:


for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print(f"Accuracy for {model_name} model: {accuracy}")


# In[ ]:




