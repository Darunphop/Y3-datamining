import bokeh
import codecs
import numpy as np
import seaborn as sns
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

def ploting(dataset):
    sns.distplot(dataset)
    plt.show()

if __name__=="__main__":
    # data = preprocess(read_file())
    # for i in data:
    #     print(i)
    # ploting(data)

    data = pd.read_csv('HW1DATA.csv', header=None, na_values='?')
    data['index'] = np.arange(1, len(data)+1)

    print(data[13])
    sns.pointplot(x="index", y=13, data=data);
    # sns.pointplot()
    # sns.pointplot(data[13].dropna())
    plt.show()