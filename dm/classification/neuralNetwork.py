import numpy as np

class NeuralNetwork:
    class Layer:
        def __init__(self, s, input, type='fully'):
                self.size = s
                self.input = input
                self.nodes = []
                self.output = []
                self.type = type   # fully / direct
                self.setupNodes()

        def setupNodes(self):
            if self.type == 'fully':
                for i in range(self.size):
                    i_size = len(self.getInput())
                    rand_w = self.getRandW(i_size)
                    rand_b = self.getRandBias()
                    # print('rand_w', rand_w)
                    # print('rand_b', rand_b)
                    tmp_node = self.LinearNode(self.getInput(), rand_w, rand_b)
                    self.nodes.append(tmp_node)
                    # print('Added fully node Successful')
            else:
                for i in range(self.size):
                    # print(self.getInput()[i])
                    tmp_node = self.ActivationNode(self.getInput()[i], 'sig')
                    self.nodes.append(tmp_node)
                    # print('Added Direct successful')
            # print('setup', self.input)

        def process(self):
            tmp = []
            for n, i in enumerate(self.nodes):
                if self.type == 'fully':
                    # print('ib layer process', self.getInput())
                    i.setInput(self.getInput())
                else:
                    # print(self.getInput()[n])
                    i.setInput(self.getInput()[n])
                i.process()
                tmp_out = i.getOutput()
                # print('i.input',i.input)
                # print('in layer process', tmp_out)
                tmp.append(tmp_out)
            self.output = tmp
            return tmp

        def getInput(self):
            if self.input[0].__class__ == list:
                ip = self.input[0]
            else:
                ip = self.input
            return ip
        def getOutput(self):
            return self.output
        def getRandW(self, size):
            return 4 * np.random.random(size) - 2   #(-2,2)
        def getRandBias(self, size=1):
            return 2 * np.random.random(size) - 1   #(-1,1)

        def setInput(self, input):
            self.input = input

        class Node:
            def __init__(self, n_input=[]):
                self.input = n_input
                self.output = 0.0
            
            def process(self, out):
                self.setOutput(out)

            def getInput(self):
                return self.input
            def getOutput(self):
                return self.output

            def setInput(self, n_input):
                self.input = n_input
            def setOutput(self, value):
                self.output = value

            # END Node class #

        class LinearNode(Node):
            def __init__(self, n_input=[], n_w=[], n_b=0):
                super().__init__(n_input)
                self.setWeight(n_w)
                self.bias = n_b
                

            def getSumWeight(self):
                sum = 0
                # print('W',self.weight)
                for i in range(len(self.input)):
                    # print(i)
                    # print('In getSumW', self.input[i])
                    # print('In getSumW', self.weight[i])
                    sum += self.input[i] * self.weight[i]
                # print('SUM is', sum)
                return sum
            def setWeight(self, n_weight):
                if len(n_weight) == len(self.input):
                    self.weight = n_weight
                else:
                    raise ValueError('Weigths size not match the Input size')

            def process(self):
                # print('In node BIAS', self.bias)
                # print('In node W', self.getSumWeight())
                # print('process bias', self.bias)
                sumwb = self.getSumWeight() + self.bias
                # print('sum inprocess is', sumwb)
                super().process(sumwb)
            # END LinearNode class #

        class ActivationNode(Node):
            def __init__(self, n_input=[], f='sig'):
                self.func = f 
                super().__init__(n_input)
                
            def activationFunction(self, input, f='sig', order=0):
                if order == 0:
                    if f == 'sig':  #sigmoid
                        return 1.0/(1+np.exp(0-input))
                    else:   #tanh
                        return np.tanh(input)
                else:
                    if f == 'sig':
                        fx = self.activationFunction(input,f,order-1)
                        return fx * (1 - fx)
                    else:
                        fx = self.activationFunction(input,f,order-1)
                        return 1 - np.power(fx, 2)
            
            def process(self):
                # print('In activate',self.getInput())
                fx = self.activationFunction(self.getInput(), self.func)
                super().process(fx)
            # END ActivationNode class #

    def __init__(self, n):
        self.input = np.full(n, 0)
        self.layers = []
    
    def addHidden(self, n):
        layer_size = len(self.layers)
        ip = []
        if layer_size == 0:
            ip = self.input
        else:
            ip = self.layers[layer_size-1].getOutput()
        self.addLinearLayer(n, ip)
        ip = self.layers[layer_size].getOutput()
        # print('IP ',ip)
        self.addActivationLayer(n, ip)
        self.allProcess()

    def addLinearLayer(self, n, input):
        tmp_layer = self.Layer(n, input)
        tmp_layer.process()
        self.layers.append(tmp_layer)
    
    def addActivationLayer(self, n, input):
        tmp_layer = self.Layer(n, input, 'direct')
        tmp_layer.process
        self.layers.append(tmp_layer)

    def setInput(self, input):
        size = len(self.layers)
        print('Old input :', self.getInput())
        self.input = input
        if size != 0:
            self.layers[0].input = input
        print('New input :', self.getInput())

    def getLayerList(self):
        for i in self.layers:
            print('%6s | %d Nodes'%(i.type, i.size))
            for j in i.nodes:
                print('%sInput :%s'%(''.ljust(7), j.input))
                print('%sOutput :%s'%(''.ljust(10), j.output))
            print('\n')
    def getInput(self):
        return self.input
    def getOutput(self):
        return self.layers[-1:][0].getOutput()

    def allProcess(self):
        print('\nBegin All process----------')
        interm = []
        for n, i in enumerate(self.layers):
            print('Begin New Layer')
            if n != 0:
                i.setInput(interm)
            interm = i.process()
        print('End All process----------\n')

    # END NeuralNetwork class #

if __name__ == '__main__':
    print('Hi')
    z = NeuralNetwork(5)
    # ip = [[1,1],[2,1],[4,0],[2,1],[5,5]]
    ip = [0.01,0.39,0.41,0.22,0.6]
    z.addHidden(5)
    z.addHidden(4)
    z.addHidden(3)
    z.getLayerList()
    z.allProcess()
    print(z.getOutput())
    z.setInput(ip)
    z.allProcess()
    z.getLayerList()
    print(z.getOutput())