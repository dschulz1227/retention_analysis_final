# import logo from art
import pandas as pd


"""
    Engineer a program that can analyze the data between each of the 3 shifts' camera checks in order to compare
    the data against each other.
    Find discrepancies and potential patterns that reflect the health of our network.
    Make predictions using data
"""

# print(logo)

# my_csv_file = input("What's the name of the file located in the Retention Forms folder?")
# my_csv_file = 'C:\\Retention Forms\\' + my_csv_file
my_csv_file = "C:\\Retention Forms\\ret_prac_csv.csv"
df = pd.read_csv(my_csv_file, index_col=[0])
df = df.reset_index(drop=False)
# print(df)df


mean_list = []
january_1 = {}


def find_difference(colName):
    """Use this to compare the values within each column to find differences within the data"""
    a = df.loc[0, colName]
    b = df.loc[1, colName]
    c = df.loc[2, colName]

    sum_values = a + b + c
    mean_value = sum_values / 3
    mean_list.append(round(mean_value))
    print(f"{colName} : Total = {sum_values}, Average = {round(mean_value)}")
    return mean_value


server_cols = [x for x in df.columns if x.startswith('IV-') or x.startswith('NSM-')]
# print(server_cols)

for colName in server_cols:
    find_difference(colName)
    mean_value = find_difference(colName)
    january_1[colName] = float(round(mean_value))
# print(f"Server Averages: {mean_list}")
print(f"January 1st: {january_1}")


