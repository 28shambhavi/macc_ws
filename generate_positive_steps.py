# Input: a positive event tree E with root super-node S
# Output: a sequence of actions that add blocks to the structure
# 1 (1) Traverse the tree E in depth-first order in such a way that a lower-valued
# sibling is visited before a higher-valued sibling
# 2 (2) When a node n is visited, add a block at the corresponding super-node N if
# the value of n is not the lowest in its interval
# 3 (3) The route between N and the reservoir is indicated by the path of
# super-nodes between N and S in the event tree

def gen_pos_steps(tree, root):
    seq_list = []
    for node in tree.nodes():
        if node in tree.nodes():
            for val in tree.nodes[node]['list'][k - 1]:
                for parent in tree.predecessors(node):
                    if val >= max(tree.nodes[parent]['list'][k - 1]):
                        pos_tree.add_edge(val, parent)
    gen_pos_steps(pos_tree, root)
    return seq_list