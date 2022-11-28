import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pdb 

def reweight_edges(H, structure):
    u = np.zeros((len(structure), len(structure[0])))
    # for i in range(0, len(structure)):
    #     for j in range(0, len(structure[0])):
    #         for h in range(0, structure[i][j]+1):
    #             s = 0
    #             for i0 in range(i - h - 1, i + h):
    #                 for j0 in range(j - h - 1, j + h):
    #                     if (i0 - i) ** 2 + (j0 - j) ** 2 <= h ** 2:
    #                         s += structure[i0][j0]
    #                     u[i0][j0] += s / (h+1)
    #             # u[i][j] += s / h
    for i in range(0, len(structure)):
        for j in range(0, len(structure[0])):
            if structure[i][j]>0:
                #we need to add u in shadow region
                for x in range(i - structure[i][j]-1, i+ structure[i][j]):
                    for y in range(j - structure[i][j]-1, j+ structure[i][j]):
                        if (abs(x-i)+abs(y-j))<structure[i][j]:
                            u[x][y]+=(structure[i][j]-(abs(x-i)+abs(y-j)))/structure[i][j]
    
    print(u)

    for e in H.edges():
        nmr = 1 + abs(structure[e[0][0]][e[0][1]] - structure[e[1][0]][e[1][1]])
        dnr = 1 + u[e[0][0]][e[0][1]] + u[e[1][0]][e[1][1]]
        temp_var = nmr / (dnr)
        # if temp_var>1:
        #     print("struc e1, e2", structure[e[0][0]][e[0][1]], structure[e[1][0]][e[1][1]], "nmr and dnr ", nmr, dnr)
        #     print("edges between", e[0], e[1], "adding weight", temp_var)
        H[e[0]][e[1]]['weight'] = temp_var
        # H.remove_edge(e[0],e[1])
        # H.add_edge(e[0], e[1], weight=temp_var) 
    return H

def get_spanning_tree(structure):
    G = nx.generators.lattice.grid_2d_graph(len(structure), len(structure[0]))
    H = nx.generators.lattice.grid_2d_graph(len(structure), len(structure[0]))    
    positions2 = {node: node for node in H.nodes()}
    positions2[(len(structure),len(structure[0]))]=(len(structure),len(structure[0]))
    H = reweight_edges(H, structure)
    for n in G.nodes():
        if n[0] == 0 or n[1] == 0 or n[0] == len(structure) - 1 or n[1] == len(structure[0]) - 1:
            H.add_edge((len(structure),len(structure[0])), n, weight=0)
            #All edges incident on S are set to weight 0.
    mst2 = nx.minimum_spanning_edges(H, algorithm='kruskal', data=False)
    edgelists2 = list(mst2)
    edgelist_sorted = sorted(edgelists2)
    plt.figure(figsize=(2*len(structure[0]),2*len(structure[0])))
    nx.draw_networkx(H, positions2, width=2, node_size=15, edgelist=edgelists2)
    plt.show()
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