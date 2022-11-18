import networkx as nx
import pdb
def cons_list(tree, N):
    if tree.out_degree(N) == 0:
        tree.nodes[N]['list'].append(tree.nodes[N]['height'])
        return tree
    if tree.successors(N)!=None:
        for child in tree.successors(N):
            cons_list(tree, child)
    max_len = max([len(tree.nodes[child]['list']) for child in tree.successors(N)])
    
    for i in range(1, max_len+1):
        if len(tree.nodes[N]['list']) < i+1:
            tree.nodes[N]['list'].append(0)
            gn_list = []
            for child in tree.successors(N):
                    if len(tree.nodes[child]['list'])>i:
                        gn_list.append(tree.nodes[child]['list'][i]) 
            if len(gn_list)>0:
                if i%2 == 1:
                        tree.nodes[N]['list'][i] = max(tree.nodes[N]['list'][i - 1], max(gn_list)-1)
                else:
                        tree.nodes[N]['list'][i] = min(tree.nodes[N]['list'][i - 1], min(gn_list))
    
    max_N = len(tree.nodes[N]['list'])-1
    #leaf node should reach here also
    if max_N % 2 == 1 and tree.nodes[N]['list'][max_N] <= tree.nodes[N]['height']:
        tree.nodes[N]['list'][max_N]=(tree.nodes[N]['height'])
    elif max_N % 2 == 1 and tree.nodes[N]['list'][max_N] > tree.nodes[N]['height']:
        tree.nodes[N]['list'].append(tree.nodes[N]['height'])
    elif max_N % 2 == 0 and tree.nodes[N]['list'][max_N] >= tree.nodes[N]['height']:
        tree.nodes[N]['list'][max_N]=(tree.nodes[N]['height'])
    elif max_N % 2 == 0 and tree.nodes[N]['list'][max_N] < tree.nodes[N]['height']:
        tree.nodes[N]['list'].append(tree.nodes[N]['height'])
    return tree