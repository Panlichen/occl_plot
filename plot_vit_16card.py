import plot_bar

import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
# from brokenaxes import brokenaxes
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

legends = ["NCCL", "OCCL"]
x_labels = [i+1 for i in range(198)]

data_set = ["base", "large"]

data_dict = {
    data_set[0]: {
        legends[0]: [660.72, 660.57, 646.57, 646.74, 646.52, 650.9, 651.14, 649.89, 649.45, 651.65, 651.64, 651.31, 651.49, 651.64, 651.32, 651.58, 652.79, 652.48, 651.5, 652.06, 652.86, 653.01, 652.63, 652.99, 653.18, 652.18, 652.68, 652.59, 652.21, 651.91, 651.32, 651.51, 651.57, 652.13, 652.37, 652.33, 652.47, 652.83, 652.91, 653.14, 653.62, 653.67, 653.61, 653.6, 653.66, 653.45, 653.47, 653.36, 653.26, 653.16, 653.08, 653.2, 653.31, 653.33, 653.32, 653.36, 653.67, 653.8, 653.64, 653.53, 653.43, 653.82, 653.72, 653.57, 653.69, 653.31, 653.63, 653.59, 653.41, 653.45, 653.64, 653.82, 653.68, 653.58, 653.54, 653.5, 653.49, 653.4, 653.36, 653.25, 653.02, 652.77, 652.76, 652.61, 652.57, 652.54, 652.51, 652.8, 652.74, 652.57, 652.47, 652.44, 652.71, 652.6, 652.58, 652.55, 652.78, 652.7, 652.52, 652.39, 652.34, 652.46, 652.35, 652.2, 652.22, 652.14, 652.09, 652.28, 652.4, 652.48, 652.46, 652.23, 652.24, 652.27, 652.19, 652.21, 652.31, 652.37, 652.37, 652.43, 652.52, 652.5, 652.53, 652.4, 652.47, 652.48, 652.46, 652.53, 652.57, 652.62, 652.56, 652.56, 652.49, 652.44, 652.46, 652.41, 652.43, 652.29, 652.19, 651.97, 651.95, 651.97, 651.9, 651.94, 651.92, 651.79, 651.8, 651.77, 651.8, 651.88, 651.92, 651.88, 651.81, 651.8, 651.81, 651.85, 651.86, 651.83, 651.88, 651.89, 652.05, 652.07, 652.09, 652.1, 652.18, 652.13, 652.05, 652.06, 652.02, 652.05, 652.04, 652.05, 652.02, 652.01, 652.02, 651.94, 651.84, 651.91, 651.85, 651.8, 651.81, 651.78, 651.76, 651.78, 651.72, 651.67, 651.61, 651.57, 651.62, 651.6, 651.6, 651.65, 651.59, 651.58, 651.48, 651.5, 651.36, 651.33],
        legends[1]: [649.96, 650.49, 656.04, 648.38, 650.31, 650.84, 652.31, 651.66, 650.82, 650.18, 653.79, 655.09, 654.53, 655.42, 655.14, 654.13, 654.95, 653.93, 653.05, 651.45, 651.04, 650.83, 650.86, 650.79, 650.5, 650.64, 651.23, 651.24, 650.56, 650.37, 650.44, 650.19, 650.07, 650.8, 650.13, 649.84, 649.58, 649.29, 649.54, 649.38, 649.42, 649.63, 649.23, 648.83, 648.75, 648.69, 648.32, 648.61, 648.73, 648.24, 648.39, 648.27, 648.68, 648.71, 648.8, 649, 649.22, 649.1, 649.27, 649.31, 649.32, 649.02, 649.41, 649.46, 649.04, 649.25, 649.2, 649.22, 649.43, 649.82, 649.69, 649.73, 650.02, 650.04, 649.86, 650.36, 650.02, 650.03, 649.84, 650.15, 650.01, 649.91, 649.87, 649.81, 649.74, 649.57, 649.62, 649.73, 649.79, 649.71, 649.81, 649.91, 650.27, 650.2, 650.16, 650.12, 649.99, 649.77, 649.64, 649.77, 649.54, 649.64, 649.64, 649.63, 649.61, 649.59, 649.54, 649.39, 649.28, 649.32, 649.45, 649.32, 649.16, 649.06, 649.2, 649.26, 649.21, 649.19, 649.35, 649.39, 649.23, 649.16, 649.12, 649.02, 649.05, 649.12, 649.3, 649.38, 649.34, 649.23, 649.12, 649.16, 649.12, 649, 649.03, 649.06, 649.11, 648.98, 648.91, 648.98, 649.05, 649.05, 649.23, 649.25, 649.21, 649.18, 649.1, 648.99, 648.95, 648.83, 648.99, 648.89, 648.82, 648.76, 648.7, 648.58, 648.66, 648.65, 648.67, 648.69, 648.57, 648.63, 648.7, 648.59, 648.43, 648.44, 648.24, 648.36, 648.33, 648.28, 648.43, 648.53, 648.5, 648.59, 648.47, 648.44, 648.48, 648.57, 648.54, 648.49, 648.6, 648.59, 648.57, 648.58, 648.6, 648.62, 648.53, 648.45, 648.53, 648.49, 648.56, 648.57, 648.51, 648.54, 648.5, 648.52, 648.55, 648.45]
    },
    data_set[1]: {
        legends[0]: [254.83, 257.29, 260.7, 262.61, 262.68, 262.4, 262.95, 261.7, 261.51, 262.01, 262.23, 262.57, 262.81, 262.41, 262.67, 262.98, 263.07, 263.2, 263.2, 263.16, 263.2, 263.12, 263.44, 263.25, 263.32, 263.31, 263.24, 263.31, 263.4, 263.58, 263.47, 263.23, 263.2, 263.31, 263.42, 263.45, 263.29, 263.06, 263.06, 263.12, 263.24, 263.15, 263.16, 263, 263.14, 262.95, 262.98, 262.85, 262.93, 263.01, 263.16, 263.01, 263.03, 262.92, 262.95, 262.85, 262.91, 262.85, 262.92, 262.84, 262.67, 262.68, 262.69, 262.64, 262.73, 262.67, 262.66, 262.63, 262.7, 262.72, 262.85, 262.9, 262.92, 263.01, 262.93, 262.86, 262.91, 263.01, 263.1, 263.11, 263.22, 263.3, 263.32, 263.25, 263.2, 263.31, 263.41, 263.33, 263.38, 263.38, 263.39, 263.4, 263.39, 263.32, 263.37, 263.43, 263.33, 263.35, 263.3, 263.29, 263.37, 263.38, 263.46, 263.5, 263.58, 263.56, 263.62, 263.6, 263.63, 263.66, 263.72, 263.65, 263.69, 263.72, 263.67, 263.66, 263.69, 263.74, 263.79, 263.79, 263.83, 263.81, 263.75, 263.78, 263.76, 263.76, 263.73, 263.75, 263.75, 263.76, 263.83, 263.82, 263.8, 263.78, 263.76, 263.8, 263.73, 263.71, 263.74, 263.73, 263.73, 263.7, 263.7, 263.68, 263.63, 263.64, 263.69, 263.72, 263.7, 263.68, 263.65, 263.57, 263.62, 263.67, 263.69, 263.63, 263.66, 263.71, 263.7, 263.7, 263.69, 263.69, 263.7, 263.7, 263.71, 263.71, 263.72, 263.72, 263.67, 263.68, 263.68, 263.68, 263.68, 263.64, 263.62, 263.59, 263.64, 263.62, 263.63, 263.65, 263.68, 263.65, 263.61, 263.67, 263.6, 263.6, 263.61, 263.66, 263.74, 263.77, 263.77, 263.77, 263.74, 263.74, 263.68, 263.69, 263.7, 264.68],
        legends[1]: [263.84, 261.77, 261.91, 259.7, 258.86, 258.32, 259.16, 260.1, 260.25, 259.8, 259.04, 259.15, 259.55, 260.28, 260.36, 260.17, 259.78, 259.82, 260.2, 260.03, 259.83, 259.37, 259.42, 259.11, 259.13, 259.24, 259.46, 259.47, 259.57, 259.52, 259.95, 259.78, 259.85, 260.06, 260.22, 260.13, 260.03, 259.81, 259.69, 259.83, 259.73, 259.74, 259.89, 259.82, 259.87, 259.82, 259.89, 259.61, 259.63, 259.7, 259.86, 259.87, 259.92, 260.09, 260.36, 260.31, 260.31, 260.52, 260.51, 260.34, 260.37, 260.48, 260.48, 260.41, 260.37, 260.36, 260.48, 260.43, 260.37, 260.21, 260.18, 260.16, 260.09, 260.17, 260.21, 260.15, 260.08, 260.11, 260.2, 260.1, 260.11, 260.11, 260.01, 259.88, 259.85, 259.84, 259.89, 259.83, 259.82, 259.69, 259.8, 259.72, 259.72, 259.76, 259.81, 259.74, 259.8, 259.82, 259.88, 259.95, 259.92, 259.86, 259.9, 259.89, 259.92, 260, 260.05, 259.93, 259.97, 260.02, 260.05, 259.98, 259.99, 259.95, 259.98, 259.99, 260.05, 260.06, 260.09, 260.07, 260.1, 260.11, 260.15, 260.14, 260.14, 260.05, 260.03, 259.93, 259.89, 259.91, 259.96, 259.88, 259.86, 259.87, 259.84, 259.87, 259.86, 259.86, 259.89, 259.88, 259.94, 259.93, 259.93, 259.91, 259.91, 259.94, 259.89, 259.9, 259.81, 259.83, 259.84, 259.83, 259.91, 259.92, 259.95, 259.94, 259.95, 259.95, 260, 259.99, 260.01, 260.03, 260.01, 260.03, 260.07, 260.06, 260.04, 260.06, 260.1, 260.15, 260.18, 260.15, 260.13, 260.16, 260.12, 260.09, 260.16, 260.18, 260.12, 260.13, 260.17, 260.21, 260.27, 260.25, 260.29, 260.3, 260.34, 260.29, 260.32, 260.38, 260.39, 260.37, 260.39, 260.4, 260.43, 260.46, 260.51, 258.22]
    }
}

