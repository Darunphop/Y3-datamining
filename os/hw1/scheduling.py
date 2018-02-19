import numpy as np

testSeed = [[1,10], [15,25], [30,40]]

def testSetGen(ratio):
    result = []
    for i in range(0,len(ratio)):
        # print()
        result.extend(np.random.random_integers(testSeed[i][0], testSeed[i][1],ratio[i]))
    return result

if __name__ == "__main__":
    print(testSetGen([2,3,4]))