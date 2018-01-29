import bokeh
import codecs
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

def preprocess(raw):
    data = []
    index = 0
    for i in raw:
        # try:
        #     data.append([index, int(i)])
        # except ValueError:
        #     data.append([index, -1])
        # index += 1
        try:
            data.append(int(i))
        except ValueError:
            data.append(-1)
    return data

def ploting(data,na_data):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data["index"], data[13],s=5)
    ax.scatter(na_data, np.full_like(na_data, 250),s=20,c='r')
    plt.xticks(np.arange(min(data["index"]), max(data["index"]), 50))

if __name__=="__main__":
    data = pd.read_csv('HW1DATA.csv', header=None, na_values='?')
    data['index'] = np.arange(1, len(data)+1)

    unknow_index = data.loc[data[13].isnull()]['index'].values

    # sns.stripplot(unknow_index,linewidth=3,size=0.5)

    ploting(data,unknow_index)

    # sns.pointplot(x="index", y=13, data=data, markers='o', size=0.8,linewidth=0)
    # ax = sns.stripplot(x="index", y=13, data=data, size=0.8,linewidth=2)
    # ax.get_xaxis().set_visible(False)
    # sns.distplot(data[13].dropna())
    # sns.boxplot(x=13, data=data)
    # sns.pointplot()
    # sns.pointplot(data[13].dropna())


    plt.grid(alpha=0.5)
    plt.show()