#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


from pymongo import MongoClient


# In[6]:


# uri = [insert yours]
# db = MongoClient(uri, ssl=True, tlsAllowInvalidCertificates=True)[yours]


# In[7]:


pnad = db.pnad23_gdcbs


# In[2]:


df = pd.read_csv("pnad23.csv")


# In[3]:


df


# In[4]:


records = df.to_dict('records')


# In[8]:


pnad.insert_many(records)


# In[9]:


pnad.find_one()

