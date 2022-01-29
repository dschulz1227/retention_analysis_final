# import logo from art
import pandas as pd
from numpy import sum

"""
    Engineer a program that can analyze the data between each of the 3 shifts' camera checks in order to compare
    the data against each other.
    Find discrepancies and potential patterns that reflect the health of our network.
    Make predictions using data
"""

# print(logo)

# my_csv_file = input("What's the name of the file located in the Retention Forms folder?")
# my_csv_file = 'C:\\Retention Forms\\' + my_csv_file
# my_csv_file = "C:\\Retention Forms\\ret_prac_csv.csv"
"""
--> URL ABOVE IS FOR AT WORK
--> Make my_csv_file accept user input to enter the path to the CSV File
"""

my_csv_file = "../retention_analysis_final/ret_prac_csv.csv"
df = pd.read_csv(my_csv_file, index_col=[0])
df = df.reset_index(drop=False)
# print(df)df

# check_date = input("Date (ex January_1): ")
mean_list = []
results_dict = {}


# new_file = input("WRITE THE DAY OF THE MONTH")

# out_file = open(f"/Users/blckout/PycharmProjects/retention_analysis_final/results_folder/{new_file}", "w")


def find_difference(colName):
    """Use this to compare the values within each column to find differences within the data"""
    a = df.loc[0, colName]
    b = df.loc[1, colName]
    c = df.loc[2, colName]

    sum_values = a + b + c
    # # create new variables to represent pieces of equation
    """
    --> Equation that finds Percentage of the difference between two values
    --> abs()converts negative number to positive number
    --> Round to nearest whole number
    --> 
    """
    # difference_list_ab = []
    # difference_list_ac = []
    # difference_list_bc = []
    diff_ab = round((abs(a - b)) / ((a + b) / 2) * 100)
    diff_ac = round((abs(a - c)) / ((a + c) / 2) * 100)
    diff_bc = round((abs(b - c)) / ((b + c) / 2) * 100)
    print(f"Diff AB : {diff_ab}, Diff AC : {diff_ac}, Diff BC : {diff_bc}")
    # difference_list_ab.append(diff_ab)
    # difference_list_ac.append(diff_ac)
    # difference_list_bc.append(diff_bc)
    if diff_ab > 25:
        print(f"Diff AB = {diff_ab} - greater than 25")
    else:
        print(f"AB = {diff_ab} is All Good")
    if diff_ac > 25:
        print(f"Diff AC = {diff_ac} greater than 25")
    else:
        print(f"AC = {diff_ac} is All Good")
    if diff_bc > 25:
        print(f"Diff BC = {diff_bc} is greater than 25")
    else:
        print(f"BC = {diff_bc} is All Good")
    # print(a, b, c)
    daily_average = sum_values / 3
    mean_list.append(round(daily_average))
    # print(f"{colName} : Total = {sum_values}, Average = {round(retention_avg)}")
    # out_file.write(f"{colName} : Total = {sum_values}, Average = {round(retention_avg)}\n")
    return daily_average


server_cols = [x for x in df.columns if x.startswith('IV-') or x.startswith('NSM-')]
# print(server_cols)

for colName in server_cols:
    find_difference(colName)
    retention_avg = find_difference(colName)
    results_dict[colName] = float(round(retention_avg))
# out_file.close()

# print(f"Server Averages: {mean_list}")

# print(f"Results: {results_dict}")
