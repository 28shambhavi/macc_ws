import networkx as nx
import pdb
def gen_pos_steps(tree, N, super_tree):
    if N in tree:
        if len(list(tree.successors(N)))>1:
            if N[2]!=min(super_tree.nodes[(N[0], N[1])]['list']):
                # counter+=1
                print("adding block at", (N[0], N[1]), "to value", N[2])
                print("path", nx.shortest_path(tree,tree.graph['root'], N))
            open_list = []
            for child in tree.successors(N):
                open_list.append(child)
            open_list.sort(key=lambda x: x[2])
            for child in open_list:
                gen_pos_steps(tree, child, super_tree)
                
        elif len(list(tree.successors(N)))==1:
            if N[2]!=min(super_tree.nodes[(N[0], N[1])]['list']):
                print("adding block at", (N[0], N[1]), "to value", N[2]) 
                print("path", nx.shortest_path(tree,tree.graph['root'], N))
            for child in tree.successors(N):
                gen_pos_steps(tree, child, super_tree)
        else:
            if N[2]!=min(super_tree.nodes[(N[0], N[1])]['list']):
                    print("adding block at", (N[0], N[1]), "to value", N[2]) 
                    print("path", nx.shortest_path(tree,tree.graph['root'], N))

