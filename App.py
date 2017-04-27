import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

RESULT_DIR = 'result'
FILENAME_SEPARATOR = '_'

# Get files names
files = dict()
for file in os.listdir(RESULT_DIR):
    if file.endswith(".txt") :
        frameworkName = file.split(FILENAME_SEPARATOR)[0]
        if frameworkName not in files:
            files[frameworkName] = list()
        files[frameworkName].append(file)

# Ensure the Internet type is in the same order in all dictionary positions
n_groups = 0
X_labels = []
for key, values in files.items():
    files[key].sort(reverse=True)
    if n_groups == 0:
        n_groups = len(files[key])
    if not X_labels:
        X_labels = [(f.split(FILENAME_SEPARATOR)[2]).split(".")[0] for f in values]

# Data to plot
X_data = dict()
i = -1
for key, values in files.items():
    print(key)
    X_data[key] = list()
    for value in values:
        dataFrame = pd.read_csv(RESULT_DIR + '/' + value, sep=";", header=2)
        mean = np.mean(dataFrame[dataFrame.columns[-1]])  # mean of the last column (Speed Index)
        print("\t" + str(value) + ": " + str(mean))
        X_data[key].append(mean)

#create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.2
opacity = 0.8

colors = ['r', 'g', 'b', 'k', 'c']

for i, val in enumerate(X_data):
    lefts = index + (i*(bar_width+0.01))
    plt.bar(lefts, X_data[val], bar_width,
            alpha=opacity,
            color=colors[i],
            label=val)



plt.xlabel('Framework and Internet connection')
plt.ylabel('Speed Index')
plt.title('Scores by person')
plt.xticks(index + bar_width, X_labels) #Kolejnosc musi byc ta sama przy tworzeniu wykresu!
plt.legend()

plt.tight_layout()
plt.show()


