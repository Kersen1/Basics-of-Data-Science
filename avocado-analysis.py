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

#2 Create dictionary data structure
dictionary = {
    "type": ["conventional", "organic", "organic"],
    "region": ["Albany", "Boston", "Chicago"],
    "AveragePrice": [1.33, 1.85, 1.62],
}
df_dictionary = pd.DataFrame(dictionary)
print("\nExample of the dictionary from the project")
print(df_dictionary)


