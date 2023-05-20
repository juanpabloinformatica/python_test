from stageLights import *

# import sys

# sys.path.append("./utils")
from utils.helperFunctions import get_columns_array


def task1(ax):
    ax.set_facecolor("black")
    step = 100
    init_x = 50
    for i in range(0, 10):
        init_y = 50
        for j in range(0, 10):
            light = Light((init_x, init_y), "red")
            light.plotLight(ax)
            init_y += step
        init_x += step
    plt.title("Red Lights - 10*10", fontsize="18")
    savePath = "./images/task1.png"
    plt.savefig(savePath)
    return ax


def task2(ax, data_frame):
    ax.set_facecolor("black")
    x_values, y_values, ball_colors = get_columns_array(data_frame)
    print(len(y_values) == len(ball_colors))
    print(ball_colors)
    light = Light((50, 50), "red")
    light.plotLight(ax)
    for i in range(0, len(x_values)):
        light = Light((x_values[i], y_values[i]), ball_colors[i])
        light.plotLight(ax)
    plt.title("Coloured Lights - From File", fontsize="18")
    savePath = "./images/task2.png"
    plt.savefig(savePath)
    return ax


def task3(ax, data_frame):
    ax.set_facecolor("black")
    x_values, y_values, ball_colors = get_columns_array(data_frame)
    general_colors = ["yellow", "green", "blue", "pink", "red", "orange"]
    # light = Light((x_values[0], y_values[0]), ball_colors[0])
    # light.plotLight(ax)
    # light = Light((x_values[1], y_values[1]), ball_colors[1])
    # light.plotLight(ax)
    # light = Light((x_values[2], y_values[2]), ball_colors[2])
    for t in range(0, 10):
        light = Light((x_values[t], y_values[t]), ball_colors[t])
        light.plotLight(ax)
    # light.plotLight(ax)
    # print(ball_colors)

    # for t in range(0,5):
    # for i in range(0,len(x_values)):

    # for i in range(0, len(x_values)):

    # light = Light((x_value"s[i], y_values[i]), ball_colors[i])
    # light.plotLight(ax)

    subIndex = 1
    plt.title(f"Moving Coloured lights i:{subIndex}", fontsize="18")
    index = 1
    savePath = f"./images/task3/task3_{index}.png"
    plt.savefig(savePath)
    print("task3")
    pass


def task4():
    print("task4")
    pass
