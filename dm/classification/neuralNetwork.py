import numpy as np
import copy as cp

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
            else:
                for i in range(self.size):
                    tmp_node = self.ActivationNode(self.getInput()[i], 'sig')
                    self.nodes.append(tmp_node)

        def process(self):
            tmp = []
            for n, i in enumerate(self.nodes):
                if self.type == 'fully':
                    i.setInput(self.getInput())
                else:
                    i.setInput(self.getInput()[n])
                i.process()
                tmp_out = i.getOutput()
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
            return 1 * np.random.random(size) - 0   #(-1,1)
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
                
            def applyW(self, delta):
                # print('DELTA ', len(delta))
                # print('W ', len(self.weight))
                
                w_tmp = []
                for n, i in enumerate(delta):
                    # tmp = []
                    dump = self.weight[n]
                    # print('Before', self.weight[n])
                    dump += i
                    # print('applying ', i)
                    # print('After', self.weight[n])
                    w_tmp.append(dump)
                # print('New tmp',w_tmp)
                self.weight = w_tmp

            def getSumWeight(self):
                sum = 0
                for i in range(len(self.input)):
                    sum += self.input[i] * self.weight[i]
                return sum
            def setWeight(self, n_weight):
                if len(n_weight) == len(self.input):
                    self.weight = n_weight
                else:
                    raise ValueError('Weigths size not match the Input size')

            def getWeight(self):
                return self.weight

            def process(self):
                sumwb = self.getSumWeight() + self.bias
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
                fx = self.activationFunction(self.getInput(), self.func)
                super().process(fx)
            # END ActivationNode class #

    def __init__(self, n, lr=0.5):
        self.input = np.full(n, 0)
        self.layers = []
        self.learning_rate = lr
    
    def addHidden(self, n):
        layer_size = len(self.layers)
        ip = []
        if layer_size == 0:
            ip = self.input
        else:
            ip = self.layers[layer_size-1].getOutput()
        self.addLinearLayer(n, ip)
        ip = self.layers[layer_size].getOutput()
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
        self.input = input
        if size != 0:
            self.layers[0].input = input

    def getLayerList(self):
        for i in self.layers:
            print('%6s | %d Nodes'%(i.type, i.size))
            for j in i.nodes:
                # print('%sInput :%s'%(''.ljust(7), j.input))
                try:
                    print('%sWeight :%s'%(''.ljust(9), j.weight))
                    print('\n')
                    print('%sBias :%s'%(''.ljust(9), j.bias))
                except:
                    pass
                # print('%sOutput :%s'%(''.ljust(11), j.output))
            print('\n')
    def getInput(self):
        return self.input
    def getOutput(self):
        return self.layers[-1:][0].getOutput()

    def allProcess(self, v=False):
        if v:
            print('\nBegin All process----------')
        interm = []
        for n, i in enumerate(self.layers):
            if v:
                print('Begin New Layer')
            if n != 0:
                i.setInput(interm)
            interm = i.process()
        if v:
            print('End All process----------\n')

    def classify(self):
        return np.argmax(self.getOutput())

    def train(self, input, expect):
        self.setInput(input)
        self.allProcess()
        exp = self.classGen(int(expect),len(self.layers[-1:][0].getOutput()))
        grad = []
        o = []
        for n, i in enumerate(reversed(self.layers)):   #find gradiant
            if n % 2 == 0:
                ot = i.getOutput()
                for j in ot:
                    o.append([j, i.nodes[0].activationFunction(j,order=1)])
                continue
            g_tmp = []
            for nj, j in enumerate(i.nodes):
                dedn = 0
                if n == 1:
                    dedn = o[nj][0] - exp[nj]
                else:
                    sum = 0
                    for nk, k in enumerate(grad[-1:][0]):
                        sum += k* self.layers[(len(self.layers)-1)-(n-2)].nodes[nk].getWeight()[nj]
                    dedn = sum
                g_tmp.append(dedn*o[nj][1])
            grad.append(g_tmp)
            o = []

        o = []
        for n, i in enumerate(reversed(self.layers)):   #apply weight
            count = 0

            if n % 2 == 0:
                o = i.getOutput()
                continue
            else:
                for nj, j in enumerate(i.nodes):
                    delta = []
                    for nx, x in enumerate(j.weight):
                        a = grad[count][nj]
                        b = o[nj]
                        dt = 0 - self.learning_rate * a * b
                        delta.append(dt)
                    j.applyW(delta)
                    j.bias = j.bias - self.learning_rate * grad[count][nj] * j.bias
                count += 1
        self.allProcess()


                
        return 0
    
    def classGen(self, out, size):
        t = np.full(size, 0)
        t[out] = 1
        return t

    # END NeuralNetwork class #

if __name__ == '__main__':
    print('Hi')
    z = NeuralNetwork(5,0.5)
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