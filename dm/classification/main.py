import input
import neuralNetwork

if __name__ == '__main__':
    raw_data = input.loadFile().sample(frac=1)   #Load and shuffle data
    kf_data = input.kFold(10, raw_data)
    # print(len(kf_data))
    for n, i in enumerate(kf_data):
        print('%2d   ::   Train size : %d | Test size : %d'%(n+1, len(i[0]), len(i[1])))
        print('%s'%(''.ljust(50,'-')))