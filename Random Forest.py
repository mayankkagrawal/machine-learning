
# coding: utf-8

# In[40]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# In[41]:


data=pd.read_csv('Position_Salaries.csv')
data


# In[42]:


X=data.iloc[:,1:2].values
y=data.iloc[:,2].values
y


# In[43]:


from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 200, random_state = 0)
regressor.fit(X_train, y_train)


# In[44]:


y_pred = regressor.predict(X_test)
y_pred


# In[45]:


from sklearn import metrics


# In[46]:


print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  


# In[47]:


z=print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# In[48]:


# random forest classification


# In[66]:


df=pd.read_csv('bill_authentication.csv')
df


# In[67]:


X=df.iloc[:,0:4].values
y=df.iloc[:,4].values


# In[69]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)


# In[72]:


regressor = RandomForestRegressor(n_estimators = 20, random_state = 0)
regressor.fit(X_train, y_train)

