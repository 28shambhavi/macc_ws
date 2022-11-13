
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