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
df.info()

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

