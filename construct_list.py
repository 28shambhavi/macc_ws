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

def cons_list(tree, N):
    if tree.out_degree(N) == 0:
        tree.nodes[N]['list'].append(tree.nodes[N]['height'])
        return
    for child in tree.successors(N):
        cons_list(tree, child)
    len = max([len(tree.nodes[child]['list']) for child in tree.successors(N)])
    for i in range(2, len):
        if i % 2 == 0:
            tree.nodes[N]['list'].append(max(tree.nodes[N]['list'][i - 1], max([tree.nodes[child]['list'][i - 1] for child in tree.successors(N)])))
        else:
            tree.nodes[N]['list'].append(min(tree.nodes[N]['list'][i - 1], min([tree.nodes[child]['list'][i - 1] for child in tree.successors(N)])))
    
    if len % 2 == 0 and tree.nodes[N]['list'][len] <= tree.nodes[N]['height']:
        tree.nodes[N]['list'][len] = tree.nodes[N]['height']
    elif len % 2 == 0 and tree.nodes[N]['list'][len] > tree.nodes[N]['height']:
        tree.nodes[N]['list'].append(tree.nodes[N]['height'])
    elif len % 2 == 1 and tree.nodes[N]['list'][len] >= tree.nodes[N]['height']:
        tree.nodes[N]['list'][len] = tree.nodes[N]['height']
    elif len % 2 == 1 and tree.nodes[N]['list'][len] < tree.nodes[N]['height']:
        tree.nodes[N]['list'].append(tree.nodes[N]['height'])
         
