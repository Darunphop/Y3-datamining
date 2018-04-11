import numpy as np

class NeuralNetwork:
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
            self.weight = n_w
            self.bias = n_b
            super().__init__(n_input)

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
            super().process(self.activationFunction(self.getInput()[0], self.func))
         # END ActivationNode class #

    data = 0
    def __init__(self):
        self.data = 1
    
    # END NeuralNetwork class #

if __name__ == '__main__':
    print('Hi')
    x = NeuralNetwork()
    i = [1, 2, 3, 4]
    w = [-0.1, 0.3, -0.5, 0.1]
    b = 0.5
    n = x.LinearNode(i,w,b)
    n.process()
    print(n.getOutput())
    # y = x.ActivationNode()
    # print(y.activationFunction(3,'sig',2))