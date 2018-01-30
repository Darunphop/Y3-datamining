import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

def preprocess(raw):
    threshole_percentile = 96
    md = np.median(raw[13].dropna())
    threshole_val = np.percentile(raw[13].dropna(),threshole_percentile)
    where_are_NaNs = np.isnan(raw[13])
    raw[13][where_are_NaNs] = md
    raw[13][ raw[13] > threshole_val] = np.nan
    where_are_NaNs = np.isnan(raw[13])
    raw["index"][where_are_NaNs] = np.nan
    print(md)
    print(threshole_val)
    return raw

def ploting(data,na_data,showNA=True):
    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    # ax.scatter(data["index"], data[13],s=5)
    sns.pointplot(x="index", y=13, data=data, markers='o', size=0.8,linewidth=0, scale=0.4,ax=ax)
    if showNA == True:
        ax.scatter(na_data, np.full_like(na_data, 250),s=50,c='r')
    plt.xticks(np.arange(min(data["index"]), max(data["index"]), 1))

def boxplot(data):
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    ax = sns.boxplot(x=13, data=data)
    
def lineplot(data):
    fig = plt.figure(2)
    ax = fig.add_subplot(111)
    sns.pointplot(x="index", y=13, data=data, markers='o', size=0.8,linewidth=0, scale=0.4)

def rangeplot(data,middle,rangew):
    fig = plt.figure(3)
    ax = fig.add_subplot(111)
    for i in range(0,1):
        print(middle[i])
        print(data[13][middle[i]-rangew:middle[i]+rangew]-1)
        y = data[13][middle[i]-rangew:middle[i]+rangew].dropna()
        x = data["index"][middle[i]-rangew:middle[i]+rangew].dropna()

        ax = sns.regplot(x=x, y=y, order=4, ci=None, truncate=True)

    return

if __name__=="__main__":
    data = pd.read_csv('HW1DATA.csv', header=None, na_values='?')
    data['index'] = np.arange(1, len(data)+1)

    unknow_index = data.loc[data[13].isnull()]['index'].values

    data = preprocess(data)
    # sns.stripplot(unknow_index,linewidth=3,size=0.5)

    # ploting(data,unknow_index,False)
    # boxplot(data)
    # lineplot(data)
    
    rangeplot(data,unknow_index,10)

    # ax = sns.stripplot(x="index", y=13, data=data, size=0.8,linewidth=2)
    # ax.get_xaxis().set_visible(False)
    # sns.distplot(data[13].dropna())
    # sns.boxplot(x=13, data=data)
    # sns.pointplot()
    # sns.pointplot(data[13].dropna())

    # print(unknow_index)

    # ax = sns.regplot(x=data["index"], y=data[13], data=data, order=3, ci=None, truncate=True)

    # for i in unknow_index:
    #     print(data[13][i-1], i)

    plt.grid(alpha=0.5)
    plt.show()