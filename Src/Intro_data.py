# Author       : Chinmay Tagare
# Last Updated : 06-June-2021

import pandas as pd

data_path = "D:\\Chinmay\\GitHub\\Data-Analysis-with-Pandas\\Data-Analysis-with-Pandas\\Data_Sets\\avocado.csv"
df = pd.read_csv(data_path)
# =============================================================================
# print(df.head(3))
# print(df.tail(2))
# for col in df.columns:
#     print(col)
# print(df["AveragePrice"])
# print(df["AveragePrice"].head())
# =============================================================================

# =============================================================================
# albany_df = df[ df["region"]=='Albany' ]
# print(albany_df.head())
# =============================================================================
# setting index as date
# inplace will modify the original df
# albany_df.set_index("Date", inplace = True)
# to set into new df, use following --> 
# albany_df = df[ df["region"]=='Albany' ]
# albany_df_date_idx = albany_df.set_index("Date")
# print(albany_df_date_idx)

# Plots the graph
# albany_df_date_idx.plot()
# albany_df_date_idx["AveragePrice"].plot()

# Pandas didnt recognize that date is a date format. so x axis will look wierd
# convert date column in date format

# =============================================================================
# df["Date"] = pd.to_datetime(df["Date"])
# albany_df = df[df["region"] == "Albany"]
# albany_df = albany_df.set_index("Date")
# 
# # albany_df["AveragePrice"].plot()
# # 
# albany_df = albany_df.sort_index()
# print(albany_df)
# # 25 moving average
# albany_df["AveragePrice"].rolling(25).mean().plot()
# # 
# # =============================================================================
# # Creating new column as price 25 moving average
# 
# albany_df["Price_25_MA"] = albany_df["AveragePrice"].rolling(25).mean()
# print(albany_df.head()) # first 25 - nothing to calculate, that;s why it NaN
# 
# print(albany_df.tail())
# 
# # dropping NA
# albany_df.dropna().head() # now we got the values in head - dropped NaN
# =============================================================================

# BEST PRACTICE TO AVOID WARNINGS --> create copy of original df
albany_df = df.copy()[df["region"] == "Albany"]
albany_df.set_index("Date", inplace = True)
albany_df.sort_index(inplace = True)
albany_df["Price_25_MA"] = albany_df["AveragePrice"].rolling(25).mean()
albany_df = albany_df.dropna()

print(albany_df)






























