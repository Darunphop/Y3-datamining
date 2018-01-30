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
    # print(md)
    # print(threshole_val)
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

def rangeplot(data,middle,window):
    reg_f = []
    for i in range(0,len(middle)):
    # for i in range(0,1):
        fig = plt.figure(middle[i])
        ax = fig.add_subplot(111)
        # print(middle[i])
        # print(data[13][middle[i]-window:middle[i]+window])
        y = data[13][middle[i]-window:middle[i]+window].dropna()
        x = data["index"][middle[i]-window:middle[i]+window].dropna()

        reg_f.append(np.polyfit(x, y, 4))
        # print(data[13][middle[i]])
        new_point = np.polyval(reg_f[i],middle[i])
        data[13][middle[i]-1] = new_point

        

        ax.scatter(middle[i], new_point,s=50,c='r')
        

        sns.regplot(x=x, y=y, order=4, ci=None, truncate=True)

        plt.grid(alpha=0.5)
    return reg_f

if __name__=="__main__":
    data = pd.read_csv('HW1DATA.csv', header=None, na_values='?')
    data['index'] = np.arange(1, len(data)+1)

    unknow_index = data.loc[data[13].isnull()]['index'].values
    
    data = preprocess(data)
    # sns.stripplot(unknow_index,linewidth=3,size=0.5)

    # ploting(data,unknow_index,False)
    # boxplot(data)
    # lineplot(data)

    reg_f = rangeplot(data,unknow_index,10)

    # ax = sns.stripplot(x="index", y=13, data=data, size=0.8,linewidth=2)
    # ax.get_xaxis().set_visible(False)
    # sns.distplot(data[13].dropna())
    # sns.boxplot(x=13, data=data)
    # sns.pointplot()
    # sns.pointplot(data[13].dropna())

    # print(unknow_index)

    # ax = sns.regplot(x=data["index"], y=data[13], data=data, order=3, ci=None, truncate=True)

    for i in unknow_index:
        print(data[13][i-1], i)

    # print(reg_f[0].get_lines()[0].get_xdata())
    # print(reg_f[0].get_lines()[0].get_ydata())

    k=0
    for i in unknow_index:
        print(i," : ",np.polyval(reg_f[k],i))
        k += 1

    plt.show()