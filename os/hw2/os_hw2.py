import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def checkPage(frame, target):
    index = -1
    for i in range(len(frame)):
        if frame[i] == target:
            index = i
            break
    return index

def genReference(length, variety):
    return np.random.choice(variety, length)

def FIFO(frame, i):
    return np.append(frame, i)[1:]

def OPTIMAL(frame, o, reference):
    # print(reference)
    nframe = np.copy(frame)
    tmp = np.full((len(nframe)), len(reference))
    for i in range(len(reference)):
        for j in range(len(nframe)):
            if tmp[j] == len(reference):
                if reference[i] == nframe[j]:
                    tmp[j] = i
    # print(tmp)
    nframe[np.argmax(tmp)] = o
    return nframe

def LRU(frame, o, reference):
    # print('RF', reference)
    nframe = np.copy(frame)
    tmp = np.full((len(nframe)), 0)
    for i in range(len(tmp)):
        if tmp[i] == 0:
            for j in range(len(reference)):
                if nframe[i] == reference[len(reference) - j - 1]:
                    tmp[i] = len(reference) - j - 1
                    break
    # print(tmp)
    nframe[np.argmin(tmp)] = o
    return nframe

def pageFault(frameSize, reference, type=0):
    fault = 0
    frame = np.full((frameSize), -1)
    # print(reference)
    for i in range(len(reference)):
        idx = checkPage(frame, reference[i])
        if(idx == -1):
            fault += 1
            # print("Page fault")
            # print('"',reference[i],'" Incoming | Frame', frame)
            insIdx = checkPage(frame, -1)
            if insIdx == -1:
                if type == 0:
                    frame = FIFO(frame, reference[i])
                elif type == 1:
                    frame = OPTIMAL(frame, reference[i], reference[i:])
                elif type == 2:
                    frame = LRU(frame, reference[i], reference[:i])
            else:
                frame[insIdx] = reference[i]
            # print('Frame ', frame, '\n')
    return fault


if __name__ == '__main__':
    algo = {0: 'FIFO', 1: 'OPTIMAL', 2: 'LRU'}
    variety = {0: 10, 1: 50}
    for exp in range(2):
        plot = []
        res = np.full((3, variety[exp]), 0)
        reference = genReference(100, variety[exp])
        fig = plt.figure()
        ax = fig.gca()
        plt.title('Dataset '+str(exp+1))
        for i in range(3):
            for j in range(variety[exp]):
                res[i][j] = pageFault(j+1, reference, i)
            plot.extend(plt.plot(range(1, variety[exp]+1), res[i], marker='o', label=algo[i]))
        plt.legend(handles =[plot[0], plot[1], plot[2]])
        ax.set_xticks(np.arange(0, variety[exp]+1, variety[exp]/10))
        # ax.set_yticks(np.arange(0, 100+1, 10))
        plt.xlabel('Frame size')
        plt.ylabel('Number of Page faults')
        plt.grid()
        plt.show()
        print(res)