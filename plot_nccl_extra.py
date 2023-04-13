import plot_bar

import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
# from brokenaxes import brokenaxes
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

legends = ["NCCL", "OCCL"]
x_labels = ["End-to-end Latency", "Core Execution Time"]

data_set = ["AG_4K", "RS_4M"]

data_dict = {
    data_set[0]: {
        legends[0]: {
            x_labels[0]: [44.61, 44.94, 45.48, 45.71, 45.01],
            x_labels[1]: [43.39, 38.24, 40.34, 38.58, 38.06, 37.75, 37.99, 38.05, 38.63, 45.07, 39.18, 37.85, 38.91, 38.79, 42.71, 37.79, 38.47, 38.36, 38.09]
        },
        legends[1]: {
            x_labels[0]: [48.91, 49.7, 49.83, 49.31],
            x_labels[1]: [38.06, 39.22, 39.44, 38.68, 39.13]
        }
    },
    data_set[1]: {
        legends[0]: {
            x_labels[0]: [855.8, 851.7, 856.9, 856.3],
            x_labels[1]: [852.527, 849.647, 846.927, 851.471, 838.703]
        },
        legends[1]: {
            x_labels[0]: [852.4, 846.6, 853.1, 853.3, 853.8],
            x_labels[1]: [818.8, 830.21, 832.81, 844.69, 822.49, 843.29, 832.74, 828.89, 821.09, 805.16]
        }
    },
}

color_dict = {
    legends[0]: (255/255, 158/255, 2/255),
    legends[1]: (33/255, 158/255, 188/255),
}

def plot_bar_avg_errbar(data_dict, figname, figsize, bar_width, the_data_set, legends_loc="lower center"):
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
            plt.text(a, b+0.05, "%.1f" % b, ha='center', va='bottom', fontsize=14)
        
    plt.ylabel("Time (us)", size="16")
    if (the_data_set == data_set[0]):
        plt.ylim(0, np.max(plot_data_dict[legends[0]]["avg"]) * 1.21)
    else:
        plt.ylim(0, np.max(plot_data_dict[legends[0]]["avg"]) * 1.16)
    plt.xticks(x_pos, x_labels)
    plt.legend(legends, prop={'size': '13'}, loc=legends_loc)
    plt.tick_params(axis='y', labelsize='14')
    plt.tick_params(axis='x', labelsize='16')
    plt.tight_layout()
    plt.savefig(figname)
    plt.show()

if __name__ == "__main__":
    for the_data_set in data_set:
        figname = "nccl_extra_"+the_data_set+".pdf"
        print(figname)
        plot_bar_avg_errbar(data_dict[the_data_set], "figures_nccl_extra/"+figname, (5.2, 3), 0.25, the_data_set)
