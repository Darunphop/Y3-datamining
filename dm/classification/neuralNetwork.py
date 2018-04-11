import numpy as np

class NeuralNetwork:
    class Node:
        def __init__(self):
            self.input = []
            self.weight = []
            self.output = 0.0
            self.bias = 0.0

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
        
        def process(self, f='sig', type='linear'):  #linear / activation
            out = 0
            if type == 'linear':
                out = self.getSumWeight() + self.bias
            else:
                out = self.activationFunction(self.input, f)
            self.setOutput(out)

        def getInput(self):
            return self.input
        def getOutput(self):
            return self.output
        def getSumWeight(self):
            sum = 0
            for i in range(len(self.input)):
                sum += self.input[i] * self.weight[i]
            return sum

        def setInput(self, n_input):
            self.input = n_input
        def setWeight(self, n_weight):
            self.weight = n_weight
        def setOutput(self, value):
            self.output = value

        # END Node class #

    data = 0
    def __init__(self):
        self.data = 1
    
    # END NeuralNetwork class #

if __name__ == '__main__':
    print('Hi')
    x = NeuralNetwork()
    y = x.Node()
    print(y.activationFunction(3,'sig',2))