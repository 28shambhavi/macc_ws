import networkx as nx

# Input: the spanning tree T with root S, and the list annotations on T’s nodes
# Output: a sequence of actions for constructing the user-specified structure
# 1 (1) Let M be the maximum number of intervals in any list
# 2 (2) For k = 1 . . . M:
# 3 (a) If k is odd:
# 4 (i) Construct a positive event tree with super-nodes corresponding to the
# nodes of T that have a k-th interval
# 5 (ii) Construct nodes corresponding to the different values in the k-th interval
# of each super-node
# 6 (iii) For node with value v, construct an edge joining it to the node with the
# lowest value ≥ v − 1 in the parent super-node
# 7 (iv) Call Generate-Positive-Steps on this event tree
# 8 (b) If k is even:
# 9 (i) Construct a negative event tree with super-nodes corresponding to the
# nodes of T that have a k-th interval
# 10 (ii) Construct nodes corresponding to the different values in the k-th interval
# of each super-node
# 11 (iii) For node with value v, construct an edge joining it to the node with the
# highest value ≤ v in the parent super-node
# 12 (iv) Call Generate-Negative-Steps on this event tree

def gen_plan(tree, root, a_list):
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


 return seq_list