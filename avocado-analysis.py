#1 Load libraries for the project
import kagglehub
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#Some libraries we will be using in this project.
#We use "as pd,np,plt" to not get stiff hands.
#It's just a common practice actually.

path = kagglehub.dataset_download("neuromusic/avocado-prices")
print("Path to dataset files:", path)
df = pd.read_csv(os.path.join(path, "avocado.csv"))
print(df.head())
#Shoutout to the database creator.
#It would take me years to count all of these avocados.
#Here we use API to access the database. You will need to create your own API key on kaggle or just download the database.
#Anyway, after connecting and downloading the database using kagglehub functions we check where out computer has the saving space set as.
#After checking for the place.
# We use pandas.read_csv and join the path to avocado.csv because pd.read_cvs needs to connect to the appropriate csv file and we know the path because we printed it earlier.


#2 Create dictionary data structure and data frame
dictionary = {
    "type": ["conventional", "organic", "organic"],
    "region": ["Albany", "Boston", "Chicago"],
    "AveragePrice": [1.33, 1.85, 1.62],
}
df_dictionary = pd.DataFrame(dictionary)
print("\nExample of the Data Frame from the dictionary")
print(df_dictionary)

#Did you know that dictionaries are ordered since Python 3.7? Cool...
#Dictionaries are really cool because they allow us to get a shortcut into finding keys to known values.
# For example If we want to know what type our avocados are we will access this information using dictionary["type"].
#Using that method here would give us an array containing three items.

#3 Create Data frame from list of lists

list_ex = [
    ["conventional", "Albany", 1.33],
    ["organic", "Boston", 1.85],
    ["organic", "Chicago", 1.62],
]
df_list = pd.DataFrame(list_ex, columns=["type", "region", "AveragePrice"])
print("\nExample of the Data Frame from the list of lists")
print(df_list)
#Here we create a matrix 3x3 and then create a readable DataFrame choosing the names for columns
#It works because we have three column names.

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
