import numpy as np

def kmeans(dataSet, k):
	
    centroids = randomCentroids(dataSet.shape[1], k)
    
    # Initialize book keeping vars.
    iterations = 0
    o_centroids = None
    epsilon = 0.001

    while stopCondition(centroids, o_centroids, iterations):
        pass
    
    return centroids

def randomCentroids(attr, k):
    res = []
    for i in range(k):
        tmp = []
        for j in range(attr):
            tmp.append(np.random.rand())
        res.append(tmp)
    return res

def distant(a, b):
    return np.sqrt(sum((a - b) ** 2))

def stopCondition(n_centroids, o_centroids, iterations, epsilon=0.1, max_it = 1000):
    n_attr = len(n_centroids)
    dif_c = sum([distant(n_centroids[i], o_centroids[i]) for i in range(n_attr)])
    print(dif_c)
    return dif_c > epsilon and iterations < max_it

def getLabels(data, centroids):
    res = [[] for i in range(len(centroids))]
    for i in data:
        min = [1000,-1]
        for nj, j in enumerate(centroids):
            dis = distant(i,j)
            if dis < min[0]:
                min[0] = dis
                min[1] = nj
        res[min[1]].append(i)
    return res

def findMean(labels):
    l = len(labels)
    return [i/l for i in [sum(x) for x in zip(*labels)]]

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