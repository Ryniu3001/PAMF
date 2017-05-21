import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os

RESULT_DIR = 'result'
FILENAME_SEPARATOR = '_'

# Get files names
files = dict()
for file in os.listdir(RESULT_DIR):
    if file.endswith(".txt") :
        type = file.split(FILENAME_SEPARATOR)[2].split('.')[0]
        if type not in files:
            files[type] = list()
        files[type].append(file)

# Ensure the Internet type is in the same order in all dictionary positions
n_groups = 0                # How many groups on chart
X_labels = []
for key, values in files.items():
    files[key].sort(reverse=True)
    if n_groups == 0:
        n_groups = len(files)
    if not X_labels:
        X_labels = [(f.split(FILENAME_SEPARATOR)[0]) for f in values]

# Data to plot
X_data = dict()
for key, values in files.items():
    print(key)
    X_data[key] = dict()
    for value in values:
        dataFrame = pd.read_csv(RESULT_DIR + '/' + value, sep=";", header=2)
        mean = dataFrame[dataFrame.columns[-1]]  # mean of the last column (Speed Index)
        print("\t" + str(value) + ": " + str(list(mean)))
        X_data[key][value] = list(mean)

# create plot

for key, values in X_data.items():
    data_to_plot = [l for l in X_data[key].values()]

    fig = plt.figure(1, figsize=(9, 6))
    ax = fig.add_subplot(111)
    bp = ax.boxplot(data_to_plot, sym='')
    ax.set(xticklabels=X_labels, xlabel=key, ylabel='Render Start [ms]', title='First Render Times')
    fig.savefig(str(key) + '_fig.png')
    plt.clf()


# fig, axes = plt.subplots(ncols=2, sharey=True)
# fig.subplots_adjust(wspace=0)
#
# for ax, name in zip(axes, X_data.keys()):
#     ax.boxplot([X_data[name][item] for item in X_data[name].keys()], sym='')
#     ax.set(xticklabels=['A', 'B', 'C', 'D'], xlabel=name)
#     ax.margins(0.05) # Optional
#
# plt.show()
