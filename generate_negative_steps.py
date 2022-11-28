import networkx as nx
import pdb
def gen_neg_steps(tree, N, super_tree, steps):
    counter =0
    if N in tree:
        if len(list(tree.successors(N)))>1:
            if N[2]!=max(super_tree.nodes[(N[0], N[1])]['list']):
                counter+=1
                print("removing block from", (N[0], N[1]), "to value", N[2])
                
                #shortest path from N to root
                path = nx.shortest_path(tree,tree.graph['root'], N)
                print("reverse of path", path)
                steps.append(("neg", N, path))
            open_list = []
            for child in tree.successors(N):
                open_list.append(child)
            open_list.sort(key=lambda x: x[2], reverse=True)
            for child in open_list:
                steps = gen_neg_steps(tree, child, super_tree, steps)                
        elif len(list(tree.successors(N)))==1:
            if N[2]!=max(super_tree.nodes[(N[0], N[1])]['list']):
                counter+=1
                print("removing block from", (N[0], N[1]), "to value", N[2])
                path = nx.shortest_path(tree,tree.graph['root'], N)
                print("reverse of path", path)
                steps.append(("neg", N, path))
            for child in tree.successors(N):
                steps = gen_neg_steps(tree, child, super_tree, steps)
        else:
            if N[2]!=max(super_tree.nodes[(N[0], N[1])]['list']):
                    counter+=1
                    print("removing block from", (N[0], N[1]), "to value", N[2])
                    path = nx.shortest_path(tree,tree.graph['root'], N)
                    print("reverse of path", path)
                    steps.append(("neg", N, path))
    return steps