color_dict = {
    legends[0]: (255/255, 158/255, 2/255),
    legends[1]: (33/255, 158/255, 188/255),
}

def plot_lines(data_dict, figname, figsize, the_data_set="", legends_loc="best"):
    plt.close("all")
    plt.figure(1, figsize=figsize)

    plot_line_dict = {}
    for legend in legends:
        plot_line_dict.setdefault(legend, np.array(data_dict[legend]))

    x_pos = np.array([i for i in range(len(x_labels))])
    for legend in legends:
        plt.plot(x_pos, plot_line_dict[legend], color=color_dict[legend])
    plt.legend(legends, prop={'size': '13'}, loc=legends_loc)
    plt.ylim(0,np.max(plot_line_dict[legends[0]]) * 1.2)
    plt.ylabel("Training\nThroughput", size="16")
    plt.xlabel("Training Iteration", size="16")
    plt.tick_params(axis='y', labelsize="16")
    plt.tick_params(axis='x', labelsize='16')
    plt.tight_layout()
    plt.savefig(figname)
    plt.show()
    
if __name__ == "__main__":
    for the_data_set in data_set[:4]:
        figname = "figures_vit_16card/vit_16card_"+the_data_set+".pdf"
        print(figname)
        plot_lines(data_dict[the_data_set], figname, (5, 2.4), the_data_set)
