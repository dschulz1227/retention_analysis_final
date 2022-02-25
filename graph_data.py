import seaborn as sns
import matplotlib.pyplot as plt
from get_data import differences_dict, total_dict, averages_dict, all_avgs



def graph_highest_differences():
    value_names = []
    diff_values = []

    """ Get highest % difference from each server"""
    for k, v in differences_dict.items():
        """If v(value) datatype == tuple, make largest_dif == to the largest of 3 numbers in tuple"""
        """Add that value to list of values, making only list of integers"""
        if isinstance(v, tuple):
            largest_dif = max(v)
            diff_values.append(largest_dif)
            print(f"{k}: {largest_dif}")
        else:
            """if type != tuple, add value to values list"""
            diff_values.append(v)
        """always append k to keys"""
        value_names.append(k)
        # print(k, v)

    x = value_names
    y = diff_values

    diff_bar = sns.barplot(x, y)
    diff_bar.set_xlabel("Server")
    diff_bar.set_ylabel("Percentage")
    diff_bar.set(title="3 Day Highest % Differences")

    plt.show()


def graph_total():
    all_totals = []
    value_names =[]
    for k, v in total_dict.items():
        all_totals.append(v)
        value_names.append(k)

    x = value_names
    y = all_totals

    total_bar = sns.barplot(x, y)
    total_bar.set_xlabel("Server")
    total_bar.set_ylabel("Total Days")
    total_bar.set(title="Three Day Total")

    plt.show()


def graph_averages():
    all_averages = []
    value_names =[]
    for k, v in averages_dict.items():
        all_averages.append(v)
        value_names.append(k)

    x = value_names
    y = all_averages

    avg_bar = sns.barplot(x, y)
    avg_bar.set_xlabel("Server")
    avg_bar.set_ylabel("Average Days")
    avg_bar.set(title="Three Day Average")

    plt.show()

