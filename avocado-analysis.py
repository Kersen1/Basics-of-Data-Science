#Load libraries for the project
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
