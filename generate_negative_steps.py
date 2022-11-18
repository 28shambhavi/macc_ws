import networkx as nx
import pdb
def gen_neg_steps(tree, root, k, height_map):
    seq_list = []
    open_list = []
    flag = 0
    for node in nx.dfs_preorder_nodes(tree, root):
        if node==root:
            continue
        depth = nx.shortest_path_length(tree, root, node)
        if flag==depth:
            open_list.append(node)
        elif flag!=depth:
            open_list.sort(key=lambda x: x[2], reverse=True)
            seq_list.append(open_list[0])
            open_list = []
            open_list.append(node)
            if len(list(nx.dfs_preorder_nodes(tree, root)))-1 == len(seq_list):
                seq_list.append(open_list[0])
            flag = depth
    if len(seq_list) == 0:
        return
    else: 
        print(seq_list, "seq_list in negative tree")
    max_value = max(node[2] for node in seq_list)
    for node in seq_list:
        if node[2]<max_value:
            remove_blocks(node, tree, max_value, height_map)

def remove_blocks(node, tree, max_value, height_map):
    print("remove block at", node, "with value", node[2], "and max value", max_value)