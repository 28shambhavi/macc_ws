import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from compute_ws import compute_ws
from build_all_lists import build_all_lists
from generate_plan_super import gen_plan
from construct_list import cons_list

class Node:
    def __init__(self, val, height):
        self.val = val
        self.height = height
        self.children = []

def get_spanning_tree(structure):
    G = nx.generators.lattice.grid_2d_graph(len(structure), len(structure[0]))
    H = nx.generators.lattice.grid_2d_graph(len(structure), len(structure[0]))    
    positions2 = {node: node for node in H.nodes()}
    positions2[(len(structure),len(structure[0]))]=(len(structure),len(structure[0]))
    for e  in G.edges():
        H.add_edge(e[0], e[1], weight=abs(structure[e[0][0]][e[0][1]]-structure[e[1][0]][e[1][1]])+0.1)
        set = [e[0],e[1]]
        for i in range(len(set)):
            if set[i][0]==0 or set[i][1]==0 or set[i][0]==len(structure[0])-1 or set[i][1]==len(structure[0])-1:     
                # verify logic here
                H.add_edge((len(structure),len(structure[0])), set[i],weight=0.1)
                
    mst2 = nx.minimum_spanning_edges(H, algorithm='kruskal', data=False)
    edgelists2 = list(mst2)
    edgelist_sorted = sorted(edgelists2)
    # plt.figure(figsize=(2*len(structure[0]),2*len(structure[0])))
    # nx.draw_networkx(H, positions2, width=2, node_size=15, edgelist=edgelists2)
    # plt.show()
    return edgelist_sorted

def flip_edge(e, tree, visited_edges, node_queue):
    if e not in visited_edges:
        if e in tree.edges() and e[1] in node_queue:
            tree.remove_edge(e[0],e[1])
            tree.add_edge(e[1],e[0])
            visited_edges.append((e[1], e[0]))
            node_queue.append(e[0])
        elif e in tree.edges() and e[0] in node_queue:
            visited_edges.append(e)
            node_queue.append(e[1])
    return visited_edges, node_queue

def main():
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
    # structure = [[0,0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,4,4,4,4,4,0,0,0],
    #             [0,0,0,4,2,2,2,4,0,0,0],
    #             [0,0,0,4,2,5,2,4,0,0,0],
    #             [0,0,0,4,2,2,2,4,0,0,0],
    #             [0,0,0,4,4,4,4,4,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0,0],
    #             [0,0,0,0,0,0,0,0,0,0,0]]
    structure = [[0,0,	0,	0,	0,	0,	0,	0,	0,	0,	0],	
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],	
                [0,	0,	0,	4,	0,	0,	5,	0,	0,	0,	0],	
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],	
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],	
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
                # [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],	
                # [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],		
                [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0]]
    # structure = [[4,4,4,4,4],
    #             [4,2,2,2,4],
    #             [4,2,5,2,4],
    #             [4,2,2,2,4],
    #             [4,4,4,4,4]]
    # structure = [[1,1,1,1,1],
    #             [1,0,0,0,1],
    #             [1,0,3,0,1],
    #             [1,0,0,0,1],
    #             [1,1,1,1,1]]
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
    for node in con_tree.nodes():
        print(node, con_tree.nodes[node]['list'])
    plan_tree = gen_plan(con_tree, structure)

main()