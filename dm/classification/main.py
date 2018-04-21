import input
import neuralNetwork
import decisionTree as dt
import sys

if __name__ == '__main__':
    raw_data = input.loadFile().sample(frac=1)   #Load and shuffle data
    kf_data = input.kFold(10, raw_data)

    error = []
    for n, i in enumerate(kf_data): #each fold
        if 0 <= n < 10:
            print('%2d   ::   Train size : %d | Test size : %d'%(n+1, len(i[0]), len(i[1])))
            print('%s'%(''.ljust(50,'-')))

            if sys.argv[1] == 'nn': #   Neuron network
                nn = neuralNetwork.NeuralNetwork(len(i[0])-1, 0.01)

                nn.addHidden(21)    #   Hidden layers
                nn.addHidden(18)
                nn.addHidden(15)
                nn.addHidden(13)
                nn.addHidden(10)

                nn.addHidden(21)    #   output layer

                input.normalize(i[0])
                input.normalize(i[1])

                for r in range(20):   # epoch
                    print(r)
                    for j in range(len(i[0])):  #feed each row

                            inp = list(i[0].iloc[j][:-1])
                            expect = i[0].iloc[j][-1:]
                            nn.train(inp, expect)

                success = 0
                for j in range(len(i[1])):  #feed test
                    # if 0 <= j < 5:
                        inp = list(i[1].iloc[j][:-1])
                        expect = i[1].iloc[j][-1:]
                        nn.setInput(inp)
                        nn.allProcess()
                        o = nn.classify()
                        if o == int(expect):
                            success += 1
                # nn.getLayerList()
                t_e = success/float(len(i[1]))
                print("This error :", t_e)
                error.append(t_e)
            
            else:   #Decision tree
                input.normalize(i[0])
                input.normalize(i[1])
                target = [xp for xp in range(21)]
                root = dt.DecisionTree.Node(target)
                root.avaiable_attr = list(i[0])[:-1]
                dt.buildTree(i[0], root, 'G3')
                success = 0
                for j in range(len(i[1])):
                    result = root.classify(i[1].iloc[j])
                    if result == int(i[1].iloc[j]['G3']):
                        success += 1
                t_e = success/float(len(i[1]))
                print("This error :", t_e)
                error.append(t_e)
                

    a_error = sum(error) / 10.0
    print('ERROR is', a_error)
    