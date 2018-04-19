import numpy as np
import pandas as pd
import os
import math
input_file = {1:'student-mat.csv', 2:'student-por.csv'}

def loadFile(file_number=1):
    if not file_number in input_file:
        file_number = 1

    fpath = os.path.join('dataset', input_file[file_number])
    return pd.read_csv(fpath, sep=';', header=0, na_values='?')

def kFold(k, data):
    data_len = len(data)
    bin_size = math.floor(data_len / k)
    remainder = data_len % bin_size
    res = []
    print('dLen', data_len)
    print('bSize', bin_size)
    print('rem', remainder)

    shared_train = data.tail(remainder)
    data.drop(data.tail(remainder).index,inplace=True)
    new_len = len(data)

    for i in range(k):
        if i == 0:
            train = data.tail(new_len - (bin_size * (i+1)))
            test = data.head(bin_size)
        elif i == k-1:
            train = data.head(i * bin_size)
            test = data.tail(bin_size)
        else:
            train = data.head(i * bin_size).append(data.tail(new_len - (bin_size * (i+1))))
            test = data.head((i+1) * bin_size).tail(bin_size)
        train = train.append(shared_train)
        res.append([train, test])

    return res

def normalize(input, output_s):
    res = []
    num_attr = input.shape[1]

    # input['school'].replace(to_replace='GP', value=0, inplace=True)
    # input['school'].replace(to_replace='MS', value=1, inplace=True)
    
    # input['sex'].replace(to_replace='F', value=0, inplace=True)
    # input['sex'].replace(to_replace='M', value=1, inplace=True)

    # input['sex'].replace(to_replace='F', value=0, inplace=True)
    # input['sex'].replace(to_replace='M', value=1, inplace=True)
    # input.set_value('school',0,555)
    # print(input)
    print(input['age'].head(5))
    input['age'] = input['age'].apply(lambda x:scaling(15, 22, x))
    print(input['age'].head(5))
    return res

def scaling(min, max, x):
    # print((x - min)/(max - min))
    return (x - min)/(max - min)

if __name__ == '__main__':
    data = loadFile(1)
    sff_data = data.sample(frac=1).sample(frac=1)
    new_df = sff_data.head(90).tail(10)
    print('--------------------')
    kFold(10, sff_data)
    