import networkx as nx
from generate_positive_steps import gen_pos_steps
from generate_negative_steps import gen_neg_steps

def gen_plan(tree):
    root = tree.graph['root']
    print(tree.nodes())
    M = max([len(tree.nodes[node]['list']) for node in tree.nodes()])
    for k in range(1, M):
        if k % 2 == 1:
            pos_tree = nx.DiGraph()
            for node in tree.nodes():
                if len(tree.nodes[node]['list']) >= k:
                    pos_tree.add_node(node)
            for node in pos_tree.nodes():
                for val in tree.nodes[node]['list'][k - 1]:
                    pos_tree.add_node(val)
            for node in pos_tree.nodes():
                if node in tree.nodes():
                    for val in tree.nodes[node]['list'][k - 1]:
                        for parent in tree.predecessors(node):
                            if val >= max(tree.nodes[parent]['list'][k - 1]):
                                pos_tree.add_edge(val, parent)
            gen_pos_steps(pos_tree, root)
        else:
            neg_tree = nx.DiGraph()
            for node in tree.nodes():
                if len(tree.nodes[node]['list']) >= k:
                    neg_tree.add_node(node)
            for node in neg_tree.nodes():
                for val in tree.nodes[node]['list'][k - 1]:
                    neg_tree.add_node(val)
            for node in neg_tree.nodes():
                if node in tree.nodes():
                    for val in tree.nodes[node]['list'][k - 1]:
                        for parent in tree.predecessors(node):
                            if val <= min(tree.nodes[parent]['list'][k - 1]):
                                neg_tree.add_edge(val, parent)
            gen_neg_steps(neg_tree, root)
    return tree