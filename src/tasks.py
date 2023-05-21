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


def task3(ax, data_frame):
    ax.set_facecolor("black")
    x_values, y_values, ball_colors = get_columns_array(data_frame)
    general_colors = ["red", "orange", "yellow", "green", "royalblue", "violet"]
    for t in range(0, len(x_values)):
        light = Light((x_values[t], y_values[t]), ball_colors[t])
        light.plotLight(ax)
    plt.title("Moving Coloured Lights i : 0", fontsize="18")
    folder_path = "./src/images/task3/"
    task_name = "task3_0.png"
    save_image(folder_path, task_name, plt)
    for i in range(0, 5):
        move_colors(general_colors, 1)
        list_colors(general_colors, ball_colors)
        print(ball_colors)
        for t in range(0, len(x_values)):
            light = Light((x_values[t], y_values[t]), ball_colors[t])
            light.plotLight(ax)
        plt.title(f"Moving Coloured Lights i : {i+1}", fontsize="18")
        folder_path = "./src/images/task3/"
        task_name = f"task3_{i+1}.png"
        save_image(folder_path, task_name, plt)


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

    # plt.show()
