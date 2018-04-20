import numpy as np
import math
import copy as cp

class DecisionTree:

    class Node:
        def __init__(self, target):
            self.target = target
            self.child = []
            self.attr = ''
            self.avaiable_attr = []
            self.theshold = 0

        def classify(self, input):
            if len(self.target) == 1:
                # print(self.target[0])
                return self.target[0]
            else:
                o = input[self.attr]
                if o <= self.theshold:
                    # print('Go l')
                    return self.child[0].classify(input)
                else:
                    # print('Go r')
                    return self.child[1].classify(input)
    #   END Node
    def __init__(self, target):
        self.tree = []


#   END DecisionTree

def findMid(data, attr):
    # agg = data.groupby([attr]).size()
    agg = data.sort_values(by=[attr])
    # print(agg[attr].max())
    mid = (agg[attr].max() - agg[attr].min())/2
    return mid

    
def buildTree(data, root, attr, count=1 ):
    root_node = root
    if len(root_node.target) <= 1:
        # return root_node
        # print('Met leaf', root_node.target[0])
        pass
    else:
        # print(root_node.target)
        m_p = len(root_node.target) / 2
        l_t = root_node.target[:math.floor(m_p)]
        r_t = root_node.target[math.floor(m_p):]
        # print('after main node split :',l_t, r_t)
        # df.loc[df['column_name'] == some_value]
        d_l = data.loc[data['G3'] <= l_t[-1:][0]]
        d_r = data.loc[data['G3'] >  l_t[-1:][0]]
        d_ls = len(d_l)
        d_rs = len(d_r)
        info = getInfo(d_ls, d_rs)
        # print(info)
        attr_info = []
        g_info = []
        for i in root_node.avaiable_attr:
            x, y = attrInfoGain(i, 'G3', data, d_l, d_r)
            attr_info.append(x)
            g_info.append(y)
        # print(attr_info)
        gain = np.full(len(attr_info), info) - attr_info
        # print(gain)
        max = [0,0]
        for n, i in enumerate(gain):
            tmp = i/g_info[n]
            if tmp > max[0]:
                max = [tmp, n]
        # print(max)
        root_node.attr = root_node.avaiable_attr.pop(max[1])
        root_node.theshold = findMid(data, root_node.attr)
        # print(root_node.attr)
        # print(root_node.avaiable_attr)
        if count == 0:
            l_node = DecisionTree.Node(l_t)
            r_node = DecisionTree.Node(r_t)
        else:
            l_node = DecisionTree.Node(root_node.target)
            r_node = DecisionTree.Node(root_node.target)
        l_node.avaiable_attr = cp.copy(root_node.avaiable_attr)
        r_node.avaiable_attr = cp.copy(root_node.avaiable_attr)

        # print(root_node.attr)
        # print(root_node.theshold)

        root_node.child.append(l_node)
        root_node.child.append(r_node)

        # print('l_node', l_node.target)
        # print('r_node', r_node.target)
        if count == 0:
            buildTree(data, l_node, 'G3')
            buildTree(data, r_node, 'G3')
        else:
            buildTree(data, l_node, 'G3', count-1)
            buildTree(data, r_node, 'G3', count-1)

        



def getInfo(ai, bi):
    a = ai + 1
    b = bi + 1
    s = a+b
    return (-(a/s)*math.log2(a/s)) - (b/s)*math.log2(b/s)

def attrInfoGain(s_attr, o_attr, data, d_l, d_r):
    t_l = d_l[[s_attr, o_attr]]
    t_r = d_r[[s_attr, o_attr]]
    mp = findMid(data, s_attr)
    # print(mp, s_attr)
    l_p = len(t_l.loc[t_l[s_attr] <= mp])
    l_n = len(t_l.loc[t_l[s_attr] >  mp])
    r_p = len(t_r.loc[t_r[s_attr] <= mp])
    r_n = len(t_r.loc[t_r[s_attr] >  mp])
    # print(l_p, l_n, r_p, r_n)
    sum = l_p + l_n + r_p + r_n
    return ((l_p+l_n)/sum) * (getInfo(l_p, l_n)) + ((r_p+r_n)/sum) * (getInfo(r_p, r_n)), getInfo(l_p, r_p)

if __name__ == '__main__':
    print('HI')