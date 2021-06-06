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

albany_df = df[ df["region"]=='Albany' ]
print(albany_df.head())