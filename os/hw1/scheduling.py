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

def toRangeList(data):
    result = []
    startT = 0
    endT = 0
    for i in range(0,len(data)):
        endT = startT + data[i][1]
        result.append([data[i][0], startT, endT, data[i][1]])
        startT = endT
    return result

def algoFCFS(data):
    return toRangeList(data)

def algoSJF(data):
    return toRangeList(sorted(data, key=lambda x: x[1]))

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
    return toRangeList(result)

def eachDelayTime(data):
    n = 0
    mask = np.zeros((len(data),), dtype=int)
    for i in range(0,len(data)):
        if mask[data[i][0]-1] == 0:
            n += 1
            mask[data[i][0]-1] = 1
    index = []
    for i in range(0,n):
        index.append([])
    for i in range(0,len(data)):
        tmp = [data[i][1], data[i][2]]
        index[data[i][0]-1].append(tmp)
    return index

def delayTime(data,qt=0):
    n = 0
    sum = 0
    mask = np.zeros((len(data),), dtype=int)
    for i in range(0,len(data)):
        sum += data[i][1] - mask[data[i][0]-1]
        # print( str(sum)+" ="+str(data[i][1])+" - "+str(mask[data[i][0]-1]))
        if mask[data[i][0]-1] == 0:
            n += 1
        mask[data[i][0]-1] += qt
    # print(mask)
    return float(sum) / n

if __name__ == "__main__":
    testSetRatio = []
    testSetRatio.append([15,30,15]) #test set 1
    # testSetRatio.append([30, 0,30])  #test set 2
    # testSetRatio.append([40,15,5]) #test set 3
    RRqt = []
    RRqt.append(5)
    # RRqt.append(10)
    # RRqt.append(20)

    for i in testSetRatio:
        test = testSetGen(i)
        # print(eachDelayTime(algoFCFS(test)))
        # print(delayTime(algoFCFS(test)))
        print("++++++++++++++++++++++++++")
        # print(algoRR(test))
        # print(delayTime(algoSJF(test)))
        print("--------------------------")
        # print(test)
        for i in RRqt:
            print(eachDelayTime(algoRR(test)))
            # print(delayTime(algoRR(test),i))
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^")