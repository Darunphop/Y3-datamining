import numpy as np

class NeuralNetwork:
    class Layer:
        def __init__(self, s, input):
                self.size = s
                self.input = []
                self.nodes = []

        def setupNodes(self):
            for i in range(self.size):
                i_size = len(self.input)
                tmpNode = self.LinearNode(self.input, self.getRandW(i_size), self.getRandBias(i_size))
                self.nodes.append(tmpNode)


        def getRandW(self, size):
            return 2 * np.random.random(size) - 1   #[-1,1]
        def getRandBias(self, size):
            return np.random.random(size)   #[0,1]

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
                for i in range(len(self.input)):
                    sum += self.input[i] * self.weight[i]
                return sum
            def setWeight(self, n_weight):
                if len(n_weight) == len(self.input):
                    self.weight = n_weight
                else:
                    raise ValueError('Weigths size not match the Input size')

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

    data = 0
    def __init__(self):
        self.data = 1
    
    # END NeuralNetwork class #

if __name__ == '__main__':
    print('Hi')
    z = NeuralNetwork()
    x = z.Layer(1,1)
    i = [1, 2, 3, 4]
    w = [-0.1, 0.3, -0.5, 0.1]
    b = 0.4
    n = x.LinearNode(i,w,b)
    n.process()
    print(n.getOutput())
    n1 = x.ActivationNode(n.getOutput(), 'sig')
    n1.process()
    print(n1.getOutput())