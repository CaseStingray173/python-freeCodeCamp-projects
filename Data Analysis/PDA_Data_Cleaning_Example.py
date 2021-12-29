import numpy as np
import pandas as pd

###############################################################
# # Creating a sample dataFrame
# samp_df = pd.DataFrame({
#     "Sex": ["M", "F", "D", "?"],
#     "Age": [22, 20, 21, 190]
# })
#
# # unique() prints the unique entries in a column of a dataFrame
# print("All the unique entries in Sex column: ", samp_df["Sex"].unique())
#
# # Counts the occurrences of all the entries in a column of the dataFrame
# print("\nCounts of occurrences of all sexes: ")
# print(samp_df["Sex"].value_counts())

# # Replace the entries of "D" with "F"
# temp1 = samp_df["Sex"].replace("D", "M")
#
# # Replaces the entries of a column in a dataFrame using dictionary
# temp2 = samp_df["Sex"].replace({"D": "M", "?": "F"})
#
# # If you have many columns to replace, we can replace entries at "dataFrame" level
# temp3 = samp_df.replace({
#     "Sex": {
#         "D": "M",
#         "?": "F"
#     },
#     "Age": {
#         190: 19
#     }
# })
#
# print(temp1)
# print(temp2)
# print(temp3)
###############################################################

###############################################################
# ambassadors = pd.Series([
#     "France",
#     "United Kingdom",
#     "United Kingdom",
#     "Italy",
#     "Germany",
#     "Germany",
#     "Germany",
# ], index=[
#     "Gerard Araud",
#     "Kim Darroch",
#     "Peter Westmacott",
#     "Armando Varricchio",
#     "Peter Wittig",
#     "Peter Ammon",
#     "Klaus Scharioth"
# ])

# # Looks at the first value(First value is False) and considers it as "not a duplicate",
# # but if the same value is repeated again its considered as duplicate
# print(ambassadors.duplicated(), "\n")

# # This works similar to default duplicated() but instead of considering the first occurrences
# # of a value as "not a duplicate", it considers the last value of some repeated value
# # as "not a duplicate"
# print(ambassadors.duplicated(keep="last"), "\n")

# # All the duplicate values are marked "True" no matter if it appears first or last
# print(ambassadors.duplicated(keep=False), "\n")

# # Default drop_duplicates(): keeps the first occurrence of the value and
# # throws the other duplicate entries
# temp1 = ambassadors.drop_duplicates()

# # Dropping duplicates this way ensures that you keep the last occurrence of the
# # value and throw the previous duplicates
# temp2 = ambassadors.drop_duplicates(keep="last")

# # This throws all the duplicates away and only keeps the values that are unique
# temp3 = ambassadors.drop_duplicates(keep=False)
#
# print(temp1, "\n")
# print(temp2, "\n")
# print(temp3, "\n")

###############################################################

###############################################################
# players = pd.DataFrame({
#     "Name": [
#         "Kobe Bryant",
#         "China Ka Pilla",
#         "Kobe Bryant",
#         "Carmelo Anthony",
#         "Kobe Bryant"
#     ],
#     "Pos": [
#         "SG",
#         "SF",
#         "SG",
#         "SF",
#         "SF"
#     ]
# })

# # If both Name and Pos are in a row and the same entries appear again in another row
# # its considered as a duplicate
# print(players.duplicated())

# # Only looking at the name column for duplicated
# print(players.duplicated(subset=["Name"]))
###############################################################


###############################################################
# SPLITTING COLUMNS
sam_df = pd.DataFrame({
    "Data": [
        "1987_M_US _1",
        "1990?_M_UK_1",
        "1992_F_US_2",
        "1970?_M_    IT_1",
        "1985_F_I   T_2"
    ]
})

# # Splits strings by removing the "_" and
# temp1 = sam_df["Data"].str.split("_")
# print(temp1)

# Splits the string and puts it in separate columns
temp2 = sam_df["Data"].str.split("_", expand=True)
# # Setting the column names after split
temp2.columns = ["Year", "Sex", "Country", "No Children"]
# print(temp2)
# # If for a row any column contains the specified string its set to True
# print(temp2["Year"].str.contains("\?"))

temp2["Country"].str.strip()
temp2_1 = temp2["Country"].str.replace(" ", "")
temp2_2 = temp2["Year"].str.replace(r"(?P<year>\d{4})\?", lambda m: m.group("year"))
print(temp2_1)
print(temp2_2)

