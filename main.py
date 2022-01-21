"""
    Engineer a program that can analyze the data between each of the 3 shifts' camera checks in order to compare
    the data against each other.
    Find discrepancies and potential patterns that reflect the health of our network.
    Make predictions using data
"""

# import logo from art
import pandas as pd
# import os

# print(logo)
my_csv_file = "C:\\Retention Forms\\ret_prac_csv.csv"
df = pd.read_csv(my_csv_file)
# df_t = df.T
# print(df.to_string()
# print(df)

#
# for index, row in df.iterrows():
#     key = row[0]
#     name = row[1]

for col in df.columns:
    values = list(df[col])
    print(values)



