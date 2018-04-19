import numpy as np

class DecisionTree:

    class Node:
        def __init__(self, target):
            self.target = target
            self.child = []
            self.attr = ''
            self.avaiable_attr = []
            self.theshold = 0

    #   END Node
    def __init__(self, target):
        self.tree = []

#   END DecisionTree

def findMid(data, attr):
    agg = data.groupby([attr]).size()
    sum_agg = sum(agg)
    mid = sum_agg/2
    for n, i in enumerate(agg):
        # print(n,i)
        mid -= i
        if mid <= 0:
            return n
    
def buildTree(data, root):
    node = DecisionTree.Node(root)
    if len(node.root) <= 1:
        return node
    else:
        
if __name__ == '__main__':
    print('HI')