#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import numpy as np

df1 = pd.read_csv('/Users/jennielee/Documents/PSU 2020-2021/WINTER2021/CS510/Labs/Data Integration/COVID_county_data.csv')
df2 = pd.read_csv('/Users/jennielee/Documents/PSU 2020-2021/WINTER2021/CS510/Labs/Data Integration/acs2017_census_tract_data.csv')

df1
df2

df1_counties = df1.loc[(df1['county']=='Loudoun') | (df1['county']=='Washington') | (df1['county']=='Harlan') | (df1['county']=='Malheur')]
#print(df1_counties)

df2_counties = df2.loc[(df2['County']=='Loudoun County') | (df2['County']=='Washington County') | (df2['County']=='Harlan County') | (df2['County']=='Malheur County')]
#print(df2_counties)

agg_totalpop = df2_counties["TotalPop"].groupby(df2_counties["County"]).sum()
print(agg_totalpop)

total_cases = df1["cases"].groupby(df1["county"]).sum()
total_deaths = df1["deaths"].groupby(df1["county"]).sum()

print(total_cases)
print(total_deaths)


# In[ ]:




