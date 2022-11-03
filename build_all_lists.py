# Input: a node-weighted tree T spanning G
# Output: an annotation of each node of T with a list of markers
# Initialize all lists to contain the single element 0
# Call Construct-List for T and its root node S
from construct_list import cons_list


def build_all_lists(tree, root):
    for node in tree.nodes():
        tree.nodes[node]['list'] = [0]
    cons_list(tree, root)