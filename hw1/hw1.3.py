import bokeh
import codecs
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

def read_file():
    file_path = "./HW1DATA.txt"
    with codecs.open(file_path, "r",encoding='utf-8', errors='ignore') as f:
        content = f.readlines()
    data = []
    for i in content:
        data.append(i.split(","))
    trans_data = []
    for i in data:
        trans_data.append(i[13])
    return trans_data

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

def ploting(data):
    ax = plt.scatter(data["index"], data[13],s=5)
    plt.xticks(np.arange(min(data["index"]), max(data["index"]), 50))

if __name__=="__main__":
    data = pd.read_csv('HW1DATA.csv', header=None, na_values='?')
    data['index'] = np.arange(1, len(data)+1)

    unknow_index = data.loc[data[13].isnull()]['index'].values

    # sns.stripplot(unknow_index,linewidth=3,size=0.5)

    ploting(data)

    # sns.pointplot(x="index", y=13, data=data, markers='o', size=0.8,linewidth=0)
    # ax = sns.stripplot(x="index", y=13, data=data, size=0.8,linewidth=2)
    # ax.get_xaxis().set_visible(False)
    # sns.distplot(data[13].dropna())
    # sns.boxplot(x=13, data=data)
    # sns.pointplot()
    # sns.pointplot(data[13].dropna())


    plt.grid(alpha=0.5)
    plt.show()