import networkx as nx
import pdb
def gen_pos_steps(tree, k):
    # traverse nodes such that higher node[2] value visited first
    for node in tree:
        if tree.successors(node)!=None:
            for child in tree.successors(node):
                print("child", child, "of", node)
            print("next node")




#     print("how many times\n \n \n \n \n ")
#     #node has x y and value
#     seq_list = []
#     open_list = []
#     flag = 0
#     root = tree.graph['root']
#     for node in nx.dfs_preorder_nodes(tree, root):
#         if node==root:
#             continue
#         depth = nx.shortest_path_length(tree, root, node)
#         if flag==depth:
#             open_list.append(node)
#         elif flag!=depth:
#             open_list.sort(key=lambda x: x[2])
#             seq_list.append(open_list[0])
#             open_list = []
#             open_list.append(node)
#             if len(list(nx.dfs_preorder_nodes(tree, root)))-1 == len(seq_list):
#                 seq_list.append(open_list[0])
#             flag = depth
#     if len(seq_list) == 0:
#         return
#     else: 
#         print(seq_list, "seq_list in positive tree")
#     min_value = min(node[2] for node in seq_list)
#     for node in seq_list:
#         if node[2]>min_value:
#             add_blocks(node, tree, min_value, height_map)

# def add_blocks(node, tree, min_value, height_map):
#     print("add block at", node, "with value", node[2], "and min value", min_value)
# # def add_blocks(open_list, tree):
# #     min_value = min(node[2] for node in open_list)
# #     for node in open_list:
# #         if node[2]>min_value:
# #             print("add block at", node, "with value", node[2], "and min value", min_value)   
