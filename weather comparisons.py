#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


seattle=pd.read_csv("D:/csv/seattle_weather.csv",index_col=0)
seattle.head()


# In[6]:


austin=pd.read_csv("D:/csv/austin_weather.csv",index_col=0)
austin.head()


# In[7]:


fig,ax=plt.subplots()
ax.errorbar(seattle["MONTH"],seattle["MLY-TAVG-NORMAL"],yerr=seattle["MLY-TAVG-STDDEV"])
ax.set_xlabel("Month")
ax.set_ylabel("Avg Temp")
plt.show()


# In[8]:


fig,ax=plt.subplots()
ax.errorbar(seattle["MONTH"],seattle["MLY-TAVG-NORMAL"],yerr=seattle["MLY-TAVG-STDDEV"])
ax.errorbar(austin["MONTH"],austin["MLY-TAVG-NORMAL"],yerr=austin["MLY-TAVG-STDDEV"])

ax.set_xlabel("Month")
ax.set_ylabel("Avg Temp")
plt.show()


# In[10]:


#scatter plot
climate=pd.read_csv("D:/csv/climate_change.csv",parse_dates=True, index_col=0)
climate


# In[11]:


fig, ax=plt.subplots()
ax.scatter(climate["co2"],climate["relative_temp"])
ax.set_xlabel("CO2 in PPM")
ax.set_ylabel("Relative Temp in C")
plt.show()


# In[12]:


#multiple scatter plot
eighties=climate["1980-01-01":"1989-12-31"]
eighties.head()


# In[13]:


ninties=climate["1990-01-01":"1999-12-31"]
ninties.head()


# In[14]:


fig,ax=plt.subplots()
ax.scatter(eighties["co2"],eighties["relative_temp"],color="r", label="eighties")
ax.scatter(ninties["co2"],ninties["relative_temp"],color="b", label ="ninties")
ax.legend()
ax.set_xlabel("CO2 in PPM")
ax.set_ylabel("Relative Temp in C")
plt.show()


# In[16]:


fig, ax=plt.subplots()
ax.scatter(climate["co2"],climate["relative_temp"],c=climate.index)
ax.set_xlabel("CO2 in PPM")
ax.set_ylabel("Relative Temp in C")
plt.show()


# In[ ]:




