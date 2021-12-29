import numpy as np
import pandas as pd

# np.nn = None

####################SERIES MANIPULATION#########################
##############################################
# # This is how you create a series
# sample_series = pd.Series([1, 2, np.nan])
# # Prints True if any values in the series are null
# print(pd.isnull(sample_series))
##############################################


#############################################
# # Counts the non null values in a series
# print("Number of non null values: ", pd.Series([1, 2, np.nan]).count())
# # Sums the all non null values in a series
# print("Sum of non null values: ", pd.Series([1, 2, 4]).sum())
# # Gives the mean of non null values in a series
# print("Mean of non null values: ", pd.Series([1, 2, 3]).mean(), "\n")
#############################################


#############################################
# samp_df = pd.Series([1, 2, 3, None, None, 4])
# print(pd.notnull(samp_df))
# print("Total count of non null values: ", pd.notnull(samp_df).sum(), "\n")
# print("The output below and above this line are the same but method is slight different\n")
# print(samp_df.notnull())
# print("Total count of non null values: ", samp_df.notnull().sum(), "\n")
#
# # Stores the non null values in the same series temporarily and prints it
# print(samp_df[pd.notnull(samp_df)], "\n")
# print("The output below and above this line are the same but method is slight different\n")
# print(samp_df[samp_df.notnull()], "\n")
#############################################


#############################################
# Drops the null values out of a series
# This print also does the same as the previous two prints
# print(samp_df.dropna())
#############################################
####################SERIES MANIPULATION#########################


####################DFRAME MANIPULATION#########################
##############################################
# # This is how you create manual dataframe
# sample_dataframe = pd.DataFrame({"Column A": [1, np.nan, 7], "Column B": [np.nan, 2, 3],
#                                  "Column C": [np.nan, 2, np.nan]})
# # Prints True if any values in the dataframe are null
# # Prints True and False as a table
# print(pd.isnull(sample_dataframe), "\n")
#############################################


#############################################
# samp_df = pd.DataFrame({
#     "Column A": [1, None, 30, None],
#     "Column B": [2, 8, 31, None],
#     "Column C": [None, 9, 32, 100],
#     "Column D": [5, 8, 34, 110]
# })
#
# # Prints the sizes of rows and columns
# print("Sizes of rows and columns: ", samp_df.shape)
#
# print(samp_df.info())
# print(samp_df.isnull())
# print(samp_df.isnull().sum())
#
# # Drops the columns that have None as an entry
# print(samp_df.dropna())
#
# print(samp_df.dropna(axis=1))
#
# # Does not drop any None values and displays the table as it is
# print(samp_df.dropna(how="all"))
#
# # This drops the row if it has less than the specified amount of not None values
# print(samp_df.dropna(thresh=3))
# print(samp_df.dropna(thresh=3, axis="columns"))
#############################################
####################DFRAME MANIPULATION#########################


####################FILLING NULL VALUES#########################
# Creating a sample series
# samp_series = pd.Series([1, None, 3, None, 5, None])
# print("The original series: ")
# print(samp_series)

# Filling the None/null values in the series with 0 or can be any number
# temp1 = samp_series.fillna(0)
# print("\nReplacing None in series with 0s: ")
# print(temp1)

# Filling the None values with the mean of all non-none values in the series
# print("The mean of all non-none values in the series: ", samp_series.mean())
# temp2 = samp_series.fillna(samp_series.mean())
# print("Replacing None values in series with mean of series: ")
# print(temp2)

# Fills the None values with the values above it in the series
# NOTE: This method cant replace the None value which is on the top of a series
# since it does not have any values above it
# temp1 = samp_series.fillna(method="ffill")
# print(temp1)

# Fills the None values with the values below it in the series
# NOTE: This method cant replace the None value in the bottom of the series
# since it does not have any values below it
# temp2 = samp_series.fillna(method="bfill")
# print(temp2)

samp_dataframe = pd.DataFrame({"Column A": [1, None, 7, None],
                               "Column B": [None, 12, 13, None],
                               "Column C": [10, 2, 30, 100],
                               "Column D": [None, 25, 50, None]})

print("The original dataframe: ")
print(samp_dataframe)

temp1 = samp_dataframe.fillna(method="ffill", axis=0)
temp2 = samp_dataframe.fillna(method="bfill", axis=1)
print(temp1)
print(temp2)
temp3 = samp_dataframe.fillna({"Column A": 0, "Column B": 99, "Column D": samp_dataframe["Column D"].mean()})
print(temp3)
####################FILLING NULL VALUES#########################
