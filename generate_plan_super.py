import networkx as nx
import numpy as np
import pdb
import matplotlib.pyplot as plt
from generate_negative_steps import gen_neg_steps
from generate_positive_steps import gen_pos_steps

def gen_plan(tree, structure):
    M = max([len(tree.nodes[node]['list']) for node in tree.nodes()])-1
    neg_counter = 0
    pos_counter = 0
    
    steps = []
    print(steps, "steps initialized")
    for k in range(0, M+1):
        # all operations are on the k-th element thus k-1-th  interval
        super_event_tree = tree.__class__()
        super_event_tree.graph['root'] = tree.graph['root']
        if k%2==1:
            for node in tree.nodes():
                if len(tree.nodes[node]['list'])>k:
                    super_event_tree.add_node((node[0], node[1]))
                    for parent in tree.predecessors(node):
                        if len(tree.nodes[parent]['list'])>k:
                            super_event_tree.add_edge((parent[0], parent[1]), (node[0], node[1]))    
                        # else: 
                        #     print(node, tree.nodes[node]['list'], parent, tree.nodes[parent]['list'])
                        #     pdb.set_trace()
                    super_event_tree.nodes[(node[0], node[1])]['list'] = [0]
                    for i in range(1, tree.nodes[node]['list'][k]+1):
                        super_event_tree.nodes[(node[0], node[1])]['list'].append(i)
            # print(steps, "steps")
            steps = build_pos_tree(super_event_tree, pos_counter, steps)

        elif k!=0:
            for node in tree.nodes():
                if len(tree.nodes[node]['list'])>k:
                    super_event_tree.add_node((node[0], node[1]))
                    for parent in tree.predecessors(node):
                        if len(tree.nodes[parent]['list'])>k:
                            super_event_tree.add_edge((parent[0], parent[1]), (node[0], node[1]))    
                        # else: 
                        #     print(node, tree.nodes[node]['list'], parent, tree.nodes[parent]['list'])
                        #     pdb.set_trace()
                    super_event_tree.nodes[(node[0], node[1])]['list'] = [0]
                    for i in range(1, tree.nodes[node]['list'][k-1]+1):
                        super_event_tree.nodes[(node[0], node[1])]['list'].append(i)
            # print(steps, "steps")
            steps = build_neg_tree(super_event_tree, neg_counter, steps)
    return steps


def build_pos_tree(super_tree ,pos_counter, steps):    
    event_tree = super_tree.__class__()
    event_tree.graph['root'] = (super_tree.graph['root'][0], super_tree.graph['root'][1], 0)
    for node in super_tree.nodes():
        for i in range(0, len(super_tree.nodes[node]['list'])):
            event_tree.add_node((node[0], node[1], i))
            for parent in super_tree.predecessors(node):
                if i==0:
                    event_tree.add_edge((parent[0], parent[1], 0), (node[0], node[1], 0))
                else:
                    event_tree.add_edge((parent[0], parent[1], i-1), (node[0], node[1], i))
    # print(steps, "steps")
    steps = gen_pos_steps(event_tree, event_tree.graph['root'], super_tree, steps)
    #return pos_counter
    # nx.draw(event_tree, with_labels=True)
    # plt.show()
    return steps

def build_neg_tree(super_tree, neg_counter, steps):
    event_tree = super_tree.__class__()
    event_tree.graph['root'] = (super_tree.graph['root'][0], super_tree.graph['root'][1], 0)
    for node in super_tree.nodes():
        for i in range(0, len(super_tree.nodes[node]['list'])):
            event_tree.add_node((node[0], node[1], i))
            for parent in super_tree.predecessors(node):
                if i==len(super_tree.nodes[parent]['list']):
                    event_tree.add_edge((parent[0], parent[1], i-1), (node[0], node[1], i))
                else:
                    event_tree.add_edge((parent[0], parent[1], i), (node[0], node[1], i))
    # print(steps, "steps")
    steps = gen_neg_steps(event_tree, event_tree.graph['root'], super_tree, steps)
    # return neg_counter
    # nx.draw(event_tree, with_labels=True)
    # plt.show()
    return steps