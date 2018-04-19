import input
import neuralNetwork

if __name__ == '__main__':
    raw_data = input.loadFile().sample(frac=1)   #Load and shuffle data
    kf_data = input.kFold(10, raw_data)
    # print(len(kf_data))
    for n, i in enumerate(kf_data): #each fold
        if 0 <= n < 1:
            print('%2d   ::   Train size : %d | Test size : %d'%(n+1, len(i[0]), len(i[1])))
            print('%s'%(''.ljust(50,'-')))

            nn = neuralNetwork.NeuralNetwork(len(i[0])-1)
            # nn.addHidden(10)
            nn.addHidden(5)
            nn.addHidden(2)
            nn.addHidden(21)
            # nn.getLayerList()
            # o = nn.getOutput()
            # print(o)

            input.normalize(i[0])
            for j in range(len(i[0])):  #feed each row
                if 0 <= j < 1:
                    inp = list(i[0].iloc[j][:-1])
                    expect = i[0].iloc[j][-1:]
                    nn.train(inp, expect)
                    # nn.getLayerList()
                    # o = nn.getOutput()
                    # o = nn.classify()
                    # print(o)
                    # print(inp)
                    # print(j)