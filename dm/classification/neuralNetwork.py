import numpy as np

class NeuralNetwork:
    class Node:
        def __init__(self):
            input = []
            output = 0.0
            bias = 0.0

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


    data = 0
    def __init__(self):
        self.data = 1

if __name__ == '__main__':
    print('Hi')
    x = NeuralNetwork()
    y = x.Node()
    print(y.activationFunction(3,'sig',1))