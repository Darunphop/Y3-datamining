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
    
def buildTree(data, root, attr):
    node = DecisionTree.Node(root)
    if len(node.target) <= 1:
        return node
    else:
        print(root)
        m_p = findMid(data, attr)
        l_t = root[:m_p+1]
        r_t = root[m_p-1:]
        print(l_t, r_t)
        # df.loc[df['column_name'] == some_value]
        data.loc[data['G3'] <= l_t[-1:][0]]
if __name__ == '__main__':
    print('HI')