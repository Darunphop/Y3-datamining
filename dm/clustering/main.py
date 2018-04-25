import input
import k_mean as km
import numpy as np

if __name__ == '__main__':
    data = input.loadFile()             #   dataset loading
    input.normalize(data)               #   normalize dataset
    for i in range(2,21):               #   Loop k from 2 - 20
        k = i
        avg_r = 3                       #   set repeating step
        sum_p = 0
        for j in range(1, avg_r+1):     #   loop for avr_r round
            final_centroidz, final_labels = km.kmeans(data.values, k)
                                        #   get the final centroid points -
                                        #   and final set of clusterd data

            p = km.getPurity(final_labels)
                                        #   calculate the purity
            sum_p += p
            print('%sK = %2d (%d) Purity %f'% (''.ljust(5), i, j, p))
        print('K = %2d Average Purity %f\n'% (i, sum_p/avg_r))
                                        #   show final purity for each k
