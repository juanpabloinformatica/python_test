import pandas as pd
import os


def get_columns_array(data_frame):
    print(data_frame)
    column_arrays = []
    for column_index in range(2, len(data_frame.columns)):
        column_array = data_frame.iloc[:, column_index].values
        column_arrays.append(column_array)
    return column_arrays


def save_image(folder_path, task_name, plt):
    os.makedirs(folder_path, exist_ok=True)
    plt.savefig(folder_path + task_name)


def move_colors(general_colors, positions):
    for i in range(0, positions):
        first = general_colors[0]
        for j in range(0, len(general_colors) - 1):
            general_colors[j] = general_colors[j + 1]
        general_colors[len(general_colors) - 1] = first


def list_colors(general_colors, ball_colors):
    general_colors_static = ["yellow", "green", "royalblue", "violet", "red", "orange"]
    dictionary = {}
    for t in range(0, len(general_colors_static)):
        dictionary[general_colors_static[t]] = general_colors[t]
    for t in range(0, len(ball_colors)):
        ball_colors[t] = dictionary.get(ball_colors[t])
