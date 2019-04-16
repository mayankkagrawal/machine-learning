
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# In[2]:


data=pd.read_csv('Position_Salaries.csv')


# In[3]:


data


# In[36]:


X=data.iloc[:,1:2].values
X


# In[35]:


y=data.iloc[:,2].values
y


# In[37]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


# In[8]:


X_train.shape


# In[11]:


from sklearn.linear_model import LinearRegression
reg=LinearRegression()


# In[16]:


plt.scatter(X,y,color='red')


# In[59]:


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


# In[65]:


reg=LinearRegression()
reg.fit(X,y)
reg.predict(X)
poly=PolynomialFeatures(degree=4)
X_poly=poly.fit_transform(X)


# In[66]:


poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


# In[67]:


plt.scatter(X,y,color='red')
plt.plot(X, lin_reg_2.predict(poly.fit_transform(X)), color = 'red') 


# In[68]:


plt.scatter(X,y,color='red')
plt.plot(X, reg.predict(X), color = 'red')

