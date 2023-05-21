from stageLights import *
from utils.helperFunctions import (
    get_columns_array,
    list_colors,
    move_colors,
    save_image,
)


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
    folder_path = "./src/images/"
    task_name = "task1.png"
    save_image(folder_path, task_name, plt)
    return ax


def task2(ax, data_frame):
    ax.set_facecolor("black")
    x_values, y_values, ball_colors = get_columns_array(data_frame)
    for i in range(0, len(x_values)):
        light = Light((x_values[i], y_values[i]), ball_colors[i])
        light.plotLight(ax)
    plt.title("Coloured Lights - From File", fontsize="18")
    folder_path = "./src/images/"
    task_name = "task2.png"
    save_image(folder_path, task_name, plt)
    return ax


def task3(ax, data_frame):
    ax.set_facecolor("black")
    x_values, y_values, ball_colors = get_columns_array(data_frame)
    general_colors = ["yellow", "green", "royalblue", "violet", "red", "orange"]
    print(general_colors)
    move_colors(general_colors, 1)
    print(general_colors)
    # light = Light((x_values[0], y_values[0]), ball_colors[0])
    # light.plotLight(ax)
    # light = Light((x_values[1], y_values[1]), ball_colors[1])
    # light.plotLight(ax)
    # light = Light((x_values[2], y_values[2]), ball_colors[2])
    # for t in range(0, 10):
    # light = Light((x_values[t], y_values[t]), ball_colors[t])
    # light.plotLight(ax)
    # light.plotLight(ax)
    # print(ball_colors)

    # for t in range(0,5):
    # for i in range(0,len(x_values)):

    # for i in range(0, len(x_values)):

    # light = Light((x_value"s[i], y_values[i]), ball_colors[i])
    # light.plotLight(ax)

    # subIndex = 1
    # plt.title(f"Moving Coloured lights i:{subIndex}", fontsize="18")
    # index = 1
    # savePath = f"./images/task3/task3_{index}.png"
    # plt.savefig(savePath)
    print("task3")
    pass


def task4(ax, data_frame):
    ax.set_facecolor("black")
    x_values, y_values, ball_colors = get_columns_array(data_frame)
    general_colors = ["red", "orange", "yellow", "green", "royalblue", "violet"]
    move_colors(general_colors, 4)
    print(general_colors)
    list_colors(general_colors, ball_colors)
    for i in range(0, len(x_values)):
        light = Light((x_values[i], y_values[i]), ball_colors[i])
        light.plotLight(ax)
    bubbleMachine = BubbleMachine((0, 200))
    for t in range(0, 100):
        bubbleMachine.plotBubbles(ax)
        bubbleMachine.stepChange()
        if t < 11:
            plt.title(f"Floating Bubbles i : {t}", fontsize="18")
            folder_path = "./src/images/task4/"
            task_name = f"task4_{t}.png"
            save_image(folder_path, task_name, plt)

    plt.show()
