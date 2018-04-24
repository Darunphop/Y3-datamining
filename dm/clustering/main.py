import input
import k_mean as km
import numpy as np

if __name__ == '__main__':
    print('hi')
    data = input.loadFile()
    input.normalize(data)
    # print(data.iloc[1])
    x = np.zeros((2, 3))
    # print(x.shape)
    # print(km.randomCentroids(data.shape[1], 1))
    a = np.random.randint(10,size=(2,5))
    b = np.random.randint(10,size=(2,5))
    # print(a,b)
    # print(km.distant(a,b))
    # print(sum([i for i in range(3)]))
    # print(km.stopCondition(a,b,0))
    m = [[1,2,3],[4,5,6],[7,8,9]]
    # print(km.findMean(m))
    c = km.randomCentroids(33,5)
    cm = data.head(5).values
    l = km.getLabels(cm,c)
    # for i in l:
    #     print(i[:1])
    cmm = km.findMean(l)
    # print('----------------')
    # print(cmm)
    # print(len(cmm))
    # print(cm)
    # for i in (km.getLabels(cm,c)):
    #     print(i)
    l_c, l_l = km.kmeans(data.values, 21)
    print(km.evalLabels(l_l))
    # print(l_c)
    # print(data.groupby('G3').agg('count'))