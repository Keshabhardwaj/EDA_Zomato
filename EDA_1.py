#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


df=pd.read_csv('zomato.csv',encoding='latin-1')
df.head()


# In[12]:


df.columns


# In[13]:


df.shape


# In[14]:


df.info()


# In[15]:


df.describe()


# #In Data Analysis What All Things We Do
# 1.Missing Values
# 2.Explore About the Numerical Variables
# 3.Explore About categorical Variables
# 4.Finding Relationship between features

# In[16]:


df.shape


# In[17]:


df.isnull().sum()
# df=df.dropna()
# df.isnull().sum()


# In[18]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[19]:


df_country=pd.read_excel('Country-Code.xlsx')
df_country.head()


# In[20]:


df.columns


# In[21]:


final_df=pd.merge(df,df_country,on='Country Code', how='left')


# In[22]:


final_df.head(2)


# In[23]:


##To check Data Types
final_df.dtypes


# In[24]:


final_df.columns


# In[25]:


final_df.shape


# In[26]:


country_names=final_df.Country.value_counts().index
country_names


# In[27]:


country_val=final_df.Country.value_counts().values
country_val


# In[28]:


## Pie Chart- Top 3 countries that uses zomato
plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.3f%%')


# In[29]:


final_df.columns


# In[38]:


final_df.query(['Country Code'==1])


# In[ ]:





# In[23]:


final_df['City'].value_counts()


# as we have seen in noida and faridabad we can use discount policies to improve sales

# In[45]:


ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().
ratings


# In[46]:


ratings1=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[47]:


ratings1


# #Observation
# When Rating is between 4.5 to 4.9---> Excellent
# 
# 1.   When Rating is between 4.5 to 4.9---> Excellent
# 2.  When Rating are between 4.0 to 4.4--->very good
# 3. when Rating is between 3.5 to 3.9----> good
# 4. when Rating is between 3.0 to 3.4----> average
# 5. when Rating is between 2.5 to 2.9----> average
# 6. when Rating is between 2.0 to 2.4----> Poor
# 
# 
# 
# 

# In[48]:


ratings1.head()


# In[ ]:





# In[49]:


import matplotlib
# plt.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="Aggregate rating",y="Rating Count",data=ratings1)


# In[41]:


## Count plot
sns.countplot(x="Rating color",data=ratings1,palette=['blue','red','orange','yellow','green','green'])


# In[50]:


ratings


# In[51]:


s=final_df[final_df['Country']=='India'].groupby('City').size().reset_index()
s.shape


# In[52]:


### Find the countries name that has given 0 rating
final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# In[53]:


final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)


# Observations Maximum number of 0 ratings are from Indian customers

# In[23]:


##find out which currency is used by which country?
final_df.columns


# In[24]:


final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# In[25]:


## Which Countries do have online deliveries option


# In[26]:


final_df[final_df['Has Online delivery'] =="Yes"].Country.value_counts()


# In[27]:


final_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()


# Observations:
# 
# Online Deliveries are available in India and UAE

# In[28]:


final_df.columns


# In[29]:


## Create a pie chart for top 5 cities distribution


# In[27]:


city_values=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index


# In[31]:


plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')


# Assignment
# Find the top 10 cuisines

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




