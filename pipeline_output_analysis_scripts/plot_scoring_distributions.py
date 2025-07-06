import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import sys
import statistics
import numpy as np
from scipy.stats import mannwhitneyu


#Reading in the the results for the validation data.
data = sys.argv[1]
metric = str(sys.argv[2])
df = pd.read_csv(data)

def mannwhitneyu_test(df, metric):
    #Extracting the metric values and the binary label values
    data_metric = df[[metric, "Binary_Label"]]
    data_metric_1 = data_metric[data_metric["Binary_Label"] == 1]
    print(data_metric_1.shape)
    data_metric_0 = data_metric[data_metric["Binary_Label"] == 0]
    print(data_metric_0.shape)

    print(f"Median of TP: {statistics.median(data_metric_1[metric])}")
    print(f"Median of TN: {statistics.median(data_metric_0[metric])}")
    print(f"Mean of TP: {statistics.mean(data_metric_1[metric])}")
    print(f"Mean of TN: {statistics.mean(data_metric_0[metric])}")
    print(f"Standard deviation of TP: {statistics.stdev(data_metric_1[metric])}")
    print(f"Standard deviation of TN: {statistics.stdev(data_metric_0[metric])}")

    #Mann whitney U test
    stat, p_value = mannwhitneyu(data_metric_1[metric], data_metric_0[metric], alternative="two-sided")

    print(f"Statsitic = {stat}, P-value = {p_value:.2e}")

mannwhitneyu_test(df, metric)

#Initiating the font sizes for the subsequent plt plots
plt.rcParams.update({'font.size': 15})

def plot_metric_distribution(df, metric):

    #Extracting the ipTM values and the binary label values as 'data_iptm'
    data_metric = df[[metric, "Binary_Label"]]

    #Create a new column of labels of either "TP" or "TN" to make the plot more intuitive
    tp_tn = []

    for i in data_metric["Binary_Label"]:
        if i == 1:
            tp_tn.append("TP")
        else:
            tp_tn.append("TN")

    data_metric["TP_or_TN"] = tp_tn

    # Initiating a box plot with binary labels on the x axis and ipTM values on the y axis.
    ax = sns.boxplot(x='TP_or_TN', y=str(metric), data=data_metric, showfliers=False)

    #Overlay swarm plot
    sns.swarmplot(x='TP_or_TN', y=str(metric), data=data_metric, color=".2")

    #Set y-axis to scientific format
    #plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))


    # Add labels and title
    plt.xlabel(' ')
    plt.ylabel(f'Max {metric}')

    #Add test statistic annotation 
    # https://stackoverflow.com/questions/36578458/how-does-one-insert-statistical-annotations-stars-or-p-values
    x1, x2 = 0, 1
    y, h, col = data_metric[metric].max() + 5000, 5000, 'k'

    plt.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c=col)
    plt.text((x1+x2)*.5, y+h, "****", ha='center', va='bottom', color=col, fontsize = 15)


    #plt.yticks(np.arange(0, 1.2, 0.2))

    #Display the plot
    #plt.show()


plot_metric_distribution(df, metric)




   
    

