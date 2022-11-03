# Input: a negative event tree E with root super-node S
# Output: a sequence of actions that remove blocks from the structure
# 1 (1) Traverse the tree E in depth-first order in such a way that a higher-valued
# sibling is visited before a lower-valued sibling
# 2 (2) When a node n is visited, remove a block from the corresponding
# super-node N if the value of n is not the highest in its interval
# 3 (3) The route between N and the reservoir is indicated by the path of
# super-nodes between N and S in the event tree

def gen_neg_steps(tree, root):
    seq_list = []
    for node in tree.nodes():
        if node in tree.nodes():
            for val in tree.nodes[node]['list'][k - 1]:
                for parent in tree.predecessors(node):
                    if val <= min(tree.nodes[parent]['list'][k - 1]):
                        neg_tree.add_edge(val, parent)
    gen_neg_steps(neg_tree, root)
    return seq_list