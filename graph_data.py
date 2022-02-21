from matplotlib import pyplot as plt
# import pandas as pd
# import pprint
from get_data import results

dict_keys = []
dict_values = []
"""Print dictionary key-value pairs on each line"""
for k, v in results.items():
    """DICT KEYS ARE SERVER NAMES"""
    dict_keys.append(k)
    """DICT VALUES ARE Total, average, % differences"""
    dict_values.append(v)
    # print(k, '-->', v)

"""EACH DICT_KEY NEEDS A LIST OF 3 VALUES"""
# print(dict_keys)
value_names = []
values = []
largest_dif = 0

for k, v in dict_values[0].items():
    """If v(value) datatype == tuple, make largest_dif == to the largest of 3 numbers in tuple"""
    """Add that value to list of values, making only list of integers"""
    if isinstance(v, tuple):
        largest_dif = max(v)
        values.append(largest_dif)
    else:
        """if type != tuple, add value to values list"""
        values.append(v)
    """always append k to keys"""
    value_names.append(k)
    print(k, v)

"""Values is the list of 3 calculated values from 1 whole day(3 forms)"""
print(values[0])


""" give each key a variable to use in plots """
# key_total = keys[0]
# key_average = keys[1]
# key_differences = keys[2]
# """ give each value a variable to use in plots """
# total = values[0]
# average = values[1]
# differences = values[2]


# print(total)
# print(average)
# print(differences)
# print(differences[0], differences[1], differences[2])

# print(k)
# def plot_values():
#     for k, v in results.items():
#         dict_keys.append(k)
#         dict_values.append(v)
#         print(k, '-->', v)
#
#
# plot_values()
