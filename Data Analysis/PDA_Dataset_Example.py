import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

sales = pd.read_csv("sales_data.csv", parse_dates=["Date"])

# Prints the first five entries in the CSV
# print(sales.head())

# Prints the row and column numbers
# print(sales.shape)

# Prints the data types of the columns used to store the data
# print(sales.info())

# Using "pd.option_context" you can display all the columns by specifying the number of the columns
# with pd.option_context('display.max_columns', 17):
    # Print the important statistical data
    # print(sales.describe())

# Prints the important statistical data for the specified column
# print(sales["Unit_Cost"].describe())

# Prints the mean for the specified column
# print(sales["Unit_Cost"].mean())

# Prints the median for the specified column
# print(sales["Unit_Cost"].median())

# Plots the graph for specified column
# print(sales["Unit_Cost"].plot(kind="box", vert=False, figsize=(14, 6)))
# Displays the actual graph
# plt.show()

# Plots the graph as continuous line representing the values in the columns
# print(sales["Unit_Cost"].plot(kind="density", figsize=(14, 6)))
# Prints the mean of the specified column on the plot created previously
# print(plt.axvline(sales["Unit_Cost"].mean(), color="red"))
# Prints the median of the specified column on the plot created previously
# print(plt.axvline(sales["Unit_Cost"].median(), color="green"))
# Displays the plotted graph
# plt.show()

# Plots ths graph as histogram
# ax = sales["Unit_Cost"].plot(kind="hist", figsize=(14, 6))
# print(ax)
# Sets the label for y_axis of the plot
# print(ax.set_ylabel("Number of sales"))
# Sets the label for x_axis of the plot
# print(ax.set_xlabel("dollars"))
# plt.show()

# Prints how many times a value in a group appears
# Age_Group has categories/groups such as Youth(<25) and Adults(35-64)
# print(sales["Age_Group"].value_counts())

# Plots the value_counts() of a specified column as a pie chart
# ax = sales["Age_Group"].value_counts().plot(kind="pie", figsize=(7, 7))
# print(ax)
# plt.show()

# Plots the value_counts() of a specified column as a bar chart
# ax = sales["Age_Group"].value_counts().plot(kind="bar", figsize=(14, 6))
# print(ax.set_ylabel("Number of Sales"))
# plt.show()

# Gives the correlations between columns
# corr = sales.corr()
# print(corr)

# Plots the correlation as a square, using color shades
# fig = plt.figure(figsize=(8, 8))
# plt.matshow(corr, cmap="RdBu", fignum=fig.number)
# plt.xticks(range(len(corr.columns)), corr.columns, rotation="vertical")
# plt.yticks(range(len(corr.columns)), corr.columns)
# plt.show()

# Make a columns based on calculating other columns
# sales["Revenue_per_age"] = sales["Revenue"] / sales["Customer_Age"]
# print(sales["Revenue_per_age"].head())

# This gives us the sales made in Kentucky
# print(sales.loc[sales["State"] == "Kentucky"])
# This gives the mean revenue of the Adults(35-64) sales group
# print(sales.loc[sales["Age_Group"] == "Adults (35-64)", "Revenue"].mean())



