
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# In[28]:


data=pd.read_csv('50_Startups.csv')
data


# In[29]:


data.head()


# In[30]:


data.shape


# In[5]:


data.describe()


# In[36]:


X=data.iloc[:,:4].values
X


# In[84]:


y=data.iloc[:,4].values
y


# In[24]:


from sklearn.preprocessing import OneHotEncoder,LabelEncoder


# In[37]:


labelencoder=LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder=OneHotEncoder(categorical_features=[3])
X=onehotencoder.fit_transform(X).toarray()


# In[62]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)


# In[64]:


X_test


# In[53]:


reg=LinearRegression()
reg.fit(X_train,y_train)


# In[54]:


reg.score(X_train,y_train)


# In[66]:


y=reg.predict(X_test)
y


# In[80]:


plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train, 
            color = "green", s = 10, label = 'Train data') 
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test, 
            color = "green", s = 10, label = 'Train data') 
plt.hlines(y=-50000,xmin=0,xmax=60000,color='red',linewidth=2)
  

