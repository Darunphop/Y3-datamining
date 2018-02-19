import numpy as np

testSeed = [[1,10], [15,25], [30,40]]

def testSetGen(ratio):
    result = []
    tmp = []
    for i in range(0,len(ratio)):
        tmp.extend(np.random.random_integers(testSeed[i][0], testSeed[i][1],ratio[i]))
    np.random.shuffle(tmp)
    for i in range(1,len(tmp)+1):
        result.append([i,tmp[i-1]])
    return result

def algoFCFS(data):
    result = []
    startT = 0
    endT = 0
    for i in range(0,len(data)):
        endT = startT + data[i][1]
        result.append([data[i][0], startT, endT, data[i][1]])
        startT = endT
    return result

def algoSJF(data):
    return sorted(data, key=lambda x: x[1])

def algoRR(data,qtime=10):
    pending = []
    result = []
    for i in data:
        if i[1] <= qtime:
            result.append(i)
        else:
            pending.append([i[0], i[1]-qtime])
            result.append([i[0], qtime])
    while len(pending) > 0:
        x = pending.pop(0)
        if x[1] <= qtime:
            result.append(x)
        else:
            pending.append([x[0], x[1]-qtime])
            result.append([x[0], qtime])
    return result

def eachDelayTime(data):
    result = {}
    for i in range(0,len(data)):
        if data[i][0] in result:
            result.update({data[i][0]: result[data[i][0]] + data[i][1]})
        else:
            result.update({data[i][0]: data[i][1]})
    return result

if __name__ == "__main__":
    testSetRatio = []
    testSetRatio.append([20,20,20]) #test set 1
    # testSetRatio.append([30, 0,30])  #test set 2
    # testSetRatio.append([20,20,20]) #test set 3

    for i in testSetRatio:
        test = testSetGen(i)
        # print(eachDelayTime(algoFCFS(test)))
        print("++++++++++++++++++++++++++")
        print(algoFCFS(test))
        print("--------------------------")
        print(test)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^")