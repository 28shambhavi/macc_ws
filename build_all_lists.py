def build_all_lists(tree, structure):
    for node in tree.nodes():
        tree.nodes[node]['list'] = [0]
        if node[0]==len(structure[0]) and node[1]==len(structure[0]):
            tree.nodes[node]['height'] = 0
        else: 
            tree.nodes[node]['height'] = structure[node[0]][node[1]]
    return tree