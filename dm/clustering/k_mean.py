import numpy as np

def kmeans(dataSet, k):
	
    centroids = randomCentroids(dataSet.shape[1], k)

    iterations = 0
    diff = 9999
    o_centroids = None
    epsilon = 0.001
    max_iterations = 150

    while stopCondition(diff, iterations, epsilon, max_iterations):
        o_centroids = centroids
        iterations += 1

        labels = getLabels(dataSet, centroids)

        centroids = findMean(labels)

        diff = sum([distant(centroids[i], o_centroids[i]) for i in range(len(centroids))])
        # print('This diff :',diff,'i :', iterations)
    
    return centroids, labels

def randomCentroids(attr, k):
    res = []
    for i in range(k):
        tmp = []
        for j in range(attr):
            tmp.append(np.random.rand())
        res.append(tmp)
    return res

def distant(a, b):
    # print(a,b)
    return np.sqrt(sum((a[:-1] - b[:-1]) ** 2))

def stopCondition(dif_c, iterations, epsilon=0.1, max_it = 1000):
    # n_attr = len(n_centroids)
    # dif_c = sum([distant(n_centroids[i], o_centroids[i]) for i in range(n_attr)])
    # print(dif_c)
    return dif_c > epsilon and iterations < max_it

def getLabels(data, centroids):
    res = [[] for i in range(len(centroids))]
    for i in data:
        # print(i)
        min = [1000,-1]
        for nj, j in enumerate(centroids):
            dis = distant(i,j)
            if dis < min[0]:
                min[0] = dis
                min[1] = nj
        res[min[1]].append(i)
    return np.asarray(res)

def findMean(labels, s_attr=33):
    res = []
    for i in labels:
        l = len(i)
        # print(l)
        # tmp = [a/l for a in [sum(x) for x in zip(*i)]]    #   Arithmetic mean
        tmp = [np.power(a, 1./l) for a in [np.prod(x) for x in zip(*i)]]  #   Gemotric mean
        # print(tmp)
        if tmp == []:
            # print('reinitialize centroid')
            tmp = list(np.random.rand(s_attr))
        res.append(tmp)
    return np.asarray(res)

def evalLabels(labels):
    k = len(labels)
    res = []
    for i in labels:
        tmp = []
        for j in i:
            # print(len(j))
            tmp.append(int(j[-1:][0]))
        res.append(tmp)
    return np.asarray(res)

def getPurity(labels, k=21):
    s = 0
    ip = 0
    for i in labels:
        s += len(i)
        max = [0 for x in range(k)]
        for nj, j in enumerate(i):
            max[int(j[-1:][0])] += 1
        ip += max[np.argmax(max)]
    return ip / s

if __name__ =='__main__':
    pass