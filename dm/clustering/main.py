import input
import k_mean as km
import numpy as np

if __name__ == '__main__':
    print('hi')
    data = input.loadFile()
    input.normalize(data)
    for i in range(2,21):
        k = i
        avg_r = 3
        sum_p = 0
        for j in range(avg_r):
            final_centroidz, final_labels = km.kmeans(data.values, k)
            p = km.getPurity(final_labels)
            sum_p += p
            print('%sK = %2d (%d) Purity %f'% (''.ljust(5), i, j, p))
        print('K = %2d Average Purity %f\n'% (i, sum_p/avg_r))
