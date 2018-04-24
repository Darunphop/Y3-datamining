import numpy as np

class Knn:
    def __init__(self, k):
        self.k = k

    def finNearest(self, dataset):
        pass

    def distant(self, a, b):
        res = 0
        for i in range(len(a)):
            res += np.power(a[i] - b[i], 2)
        return np.sqrt(res)
    
    def setData(self, input):
        d = input.shape[0]
        # d = 5
        res = np.zeros((d, d))
        for i in range(d):
            for j in range(i, d):
                if i != j:
                    print(i, j)
                    res[i][j] = self.distant(input.iloc[i], input.iloc[j])
        return res

if __name__ =='__main__':
    pass