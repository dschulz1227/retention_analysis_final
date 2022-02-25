import seaborn as sns
import matplotlib.pyplot as plt
from get_data import differences_dict, total_dict, averages_dict


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
    diff_bar.set_xlabel("Servers")
    diff_bar.set_ylabel("Percentage")

    plt.show()


def graph_total():
    all_totals = []
    value_names =[]
    for k, v in total_dict.items():
        """If v(value) datatype == tuple, make largest_dif == to the largest of 3 numbers in tuple"""
        """Add that value to list of values, making only list of integers"""
        all_totals.append(v)
        """always append k to keys"""
        value_names.append(k)
        # print(k, v)

    x = value_names
    y = all_totals

    diff_bar = sns.barplot(x, y)
    diff_bar.set_xlabel("Sersver")
    diff_bar.set_ylabel("Total Days")

    plt.show()


def graph_averages():
    all_averages = []
    value_names =[]
    for k, v in averages_dict.items():
        """If v(value) datatype == tuple, make largest_dif == to the largest of 3 numbers in tuple"""
        """Add that value to list of values, making only list of integers"""
        all_averages.append(v)
        """always append k to keys"""
        value_names.append(k)
        # print(k, v)

    x = value_names
    y = all_averages

    diff_bar = sns.barplot(x, y)
    diff_bar.set_xlabel("Server")
    diff_bar.set_ylabel("Average Days")

    plt.show()

