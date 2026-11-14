#1 Load libraries for the project
import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

path = kagglehub.dataset_download("neuromusic/avocado-prices")
print("Path to dataset files:", path)
df = pd.read_csv(os.path.join(path, "avocado.csv"))
print(df.head())

#2 Create dictionary data structure and data frame
dictionary = {
    "type": ["conventional", "organic", "organic"],
    "region": ["Albany", "Boston", "Chicago"],
    "AveragePrice": [1.33, 1.85, 1.62],
}
df_dictionary = pd.DataFrame(dictionary)
print("\nExample of the Data Frame from the dictionary")
print(df_dictionary)

#3 Create Data frame from list of lists

list_ex = [
    ["conventional", "Albany", 1.33],
    ["organic", "Boston", 1.85],
    ["organic", "Chicago", 1.62],
]
df_list = pd.DataFrame(list_ex, columns=["type", "region", "AveragePrice"])
print("\nExample of the Data Frame from the list of lists")
print(df_list)

#4 Load data from CSV and XLSX files
df.to_csv("avocado.csv", index=False)
df_csv = pd.read_csv("avocado.csv")
df.head(100).to_excel("avocado_sample.xlsx", index=False)
df_xlsx = pd.read_excel("avocado_sample.xlsx", engine="openpyxl")
print(df_csv.head())
print(df_xlsx.head())

#5 Transposing data frame
print("\nTransposed data frame from the dictionary")
print(df_dictionary.T)

#6 Display the first 10 rows
print("\nFirst 10 rows")
print(df.head(10))

#7 Display last 10 rows
print("\nLast 10 rows")
print(df.tail(10))

#8 Display info about data frame
print("\n Data frame info")
df.info()

#9 Display the number of rows and columns
print("\nShape (rows, columns):", df.shape)

#10 Display statistics of numeric columns
print("\nNumeric columns statistics")
print(df.describe())


#11 Display statistics of categorical columns
print("\nCategorical columns statistics")
print(df.describe(exclude="number"))

#12 Remove missing values
