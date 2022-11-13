from generate_plan import gen_plan

def gen_neg_steps(tree, root):
    seq_list = []
    neg_tree = []
    for node in tree.nodes():
        if node in tree.nodes():
            for val in tree.nodes[node]['list'][k - 1]:
                for parent in tree.predecessors(node):
                    if val <= min(tree.nodes[parent]['list'][k - 1]):
                        neg_tree.add_edge(val, parent)
    gen_neg_steps(neg_tree, root)
    return seq_list