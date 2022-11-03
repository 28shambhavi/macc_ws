import networkx as nx
import numpy as np

class Node:
    def __init__(self, val, height):
        self.val = val
        self.height = height
        self.children = []

    def __repr__(self):
        return f"Node({self.val}, {self.height})"

    def __str__(self):
        return f"Node({self.val}, {self.height})"

class Tree:
    def __init__(self, struct):
        self.struct = struct
        self.root = Node(0, 0)
        self.tree = nx.DiGraph()
        self.tree.add_node(self.root)
        self.build_tree(self.root, self.struct)

    def build_tree(self, node, struct):
        if struct.shape[0] == 1 and struct.shape[1] == 1:
            return
        W, xoffset, yoffset = compute_ws(struct)
        for i in range(W.shape[0]):
            for j in range(W.shape[1]):
                if W[i, j] != 0:
                    child = Node(W[i, j], W[i, j])
                    self.tree.add_node(child)
                    self.tree.add_edge(node, child)
                    self.build_tree(child, W)

    def __repr__(self):
        return f"Tree({self.struct})"

    def __str__(self):
        return f"Tree({self.struct})"




# Compute the workspace
    # struct = R
    # topBorder = argmin(1≤i≤A,1≤j≤B){i − R[i][j] + 1}
    # bottomBorder = argmax(1≤i≤A,1≤j≤B){i + R[i][j] − 1}
    # leftBorder = argmin(1≤i≤A,1≤j≤B){j − R[i][j] + 1}
    # rightBorder = argmax(1≤i≤A,1≤j≤B){j + R[i][j] − 1}
    # xoffset = −topBorder + 1
    # yoffset = −leftBorder + 1
    # workLength = bottomBorder − topBorder + 1
    # workBreadth = rightBorder − leftBorder + 1
    # Build the workLength × workBreadth workspace matrix W as follows:
    # Initialize all entries to 0
    # For each (1 ≤ i ≤ A, 1 ≤ j ≤ B):
    # W[i + xoffset][j + yoffset] = R[i][j]
    # Return:
    # the workspace matrix W
    # the offsets xoffset and yoffset

def compute_ws(struct):
      
     topBorder = np.argmin(struct - np.arange(struct.shape[0])[:, None] + 1)
     bottomBorder = np.argmax(struct + np.arange(struct.shape[0])[:, None] - 1)
     leftBorder = np.argmin(struct - np.arange(struct.shape[1])[None, :] + 1)
     rightBorder = np.argmax(struct + np.arange(struct.shape[1])[None, :] - 1)
     xoffset = -topBorder + 1
     yoffset = -leftBorder + 1
     workLength = bottomBorder - topBorder + 1
     workBreadth = rightBorder - leftBorder + 1
     W = np.zeros((workLength, workBreadth))
     for i in range(struct.shape[0]):
          for j in range(struct.shape[1]):
                W[i + xoffset, j + yoffset] = struct[i, j]
     return W, xoffset, yoffset



# Build all lists
# Input: a node-weighted tree T spanning G
# Output: an annotation of each node of T with a list of markers
# Initialize all lists to contain the single element 0
# Call Construct-List for T and its root node S

def build_all_lists(tree, root):
     for node in tree.nodes():
          tree.nodes[node]['list'] = [0]
     cons_list(tree, root)


# Construct-List
# Input: the spanning tree T, and a node N in it
# Output: an annotation of N with a list of markers
# (1) If N is a leaf node in T:
# (a) Add the user-specified height of the tower at that location to N’s list
# (b) Return
# (2) Call Construct-List recursively for all of N’s children
# (3) Let len be the maximum length of the lists constructed for N’s children
# (4) For i = 2 . . . len, construct the i-th element LN (i) of the list for N as
# follows:
# (a) If i is even, set LN (i) to be max(LN (i − 1), gN (i)) where gN (i) is
# the maximum of the i-th elements in the lists of N’s children −1
# (b) If i is odd, set LN (i) to be min(LN (i − 1), gN (i)) where gN (i) is the
# minimum of the i-th elements in the lists of N’s children
# (5) Construct the last element as follows:
# (a) If len is even and LN (len) is less than or equal to the user-specified height
# h at N, then set LN (len) = h
# (b) If len is even and LN (len) is greater than h, then add h to N’s list
# (c) If len is odd and LN (len) is greater than or equal to the user-specified
# height h at N, then set LN (len) = h
# (d) If len is odd and LN (len) is less than h, then add h to N’s list

