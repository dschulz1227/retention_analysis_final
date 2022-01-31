# import logo from art
import pandas as pd

"""
Engineer a program that can analyze the data between each of the 3 shifts' camera checks in order to compare
the data against each other.
Find discrepancies and potential patterns that reflect the health of our network.
Make predictions using data
"""

""" Code below is to accept user input as the path to the CSV file """
# my_csv_file = input("What's the name of the file located in the Retention Forms folder?")
# my_csv_file = 'C:\\Retention Forms\\' + my_csv_file
# my_csv_file = "C:\\Retention Forms\\ret_prac_csv.csv"


"""
Must find way to easily access CSV file
Must find way to save each file generated by running program to a common folder
Possibly save dictionary of daily results to it's own file
Find most efficient way to analyze data for any circumstances(daily, monthly, yearly, etc)
"""

""" Below is hardcoded path to CSV and creates a dataframe from the columns and row """
my_csv_file = "C:\\Retention Forms\\ret_prac_csv.csv"
df = pd.read_csv(my_csv_file, index_col=[0])
df = df.reset_index(drop=False)

"""List of all averages"""
mean_list = []
"""List of results as dictionary"""
total_dict = {}
differences_dict = {}
averages_dict = {}
# results_dict = {}

"""Create variable for file to write data to"""
out_file = open("C:\\Retention Forms\\results_folder\\january", "w")


def find_total(colName):
    a = df.loc[0, colName]
    b = df.loc[1, colName]
    c = df.loc[2, colName]
    row_total = a + b + c

    return row_total


def find_avg(colName):
    a = df.loc[0, colName]
    b = df.loc[1, colName]
    c = df.loc[2, colName]
    daily_average = round((a + b + c) / 3)
    return daily_average


def find_difference(colName):
    """Use this to compare the values within each column to find differences within the data"""
    a = df.loc[0, colName]
    b = df.loc[1, colName]
    c = df.loc[2, colName]
    """
    Equation that finds Percentage of the difference between two values
    abs()converts negative number to positive number
    """
    diff_ab = round((abs(a - b)) / ((a + b) / 2) * 100)
    diff_ac = round((abs(a - c)) / ((a + c) / 2) * 100)
    diff_bc = round((abs(b - c)) / ((b + c) / 2) * 100)

    return diff_ab, diff_ac, diff_bc


server_cols = [x for x in df.columns if x.startswith('IV-') or x.startswith('NSM-')]

for colName in server_cols:
    # out_file.write(f"\n{find_difference(colName)}")
    # print(colName, percent_differences)
    total_dict[colName] = find_total(colName)
    averages_dict[colName] = find_avg(colName)
    differences_dict[colName] = find_difference(colName)
    # results_dict[colName] = find_difference(colName), find_avg(colName), find_total(colName)

print(f"\nTotals: {total_dict}\nAverages: {averages_dict}\n% Differences: {differences_dict}")

# out_file.close()

