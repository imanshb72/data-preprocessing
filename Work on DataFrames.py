#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


import arabic_reshaper
from bidi.algorithm import get_display
from arabic_reshaper import reshape


# In[74]:


df = pd.read_excel('H:\\Work\\Takhfifan\\Reports\\Details\\After Merge\\98.10\\Total - 1398.10.01 to 1398.10.29.xlsx',dropna = True)
pd.set_option('display.max_columns', None)


# In[75]:


df.drop_duplicates(subset = 'mobile').drop(columns = 'log').head()


# In[6]:


df1 = df.groupby(['city','status_label'])['mobile'].count().reset_index()
df1.sort_values('mobile',ascending = False)


# In[7]:


df1['mobile_bins'] = pd.cut(df1['mobile'],bins = [0,49,99,149,199,249,299,349,399,449,500],labels = ['fist fifty','second fifty','third fifty','forth fifty','fifth fifty','sixth fifty','seventh fifty','eighth fifty','ninth fifty','tenth fifty']) # 'labels' is Optional
df1


# In[10]:


df1['mobile_bins'].mode()[0]


# In[11]:


df1['city'].value_counts()


# In[12]:


df.iloc[:,[8,10,12]]


# In[13]:


df[df['Canceled_by'] == 'Customer']['parent_id']    #Vlookup


# In[26]:


df2 = (df1['mobile'] > 80) & (df1['mobile'] < 140)
#df2 = df1['mobile'].gt(80) & df1['mobile'].lt(140)     # equals to the upper line
df1.where(df2)


# In[29]:


df['city'].unique()
#df['city'].nunique()


# In[37]:


df3 = df1.set_index(['city','status_label'])
#df3
df3.loc[[('اردبیل','Cancelled'),('اردبیل','Finalize')]]


# In[66]:


df4 = df.copy()
df4['Vendor_type'] = df4['Vendor_name'].replace(to_replace = '[ ].*',value = '',regex = True)   
#def splitt(x):
#    x['Vendor_type'] = str(x['Vendor_name']).split(' ')[0]
#    return x
#df4 = df4.apply(splitt,axis = 'columns')
df4.head()


# In[76]:


del([df['e'],df['log']])
df.head()


# In[77]:


df['date'] = pd.to_datetime(df['request_da'])
df.head()


# In[78]:


df.rename(mapper = lambda x:x.upper(),axis = 1)


# In[285]:


# requests by city
plt.figure(figsize = (20,8))
x1 = [get_display(reshape(i)) for i in df1['city']]
plt.bar(x1,df1['mobile'])
plt.ylabel('Requests')
plt.legend([get_display(reshape(i)) for i in ['شهر']])
# plt.savefig('C:\\Users\\Iman\\Desktop\\fig.jpg',dpi = 500)
plt.show()


# In[ ]:




