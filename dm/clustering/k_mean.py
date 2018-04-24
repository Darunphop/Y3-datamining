import numpy as np

def kmeans(dataSet, k):
	
    centroids = randomCentroids(dataSet.shape[1], k)
    
    # Initialize book keeping vars.
    iterations = 0
    diff = 9999
    o_centroids = None
    epsilon = 0.001

    while stopCondition(diff, iterations, epsilon):
        o_centroids = centroids
        iterations += 1

        labels = getLabels(dataSet, centroids)

        centroids = findMean(labels)

        diff = sum([distant(centroids[i], o_centroids[i]) for i in range(len(centroids))])
        print('This diff :',diff,'i :', iterations)
    
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
    return np.sqrt(sum((a - b) ** 2))

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
        print(l)
        tmp = [a/l for a in [sum(x) for x in zip(*i)]]
        if tmp == []:
            print('reinitialize centroid')
            tmp = list(np.random.rand(s_attr))
        res.append(tmp)
    return np.asarray(res)

def evalLabels(labels):
    k = len(labels)
    res = []
    for i in labels:
        tmp = []
        for j in i:
            # print(j)
            tmp.append(j[-1:][0])
        res.append(tmp)
    return np.asarray(res)

# # Function: Should Stop
# # -------------
# # Returns True or False if k-means is done. K-means terminates either
# # because it has run a maximum number of iterations OR the centroids
# # stop changing.
# def shouldStop(oldCentroids, centroids, iterations):
#     if iterations > MAX_ITERATIONS: return True
#     return oldCentroids == centroids

# # Function: Get Labels
# # -------------
# # Returns a label for each piece of data in the dataset. 
# def getLabels(dataSet, centroids):
#     # For each element in the dataset, chose the closest centroid. 
#     # Make that centroid the element's label.

# # Function: Get Centroids
# # -------------
# # Returns k random centroids, each of dimension n.
# def getCentroids(dataSet, labels, k):
#     # Each centroid is the geometric mean of the points that
#     # have that centroid's label. Important: If a centroid is empty (no points have
#     # that centroid's label) you should randomly re-initialize it.

if __name__ =='__main__':
    pass