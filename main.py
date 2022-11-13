import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from compute_ws import compute_ws
from build_all_lists import build_all_lists
# from generate_plan import gen_plan
from construct_list import cons_list
# from generate_positive_steps import gen_pos_steps
# from generate_negative_steps import gen_neg_steps
class Node:
    def __init__(self, val, height):
        self.val = val
        self.height = height
        self.children = []

def get_spanning_tree(structure):
    #as a multidigraph
    G = nx.generators.lattice.grid_2d_graph(len(structure[0]), len(structure[0]))
    H = nx.generators.lattice.grid_2d_graph(len(structure[0]), len(structure[0]))
    
    positions2 = {node: node for node in H.nodes()}
    positions2[(len(structure[0]),len(structure[0]))]=(len(structure[0]),len(structure[0]))

    for e  in G.edges():
        #weight of each edge is difference between the values of the nodes it connects
        H.add_edge(e[0], e[1], weight=abs(structure[e[0][0]][e[0][1]]-structure[e[1][0]][e[1][1]])+0.1)
        
        #boundaries connected to the reservoir
        set = [e[0],e[1]]
        for i in range(len(set)):
            if set[i][0]==0 or set[i][1]==0 or set[i][0]==len(structure[0]) or set[i][1]==len(structure[0]):     
                H.add_edge((len(structure[0]),len(structure[0])), set[i],weight=0)
                
    mst2 = nx.minimum_spanning_edges(H, algorithm='kruskal', data=False)
    edgelists2 = list(mst2)
    edgelist_sorted = sorted(edgelists2)

    # plt.figure(figsize=(2*len(structure[0]),2*len(structure[0])))
    # nx.draw_networkx(H, positions2, width=2, node_size=15, edgelist=edgelists2)
    # plt.show()
    return edgelist_sorted

def flip_edge(e, tree, visited_edges, node_queue):
    if e in visited_edges:
        return visited_edges, node_queue
    
    elif e in tree.edges() and e[1] in node_queue:
        tree.remove_edge(e[0],e[1])
        tree.add_edge(e[1],e[0])
        visited_edges.append((e[1], e[0]))
        node_queue.append(e[0])
        return visited_edges, node_queue

    elif e in tree.edges() and e[0] in node_queue:
        visited_edges.append(e)
        node_queue.append(e[1])
        return visited_edges, node_queue
    return visited_edges, node_queue

def main():
    #Generate a random structure
    structure = [[1,1,1,1,1],
                [1,0,0,0,1],
                [1,0,3,0,1],
                [1,0,0,0,1],
                [1,1,1,1,1]]

    edge_list = get_spanning_tree(structure)
    tree = nx.DiGraph()
    tree.graph['root'] = (len(structure[0]),len(structure[0]))
    tree.add_edges_from(edge_list)
    
    #turn into directed graph
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

    #build all lists of markers by initializing to zero
    marked_tree = build_all_lists(di_tree, structure)
    for n in marked_tree.nodes():
        print(n, marked_tree.nodes[n]['list'])
        #construct list of markers for each node
        marked_tree.nodes[n]['list'] = cons_list(marked_tree, n)
    
    
main()