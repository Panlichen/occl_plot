import plot_bar

import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
# from brokenaxes import brokenaxes
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

legends = ["128B", "128KB", "128MB"]
x_labels = ["Read SQE", "Extra Overheads", "Write CQE"]

time = {
    legends[0]: {
        x_labels[0]: [5.21, 5.13, 5.09, 5.29, 5.12],
        x_labels[1]: [1.21, 1.21, 1.21, 1.21, 1.21],
        x_labels[2]: [1.99, 1.99, 1.99, 1.98, 1.98]
    },
    legends[1]: {
        x_labels[0]: [5.95, 5.11, 5.86, 5.88, 5.87, 4.91, 5.92, 4.65, 4.83, 4.48],
        x_labels[1]: [1.26, 1.26, 1.25, 1.25, 1.26, 1.26, 1.25, 1.26, 1.26, 1.26],
        x_labels[2]: [1.93, 1.92, 1.88, 1.91, 1.89]
    },
    legends[2]: {
        x_labels[0]: [5.69, 10.75, 12.93, 12.97, 7.21, 6.97, 14.00, 10.66, 10.84, 8.56],
        x_labels[1]: [1.56, 1.60, 1.61, 1.63, 1.63, 1.58, 1.63, 1.64, 1.61, 1.61],
        x_labels[2]: [2.76, 2.83, 6.85, 6.84, 6.71]
    },
}

color_dict = {
    legends[0]: (144/255, 201/255, 231/255),
    legends[1]: (33/255, 158/255, 188/255),
    legends[2]: (19/255, 103/255, 131/255)
}

def plot_bar_avg_errbar_text(data_dict, figname, figsize, bar_width, legends_loc="best"):
    plt.close("all")
    plt.figure(1, figsize=figsize)
    
    plot_data_dict = {}
    for legend in legends:
        plot_data_dict.setdefault(legend, dict()).setdefault(
            "avg",
            np.array([np.mean(data_list)
                     for data_list in data_dict[legend].values()])
        )
        plot_data_dict.setdefault(legend, dict()).setdefault(
            "stderr",
            np.array([np.std(data_list)
                     for data_list in data_dict[legend].values()])
        )
    
    num_bar = len(legends)
    x_pos = np.array([i for i in range(len(x_labels))])
    error_attri = dict(capsize=2)
    for i, legend in enumerate(legends):
        pos = plot_bar.calc_bar_pos(num_bar, x_pos, i, bar_width)
        plt.bar(pos,plot_data_dict[legend]["avg"], bar_width,
                yerr=plot_data_dict[legend]["stderr"], error_kw=error_attri,
                color=color_dict[legend])
        for a, b in zip (pos, plot_data_dict[legend]["avg"]):
            plt.text(a, b+0.05, "%.1f" % b, ha='center', va='bottom', fontsize=16)
        
    plt.ylabel("Time (us)", size="20")
    plt.xticks(x_pos, x_labels)
    plt.legend(legends, prop={'size': '16'}, loc=legends_loc, ncol=3)
    plt.tick_params(axis='y', labelsize='18')
    plt.tick_params(axis='x', labelsize='20')
    plt.tight_layout()
    plt.savefig(figname)
    plt.show()


if __name__ == "__main__":
    plot_bar_avg_errbar_text(time, "figures_split/time_split.pdf", (10, 1.9), 0.2, "best")

    
