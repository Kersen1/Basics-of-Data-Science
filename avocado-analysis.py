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
df.to_excel("avocado_sample.xlsx", index=False)
df_xlsx = pd.read_excel("avocado_sample.xlsx", engine="openpyxl")
print("\nLoad saved data csv:")
print(df_csv)
print("\nLoad saved data xls:")
print(df_xlsx)
#We use index=False so that pandas won't create a separate column with indexes.
#To open xlsx files in IDE's we need to install a special XLS loader.

#5 Transposing data frame
print("\nTransposed data frame from the dictionary")
print(df_dictionary.T)
print("\nOriginal data frame from the dictionary")
print(df_dictionary)

#We flip the data, columns and rows change place.
#The flip happens following the main diagonal.

#6 Display the first 10 rows
print("\nFirst 10 rows")
print(df.head(10))

#Computer show me 10 first positions of my dataset!

#7 Display last 10 rows
print("\nLast 10 rows")
print(df.tail(10))
#Computer show me last 10 positions of my dataset!

#8 Display info about data frame
print("\n Data frame info")
df.info()

#This one is useful!
#Here we can access information about our data.
#From showing us all of the unique columns and their types to telling us the amount of entries of our data frame.
#At the end is a summary of types and their (#) number of how many of this specific type there is.
#And of course the memory usage of the data frame...

#9 Display the number of rows and columns
print("\nShape (rows, columns):", df.shape)

#Computer tell me the shape of the data!

#10 Display statistics of numeric columns
print("\nNumeric columns statistics")
print(df.describe())

#We can display numerical values by just calling .describe().
#It's the default


#11 Display statistics of categorical columns
print("\nCategorical columns statistics")
print(df.describe(exclude="number"))

#Here we exclude the numbers to get the statistics of non numbery types.
#Trying to use include=["category"] would only get us error.
#That is because we have string as a data type for the non numerical columns.

#12 Remove missing values
print("\nChecking if we are missing any value")
print(df.isna().sum())

#Here we check if something is missing and there is no missing values.
#isna() checks if there is an empty space in each frame and sums up all of the missing spaces in each column.
#We will need to create some.

df_missing = df.copy()
df_missing.loc[[2,4,6], "AveragePrice"] = np.nan
df_missing.loc[[3,5], "Total Volume"] = np.nan
print("\n Missing values before removal")
print(df_missing.isna().sum()[["AveragePrice","Total Volume"]])
df_missing = df_missing.dropna()
print("\n Rows before and after dropna:", len(df), "->", len(df_missing))

#We copy the dataframe to allocate some values to it which will be not a number.
#Then we check if there are really missing values and yes because we created 5 of them there is 5 of them.
#We count them up in each column and remove them.
#After that we show that 5 values really disappeared



#13 Select rows and columns by names and indexes

print("\nOne column (Series)")
print(df["AveragePrice"].head())
print("\nFew columns")
print(df[["Date", "AveragePrice","Total Volume"]].head())
print("\nBy labels and location")
print(df.loc[0:4, ["Date", "AveragePrice"]])
print("\nBy positions")
print(df.iloc[0:5, 1:5])
print("\nThree rows")
print(df.iloc[0:2])
print("\nSingle cell")
print(df.loc[2, "region"])

#Different methods of showing our data.
#Being able to search by location is pretty neat.
#If we pass 2 arguments to iloc the first one tells us which rows to take and the second takes the columns number as the argument
#If we pass a single value to it. It shows us the row we chose.


#14 Select rows by a condition on one column
print("\nRows with AveragePrice > 2")
print(df[df["AveragePrice"] > 2].head())

#Here we are getting the first 5 values greater than 2.
#We first find all values greater than 2, and then we print the first 5.

#15 Select rows by several conditions at once
print("\nOrganic avocados in 2017")
print(df[(df["type"] == "organic") & (df["year"] == 2017)].head())

#Computer print for me first 5 avocados which are organic and from year 2017.

#16 Select rows containing a given word in a categorical column
print("\nRegions containing 'New'")
print(df[df["region"].str.contains("New", na=False)].head())

#Computer print for me rows with string type saying New something... Ommit empty spaces and give me 5 of these.

#17 Select rows not containing a given word in a categorical column
print("\nRegions not containing 'New'")
print(df[~df["region"].str.contains("New", na=False)].head())

#Computer print me 5 values that DO NOT contain New something... with type string.

#18 Create a new column based on existing ones
df["BagsShare"] = df["Total Bags"] / df["Total Volume"]
print("\nNew column BagsShare")
print(df[["Total Bags", "Total Volume", "BagsShare"]].head())

#We can check different things.
#For example we can create a column representing a stat telling us what part of volume is in each bag.

#19 Delete a column
df = df.drop(columns=["Unnamed: 0"])
print("\nColumns after deleting Unnamed: 0")
print(df.columns.tolist())

#We don't really need the indexing column.


#20 Rename a column
df = df.rename(columns={"4046": "PLU_4046","4225": "PLU_4225","4770": "PLU_4770"})
print("\nColumns after renaming")
print(df.columns.tolist())

#There are different norms for avocados. In the base CSV we got it only said numbers.
#For someone not knowing what we are talking about it's better to rename them to something more clear.

#21 Save the data frame as a CSV file
df.to_csv("avocado_result.csv", index=False)
print("\nSaved avocado_result.csv")

#We save the data frame to a csv file without adding index column.

#22 Display mean (and max, min) of a chosen column
print("\nAveragePrice mean:", df["AveragePrice"].mean())
print("AveragePrice max:", df["AveragePrice"].max())
print("AveragePrice min:", df["AveragePrice"].min())
