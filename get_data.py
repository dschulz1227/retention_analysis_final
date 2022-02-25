# import logo from art
import pandas as pd
import pprint

""" Code below is to accept user input as the path to the CSV file """
# my_csv_file = input("What's the name of the file located in the Retention Forms folder?")

"""creates new file to write content too"""
# out_file = open("/Users/blckout/PycharmProjects/retention_analysis_final/results_folder/new.csv", "w")
out_file = open("results\\results.txt", "w")


""" Below is hardcoded path to CSV and creates a dataframe from the columns and row """
""" First line is path at work, second is path at home"""
my_csv_file = "ret_prac_csv.csv"
# my_csv_file = "/Users/blckout/PycharmProjects/retention_analysis_final/ret_prac_csv.csv"

"""create dataframe from csv file info"""
df = pd.read_csv(my_csv_file, index_col=[0])
df = df.reset_index(drop=False)

"""enables to print all columns of dataframe"""
# pd.set_option('display.max_columns', None)

"""Below are logic functions to find more data"""
all_avgs = []

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
    all_avgs.append(daily_average)
    return daily_average


differences_dict = {}


def find_difference(colName):
    """Use this to compare the values within each column to find differences within the data"""
    a = df.loc[0, colName]
    b = df.loc[1, colName]
    c = df.loc[2, colName]

    """abs()converts negative number to positive number"""
    diff_ab = round((abs(a - b)) / ((a + b) / 2) * 100)
    diff_ac = round((abs(a - c)) / ((a + c) / 2) * 100)
    diff_bc = round((abs(b - c)) / ((b + c) / 2) * 100)

    differences_dict[colName] = diff_ab, diff_ac, diff_bc

    if diff_ab > 25 or diff_bc > 25 or diff_ac > 25:
        print(f"{colName} has large differences.")


"""List of results as dictionary"""
total_dict = {}
averages_dict = {}
results = {}

server_cols = [x for x in df.columns if x.startswith('IV-') or x.startswith('NSM-')]

for colName in server_cols:
    """Below creates a dictionary of each rows calculated values"""
    results[colName] = {"Total: ": find_total(colName),
                        "Average:": find_avg(colName),
                        "% Differences:": find_difference(colName)}

    """Below adds each calculation to it's own, separate dictionary"""
    total_dict[colName] = find_total(colName)
    averages_dict[colName] = find_avg(colName)


"""Print Results to outfile"""

pprint.pprint(f"Totals: \n {total_dict}", out_file)
pprint.pprint(f"Averages: \n {averages_dict}", out_file)
pprint.pprint(f"Differences: \n {differences_dict}", out_file)
print(all_avgs)
out_file.close()
