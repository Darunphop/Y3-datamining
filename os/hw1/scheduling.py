import numpy as np

testSeed = [[1,10], [15,25], [30,40]]

def testSetGen(ratio):
    result = []
    for i in range(0,len(ratio)):
        result.extend(np.random.random_integers(testSeed[i][0], testSeed[i][1],ratio[i]))
    np.random.shuffle(result)
    return result

def algoFCFS(data):
    return data #suppose data is index by time

if __name__ == "__main__":
    testSetRatio = []
    testSetRatio.append([20,20,20]) #test set 1
    testSetRatio.append([30, 0,30])  #test set 2
    testSetRatio.append([20,20,20]) #test set 3

    for i in testSetRatio:
        print(testSetGen(i))