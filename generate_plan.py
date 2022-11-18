import networkx as nx
import pdb
import matplotlib.pyplot as plt
import numpy as np
from generate_positive_steps import gen_pos_steps
from generate_negative_steps import gen_neg_steps

def gen_plan(tree, structure):
    height_map = np.zeros((len(structure[0]), len(structure[0])))
    M = max([len(tree.nodes[node]['list']) for node in tree.nodes()])-1
    for k in range(0, M):
        if k % 2 == 1:
            pos_tree = tree.__class__()
            # for node in tree.nodes():
            #     if len(tree.nodes[node]['list'])>k:
            #         # k-th element exists in the list for this node
            #         # for the k-th element value will define how many nodes to be added
                    # for i in range(0,tree.nodes[node]['list'][k]):
                    #     pos_tree.add_node((node[0], node[1], tree.nodes[node]['list'][i]))
            for node in tree.nodes():
                if len(tree.nodes[node]['list'])>k:
                    pos_tree.add_node((node[0], node[1], tree.nodes[node]['list'][k]))
            pos_tree.graph['root'] = (tree.graph['root'][0], tree.graph['root'][1], 0)
            print("added root", pos_tree.graph['root'])

            for node in tree.nodes():
                if k<len(tree.nodes[node]['list']):
                    if (node[0], node[1], tree.nodes[node]['list'][k]) in pos_tree.nodes():
                        if len(list(tree.predecessors(node)))!=0:
                            for parent in tree.predecessors((node)):
                                    pvalue =[]
                                    for x in tree.nodes[parent]['list']:
                                        if x-1<= tree.nodes[parent]['list'][k]:
                                            pvalue.append(tree.nodes[parent]['list'][k])
                                    parent_v = (parent[0], parent[1], min(pvalue))
                                    pos_tree.add_edge(parent_v, (node[0], node[1], tree.nodes[node]['list'][k]))    
                        elif node!=tree.graph['root']:
                            if k<len(tree.nodes[node]['list']):
                                pos_tree.add_edge((node[0], node[1], tree.nodes[node]['list'][k]), pos_tree.graph['root'])
                                # print("added edge with parent", pos_tree.graph['root'], "to node", node)
            nx.draw(pos_tree, with_labels=True)
            plt.show()
            #gen_pos_steps(pos_tree, pos_tree.graph['root'], k, height_map)
            pos_tree.clear()
            
        else:
            neg_tree = tree.__class__()
            # for node in tree.nodes():
            #     if len(tree.nodes[node]['list'])>k:
            #         # k-th element exists in the list for this node
            #         # for the k-th element value will define how many nodes to be added
            #         for i in range(tree.nodes[node]['list'][k-1],tree.nodes[node]['list'][k]):
            #             neg_tree.add_node((node[0], node[1], tree.nodes[node]['list'][i]))
            for node in tree.nodes():
                if len(tree.nodes[node]['list'])>k:
                    neg_tree.add_node((node[0], node[1], tree.nodes[node]['list'][k]))
            neg_tree.graph['root'] = (tree.graph['root'][0], tree.graph['root'][1], 0)
            # print("added root", neg_tree.graph['root'])

            for node in tree.nodes():
                if k<len(tree.nodes[node]['list']):
                    if (node[0], node[1], tree.nodes[node]['list'][k]) in neg_tree.nodes():
                        
                        if len(list(tree.predecessors(node)))!=0:
                            for parent in tree.predecessors((node)):
                                    pvalue =[]
                                    for x in tree.nodes[parent]['list']:
                                        if x >= tree.nodes[parent]['list'][k]:
                                            pvalue.append(tree.nodes[parent]['list'][k])
                                    parent_v = (parent[0], parent[1], max(pvalue))
                                    neg_tree.add_edge(parent_v, (node[0], node[1], tree.nodes[node]['list'][k]))
                        
                        elif node!=tree.graph['root']:
                            if k<len(tree.nodes[node]['list']):
                                neg_tree.add_edge((node[0], node[1], tree.nodes[node]['list'][k]), neg_tree.graph['root'])
                                # print("added edge with parent", neg_tree.graph['root'], "to node", node)
            nx.draw(neg_tree, with_labels=True)
            plt.show()
            #gen_neg_steps(neg_tree, neg_tree.graph['root'], k, height_map)
            neg_tree.clear()
            
    return tree