def cons_list(tree, node):
    if tree.out_degree(node) == 0:
        tree.nodes[node]['list'].append(tree.nodes[node]['height'])
        return
    for child in tree.successors(node):
        cons_list(tree, child)
    len = max([len(tree.nodes[child]['list']) for child in tree.successors(node)])
    for i in range(2, len + 1):
        if i % 2 == 0:
            tree.nodes[node]['list'].append(max(tree.nodes[node]['list'][i - 1], max([tree.nodes[child]['list'][i - 1] for child in tree.successors(node)])))
        else:
            tree.nodes[node]['list'].append(min(tree.nodes[node]['list'][i - 1], min([tree.nodes[child]['list'][i - 1] for child in tree.successors(node)])))
    if len % 2 == 0 and tree.nodes[node]['list'][len] <= tree.nodes[node]['height']:
        tree.nodes[node]['list'][len] = tree.nodes[node]['height']
    elif len % 2 == 0 and tree.nodes[node]['list'][len] > tree.nodes[node]['height']:
        tree.nodes[node]['list'].append(tree.nodes[node]['height'])
    elif len % 2 == 1 and tree.nodes[node]['list'][len] >= tree.nodes[node]['height']:
        tree.nodes[node]['list'][len] = tree.nodes[node]['height']
    elif len % 2 == 1 and tree.nodes[node]['list'][len] < tree.nodes[node]['height']:
        tree.nodes[node]['list'].append(tree.nodes[node]['height'])

#Generate Plan
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

def generate_plan(tree, root, a_list):
    M = max([len(a_list[node]) for node in tree.nodes()])
    for k in range(1, M + 1):
        if k % 2 == 1:
            pos_tree = nx.DiGraph()
            for node in tree.nodes():
                if len(a_list[node]) >= k:
                    pos_tree.add_node(node)
            for node in pos_tree.nodes():
                for i in range(a_list[node][k - 1], a_list[node][k] + 1):
                    pos_tree.add_node((node, i))
            for node in pos_tree.nodes():
                if type(node) == int:
                    for i in range(a_list[node][k - 1], a_list[node][k] + 1):
                        for j in range(a_list[node][k - 1], i + 1):
                            pos_tree.add_edge((node, j), (node, i))
            generate_positive_steps(pos_tree, root)
        else:
            neg_tree = nx.DiGraph()
            for node in tree.nodes():
                if len(a_list[node]) >= k:
                    neg_tree.add_node(node)
            for node in neg_tree.nodes():
                for i in range(a_list[node][k - 1], a_list[node][k] + 1):
                    neg_tree.add_node((node, i))
            for node in neg_tree.nodes():
                if type(node) == int:
                    for i in range(a_list[node][k - 1], a_list[node][k] + 1):
                        for j in range(i, a_list[node][k] + 1):
                            neg_tree.add_edge((node, j), (node, i))
            generate_negative_steps(neg_tree, root)




#Generate Positive Steps
# Input: a positive event tree E with root super-node S
# Output: a sequence of actions that add blocks to the structure
# 1 (1) Traverse the tree E in depth-first order in such a way that a lower-valued
# sibling is visited before a higher-valued sibling
# 2 (2) When a node n is visited, add a block at the corresponding super-node N if
# the value of n is not the lowest in its interval
# 3 (3) The route between N and the reservoir is indicated by the path of
# super-nodes between N and S in the event tree


def generate_positive_steps(tree, root):
    for node in tree.nodes():
        if type(node) == int:
            if tree.nodes[node]['val'] != min([tree.nodes[child]['val'] for child in tree.successors(node)]):
                print("Add block at node", node, "with value", tree.nodes[node]['val'], "and route", nx.shortest_path(tree, root, node))



# Generate Negative Steps
# Input: a negative event tree E with root super-node S
# Output: a sequence of actions that remove blocks from the structure
# 1 (1) Traverse the tree E in depth-first order in such a way that a higher-valued
# sibling is visited before a lower-valued sibling
# 2 (2) When a node n is visited, remove a block from the corresponding
# super-node N if the value of n is not the highest in its interval
# 3 (3) The route between N and the reservoir is indicated by the path of
# super-nodes between N and S in the event tree

def generate_negative_steps(tree, root):
    for node in tree.nodes():
        if type(node) == int:
            if tree.nodes[node]['val'] != max([tree.nodes[child]['val'] for child in tree.successors(node)]):
                print("Remove block at node", node, "with value", tree.nodes[node]['val'], "and route", nx.shortest_path(tree, root, node))



def main():
    # Generate a random structure
    structure = [[0,0,0,0,0],
                 [0,3,2,3,0],
                [0,2,0,2,0],
                [0,1,0,1,0],
                [0,0,0,0,0]]
    print(np.array(structure))
    G = nx.generators.lattice.grid_2d_graph(5, 5)
    positions = {node: node for node in G.nodes()}
    weights = {(u, v): structure[u][v] for u, v in len(structure[0])}
    print("Structure:", structure)
    print(structure.nodes())
    pos = dict( (n, n) for n in structure.nodes() )
    N = structure.number_of_nodes()
    print(N, pos)
    labels = dict( ((i, j), i + (N-1-j) * N ) for i, j in structure.nodes() )
    nx.relabel_nodes(structure,labels,False)
    inds=labels.keys()
    vals=labels.values()
    inds.sort()
    vals.sort()
    pos2=dict(zip(vals,inds))
    nx.draw_networkx(structure, pos=pos2, with_labels=False, node_size = 15)
    # Generate a random spanning tree
    tree = nx.mimum_spanning_tree(nx.from_numpy_matrix(np.array(structure)))
    plt.figure()
    nx.draw_networkx(tree, pos=pos2, with_labels=False, node_size = 15)
    plt.show()
    # Generate a list of intervals
    #a_list = generate_list(tree, 0)
    # Generate a plan
    #generate_plan(tree, 0, a_list)

main()