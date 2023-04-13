import plot_bar

import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
# from brokenaxes import brokenaxes
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

legends = ["# Ctx. Switch", "Task Q Len."]
x_labels = [i for i in range(161)] # 不真的打印出来。

dataset = ["GPU-0", "GPU-2"] # 0是thrash的那个

data_dict = {
    dataset[0]: {
        legends[0]: [0, 555, 545, 535, 525, 515, 295, 285, 275, 265, 255, 245, 235, 225, 215, 205, 195, 185, 175, 165, 155, 145, 135, 125, 115, 105, 95, 85, 75, 65, 55, 45, 35, 25, 15, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        legends[1]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    },
    dataset[1]: {
        legends[0]: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        legends[1]: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    }
}

color_dict = {
    legends[0]: (203/255, 153/255, 126/255), # bar的颜色，在下边。
    legends[1]: (107/255, 112/255, 92/255),
}

def plot_line_bar(data_dict, figsize, bar_width, the_data_set, legends_loc="best", y_nbins=None, hline=False):

    plot_bar_data_dict = {}
    plot_line_data_dict = {}

    for i, legend in enumerate(legends):
        if i < 1: # bar
            plot_bar_data_dict.setdefault(legend, np.array(data_dict[legend]))
        else:
            plot_line_data_dict.setdefault(legend, np.array(data_dict[legend]))

    # 提前设置：
    x_pos = x_labels
    y_labelsize = '16'

    # 先画bar
    plt.close("all")
    plt.figure(1, figsize=figsize)
    figname = "figures_resnet_extra/"+"resnet_ctx_switch_"+the_data_set+".pdf"
    print(figname)

    for i, legend in enumerate(legends):
        if i < 1:
            # plt.bar(x_pos, plot_bar_data_dict[legend], color=color_dict[legend], bottom=-10)
            # , bar_width
            plt.plot(x_pos, plot_bar_data_dict[legend], color=color_dict[legend], linewidth=3)
    plt.ylabel("# Ctx.\nSwitch", size='16')
    plt.tick_params(axis='y', labelsize=y_labelsize)
    plt.ylim(-20, 580)
    plt.xticks([])
    plt.xlabel("IDs of Collectives", size='16')
    # plt.legend([legends[0]], loc=legends_loc, prop={'size': '16'})
    plt.tight_layout()
    plt.savefig(figname)
    plt.show()


    # 再画line
    # lines = []
    plt.close("all")
    plt.figure(1, figsize=figsize)
    figname = "figures_resnet_extra/"+"resnet_taskq_len_"+the_data_set+".pdf"
    print(figname)
    for i, legend in enumerate(legends):
        if i >= 1:
            plt.plot(x_pos, plot_line_data_dict[legend], color=color_dict[legend], linewidth=3)
    plt.ylabel("Task Q\nLen.", size='16')
    plt.tick_params(axis='y', labelsize=y_labelsize)
    plt.ylim(-1, 40)
    plt.xticks([])
    plt.xlabel("IDs of Collectives", size='16')
    # plt.legend(legends, loc=legends_loc, prop={'size': '16'})
    plt.tight_layout()
    plt.savefig(figname)
    plt.show()

if __name__ == "__main__":
    # the_data_set = dataset[0]
    # plot_line_bar(data_dict[the_data_set], (5, 3.3), 0.1, the_data_set)

    for the_data_set in dataset:
        plot_line_bar(data_dict[the_data_set], (5, 1.4), 0.1, the_data_set)
