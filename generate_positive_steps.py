import networkx as nx
import pdb
def gen_pos_steps(tree, N, super_tree, steps):
    if N in tree:
        if len(list(tree.successors(N)))>1:
            if N[2]!=min(super_tree.nodes[(N[0], N[1])]['list']):
            # if N[2]!=None:
                pdb.set_trace()
                print("adding block at", (N[0], N[1]), "to value", N[2])
                path = nx.shortest_path(tree,tree.graph['root'], N)
                print("path", path)
                steps.append(("pos", N, path))
            open_list = []
            for child in tree.successors(N):
                open_list.append(child)
            open_list.sort(key=lambda x: x[2])
            for child in open_list:
                steps = gen_pos_steps(tree, child, super_tree, steps)
                
        elif len(list(tree.successors(N)))==1:
            if N[2]!=min(super_tree.nodes[(N[0], N[1])]['list']):
                print("adding block at", (N[0], N[1]), "to value", N[2]) 
                path = nx.shortest_path(tree,tree.graph['root'], N)
                print("path", path)
                steps.append(("pos", N, path))
            for child in tree.successors(N):
                steps = gen_pos_steps(tree, child, super_tree, steps)
        else:
            if N[2]!=min(super_tree.nodes[(N[0], N[1])]['list']):
                    print("adding block at", (N[0], N[1]), "to value", N[2]) 
                    path = nx.shortest_path(tree,tree.graph['root'], N)
                    print("path", path)
                    steps.append(("pos", N, path))
    return steps