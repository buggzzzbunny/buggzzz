#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv('sales_data_sample.csv', encoding='latin1')
df.head()


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


numeric_df = df.select_dtypes(include=['number'])
fig = plt.figure(figsize=(12, 10))
sns.heatmap(numeric_df.corr(), annot=True, fmt='.2f')
plt.show()


# In[15]:


df= df[['PRICEEACH', 'MSRP']]
df.head()


# In[7]:


df.isna().any()


# In[8]:


df.describe().T


# In[9]:


df.shape


# In[10]:


from sklearn.cluster import KMeans
inertia = []

for i in range(1, 11):
    clusters = KMeans(n_clusters=i, init='k-means++', random_state=42)
    clusters.fit(df)
    inertia.append(clusters.inertia_)

plt.figure(figsize=(6, 6))
sns.lineplot(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], y=inertia)


# In[11]:


kmeans = KMeans(n_clusters = 3, random_state = 42)
y_kmeans = kmeans.fit_predict(df)
y_kmeans


# In[12]:


plt.figure(figsize=(8,8))
sns.scatterplot(x=df['PRICEEACH'], y=df['MSRP'], hue=y_kmeans)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c = 'red', label = 'Centroids')
plt.legend()


# In[13]:


kmeans.cluster_centers_


# In[ ]:




