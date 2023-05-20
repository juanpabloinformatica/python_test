import matplotlib.pyplot as plt
from tasks import *
from stageLights import *
import pandas as pd


def main():
    SIZE = 10
    LIMITS = (1000, 1000)
    # light = Light((50, 50), "violet")
    ax = plt.axes()
    ax.set_xlim(0, LIMITS[0])
    ax.set_ylim(0, LIMITS[1])
    ax.set_aspect("equal")

    # making first task
    # ax = task1(ax)
    # making second task
    csv_file = "./csvFiles/lights.csv"
    data_frame = pd.read_csv(csv_file)
    ax = task2(ax, data_frame)
    # making third task
    # csv_file = "./csvFiles/col_lights.csv"
    # data_frame = pd.read_csv(csv_file)
    # ax = task3(ax, data_frame)
    # light.plotLight(ax)

    # bubbles.stepChange()
    # bubbles.plotBubbles(ax)

    # plt.title("Initial code", fontsize="18")
    # plt.show()
    # plt.pause(2)
    # plt.clf()


if __name__ == "__main__":
    main()
