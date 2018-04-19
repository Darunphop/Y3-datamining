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

    print(input.head(5))
    input['school'] = input['school'].apply(lambda x:binary('GP', x))
    input['sex'] = input['sex'].apply(lambda x:binary('F', x))
    input['age'] = input['age'].apply(lambda x:scaling(15, 22, x))
    input['address'] = input['address'].apply(lambda x:binary('U', x))
    input['famsize'] = input['famsize'].apply(lambda x:binary('LE3', x))
    input['Pstatus'] = input['Pstatus'].apply(lambda x:binary('T', x))
    input['Medu'] = input['Medu'].apply(lambda x:scaling(0, 4, x))
    input['Fedu'] = input['Fedu'].apply(lambda x:scaling(0, 4, x))
    input['Mjob'] = input['Mjob'].apply(lambda x:nominal(['teacher', 'health', 'services', 'at_home', 'other'], x))
    input['Fjob'] = input['Fjob'].apply(lambda x:nominal(['teacher', 'health', 'services', 'at_home', 'other'], x))
    input['reason'] = input['reason'].apply(lambda x:nominal(['home', 'reputation', 'course', 'other'], x))
    input['guardian'] = input['guardian'].apply(lambda x:nominal(['mother', 'father', 'other'], x))
    input['traveltime'] = input['traveltime'].apply(lambda x:scaling(1, 4, x))
    input['studytime'] = input['studytime'].apply(lambda x:scaling(1, 4, x))
    input['failures'] = input['failures'].apply(lambda x:scaling(1, 4, x))
    input['schoolsup'] = input['schoolsup'].apply(lambda x:binary('yes', x))
    input['famsup'] = input['famsup'].apply(lambda x:binary('yes', x))
    input['paid'] = input['paid'].apply(lambda x:binary('yes', x))
    input['activities'] = input['activities'].apply(lambda x:binary('yes', x))
    input['nursery'] = input['nursery'].apply(lambda x:binary('yes', x))
    input['higher'] = input['higher'].apply(lambda x:binary('yes', x))
    input['internet'] = input['internet'].apply(lambda x:binary('yes', x))
    input['romantic'] = input['romantic'].apply(lambda x:binary('yes', x))
    input['famrel'] = input['famrel'].apply(lambda x:scaling(1, 5, x))
    input['freetime'] = input['freetime'].apply(lambda x:scaling(1, 5, x))
    input['goout'] = input['goout'].apply(lambda x:scaling(1, 5, x))
    input['Dalc'] = input['Dalc'].apply(lambda x:scaling(1, 5, x))
    input['Walc'] = input['Walc'].apply(lambda x:scaling(1, 5, x))
    input['health'] = input['health'].apply(lambda x:scaling(1, 5, x))
    input['absences'] = input['absences'].apply(lambda x:scaling(0, 93, x))






    print(input.head(5))
    return res

def scaling(min, max, x):
    return (x - min)/(max - min)

def binary(a, x):
    return 1 if x == a else 0

def nominal(p_list, x):
    for n, i in enumerate(p_list):
        if i == x:
            return scaling(0, len(p_list)-1, n)

if __name__ == '__main__':
    data = loadFile(1)
    sff_data = data.sample(frac=1).sample(frac=1)
    new_df = sff_data.head(90).tail(10)
    print('--------------------')
    kFold(10, sff_data)
    