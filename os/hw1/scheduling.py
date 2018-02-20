import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

testSeed = [[1,10], [15,25], [30,40]]
figc = 0

def testSetGen(ratio):
    result = []
    tmp = []
    for i in range(0,len(ratio)):
        tmp.extend(np.random.random_integers(testSeed[i][0], testSeed[i][1],ratio[i]))
    np.random.shuffle(tmp)
    for i in range(1,len(tmp)+1):
        result.append([i,tmp[i-1]])
    return result, tmp

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

def delayTime(data):
    x = []
    for i in data:
        tmp = i[0][0]
        for j in range(1,len(i)):
            tmp += i[j][0] - i[j-1][1]
        x.append(tmp)
    return float(sum(x)) / len(data)

def dataPlot(data):
    global figc
    
    for i in range(0,len(data)):
        fig = plt.figure(figc)
        ax = fig.add_subplot(111)
        ax.set_title('Test set %d'% (i+1))
        sns.kdeplot(data[i][0],shade=True)
        figc += 1

    for i in range(0,len(data)):
        color_set = ['#4480e2','#c244e2','#61c41f','#61c41f','#61c41f']
        x = [u'First Come First Serve', u'Short Job First', u'Round Robin\nQT = 5', u'Round Robin\nQT = 10', u'Round Robin\nQT = 20']
        y = data[i][1:3]
        y.extend(data[i][3])
        print(y)
        fig, ax = plt.subplots()    
        width = 0.50 # the width of the bars 
        ind = np.arange(len(y))  # the x locations for the groups
        barlist = ax.barh(ind, y, width, color="blue")
        ax.set_yticks((ind+width/2)-(.25))
        ax.set_yticklabels(x, minor=False)
        ax.set_xlim(0,max(y)+150)
        for j in range(0,len(barlist)):
            barlist[j].set_color(color_set[j])
        plt.title('Data set %d'% (i+1))
        plt.xlabel('Average waiting time(ms)')
        plt.ylabel('y')
        for i, v in enumerate(y):
            ax.text(v + 3, i - 0.1, str(round(v,4)), color='#211f18', fontweight='light')
    return

if __name__ == "__main__":
    testSetRatio = []
    testSetRatio.append([15,30,15]) #test set 1
    testSetRatio.append([30, 0,30]) #test set 2
    testSetRatio.append([40,15,5])  #test set 3
    RRqt = []
    RRqt.append(5)
    RRqt.append(10)
    RRqt.append(20)
    result = []
    o = 0
    for i in testSetRatio:
        test, dataset = testSetGen(i)
        print('[Dataset]')
        s = '[' + ', '.join(str(e[1]) for e in test) + ']'
        print(s)

        print('\nFirst Come First Serve Algorithm')
        x = delayTime(eachDelayTime(algoFCFS(test)))
        print('Average waiting time = %.4f'% x)
        print("++++++++++++++++++++++++++")
        print('\nShort Job First Algorithm')
        y = delayTime(eachDelayTime(algoSJF(test)))
        print('Average waiting time = %.4f'% y)
        print("--------------------------")
        print('\nRound Robin Algorithm')
        z = []
        for j in range(0,len(RRqt)):
            z.append(delayTime(eachDelayTime(algoRR(test,RRqt[j]))))
            print('Average waiting time (QT = %2d) = %.4f'%  (RRqt[j], z[j]))
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
        result.append([dataset,x,y,z])
        o += 1
    
    dataPlot(result)
    plt.show()