import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
count = 0

def preprocess(raw):
    threshole_percentile = 96
    md = np.median(raw[13].dropna())
    threshole_val = np.percentile(raw[13].dropna(),threshole_percentile)
    where_are_NaNs = np.isnan(raw[13])
    raw[13][where_are_NaNs] = md
    raw[13][ raw[13] > threshole_val] = np.nan      # Take out outliner from data
    where_are_NaNs = np.isnan(raw[13])              # Replace missing values with median
    raw["index"][where_are_NaNs] = np.nan
    return raw

def ploting(data,na_data,showNA=True,mode=True):
    global count
    fig = plt.figure(count)
    ax = fig.add_subplot(111)
    if mode == True:
        ax.scatter(data["index"], data[13],s=5)
    else:
        sns.pointplot(x="index", y=13, data=data, markers='o', size=0.8,linewidth=0, scale=0.4,ax=ax)
    if showNA == True:
        ax.scatter(na_data, np.full_like(na_data, 250),s=50,c='r')
    plt.xticks(np.arange(min(data["index"]), max(data["index"]), 1))
    count += 1

def boxplot(data):
    global count
    fig = plt.figure(count)
    ax = fig.add_subplot(111)
    ax = sns.boxplot(x=13, data=data)
    count += 1

def displot(data):
    global count
    fig = plt.figure(count)
    ax = fig.add_subplot(111)
    sns.distplot(data[13].dropna())
    count += 1

def rangeplot(data,middle,window,degree):
    global count
    reg_f = []
    for i in range(0,len(middle)):
        fig = plt.figure(middle[i])
        ax = fig.add_subplot(111)
        y = data[13][middle[i]-window:middle[i]+window].dropna()
        x = data["index"][middle[i]-window:middle[i]+window].dropna()

        reg_f.append(np.polyfit(x, y, degree))
        new_point = np.polyval(reg_f[i],middle[i])
        data[13][middle[i]-1] = new_point           # Update missing valuse from median to new value

        ax.scatter(middle[i], new_point,s=50,c='r') # Plot the new value of Missing Value
        
        sns.regplot(x=x, y=y, order=degree, ci=None, truncate=True)
        plt.grid(alpha=0.5)
    count += 1
    return reg_f

def show_missing_val(data,missing):
    k=0
    for i in missing:
        print(i," : ",np.polyval(data[k],i))
        k += 1

if __name__=="__main__":
    data = pd.read_csv('HW1DATA.csv', header=None, na_values='?')
    data['index'] = np.arange(1, len(data)+1)

    unknow_index = data.loc[data[13].isnull()]['index'].values

    ploting(data,unknow_index,False)    # Brefore preprocessing
    boxplot(data)

    data = preprocess(data)

    boxplot(data)
    ploting(data,unknow_index,False)

    reg_f = rangeplot(data,unknow_index,10,4)

    displot(data)

    show_missing_val(reg_f, unknow_index)

    plt.show()