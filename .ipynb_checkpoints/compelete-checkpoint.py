#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


completeData = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv")


# In[3]:


completeData


# In[4]:


allData = completeData[["Country_Region" , "Last_Update" , "Lat" , "Long_" , "Confirmed" , "Deaths" , "Recovered" , "Active"]]


# In[5]:


allData


# In[6]:


newData = pd.DataFrame({"Country": allData["Country_Region"] ,"Date": allData["Last_Update"] , "Lat": allData["Lat"] , "Confirmed": allData["Confirmed"] , "Deaths": allData["Deaths"] , "Recovered": allData["Recovered"] , "Active": allData["Active"]})


# In[7]:


newData


# In[8]:


newData.to_csv("./complete.csv")


# In[ ]:




