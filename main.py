from get_data import find_avg, find_total, find_difference
from graph_data import graph_total, graph_averages, graph_highest_differences
from art import logo

print(logo)

guide = "Function 1: Graph Averages\nFunction 2: Graph Totals\nFunction 3: Graph Highest Differences."
print(guide)
yes_or_no = input("Would you like to analyze data today?").lower()

if input("What function would you like to run?") == 1:
    graph_averages()
elif input("What function would you like to run?") == 2:
    graph_total()
elif input("What function would you like to run?") == 3:
    graph_highest_differences()


