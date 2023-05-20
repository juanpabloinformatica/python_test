import pandas as pd


def get_columns_array(data_frame):
    print(data_frame)
    column_arrays = []
    for column_index in range(2, len(data_frame.columns)):
        column_array = data_frame.iloc[:, column_index].values
        column_arrays.append(column_array)
    return column_arrays
