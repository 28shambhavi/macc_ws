import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from compute_ws import compute_ws
from build_all_lists import build_all_lists
from generate_plan_super import gen_plan
from construct_list import cons_list
from utils import *
from multi_agent import *
import pdb
import time

def main():
    start_time = time.time()
    structure = [[0,0,	0,	0,	0,	0,	0,	0,	0,	0,	0],	
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],	
                [0,	0,	0,	4,	0,	0,	5,	0,	0,	0,	0],	
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],	
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],	
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],	
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0]]
    
    # structure = np.zeros((7,7))
    # structure = [[0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0]]

    # structure = [[0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,3,3,3,0,0,0],
    #             [0,0,0,0,3,3,3,0,0,0],
    #             [0,0,0,0,3,3,3,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0]]

    # structure = [[0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,3,0,0,0,0,3,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,3,0,0,0,0,3,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0]]
    
    # structure = [[0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,1,1,1,1,1,1,0,0],
    #             [0,0,1,2,2,2,2,1,0,0],
    #             [0,0,1,2,3,3,2,1,0,0],
    #             [0,0,1,2,3,3,2,1,0,0],
    #             [0,0,1,2,2,2,2,1,0,0],
    #             [0,0,1,1,1,1,1,1,0,0],
    #             [0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0]]

    edge_list = get_spanning_tree(structure)
    tree = nx.DiGraph()
    tree.graph['root'] = (len(structure),len(structure[0]))
    tree.add_edges_from(edge_list)
    visited_edges = []
    node_queue = []
    node_queue.append(tree.graph['root'])
    di_tree = tree.__class__()
    di_tree.add_nodes_from(tree)
    di_tree.add_edges_from(tree.edges)
    di_tree.graph['root'] = tree.graph['root']
    for e in tree.edges():
        if e not in visited_edges:
            visited_edges, node_queue = flip_edge(e, di_tree, visited_edges, node_queue)
            for n in node_queue:
                for e_ in tree.edges(n):
                    if e_ not in visited_edges and e_ in di_tree.edges():
                        visited_edges, node_queue = flip_edge(e_, di_tree, visited_edges, node_queue)
    
    marked_tree = build_all_lists(di_tree, structure)
    con_tree = cons_list(marked_tree, marked_tree.graph['root'])
    #for node in con_tree.nodes():
    #    print(node, con_tree.nodes[node]['list'])
    steps = gen_plan(con_tree, structure)
    print("\n\nlength of \'steps\'", len(steps))
    find_total_steps(di_tree, steps, structure)
    print("solve time", time.time() - start_time)
    make_parallel(di_tree, steps, structure)
    # for p in p_episodes:
    #     print(p)
main()