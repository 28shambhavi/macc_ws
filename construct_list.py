def cons_list(tree, N):
    if tree.out_degree(N) == 0:
        tree.nodes[N]['list']+=[tree.nodes[N]['height']]
        print(tree.nodes[N]['list'], "is this list made")
        return
    if tree.successors(N)!=None:
        for child in tree.successors(N):
            cons_list(tree, child)
    
    len = max([len(tree.nodes[child]['list']) for child in tree.successors(N)])
    for i in range(2, len):
        if i % 2 == 0:
            tree.nodes[N]['list']+=[max(tree.nodes[N]['list'][i - 1], max([tree.nodes[child]['list'][i - 1] for child in tree.successors(N)]))]
        else:
            tree.nodes[N]['list']+=[min(tree.nodes[N]['list'][i - 1], min([tree.nodes[child]['list'][i - 1] for child in tree.successors(N)]))]
    
    if len % 2 == 0 and tree.nodes[N]['list'][len] <= tree.nodes[N]['height']:
        tree.nodes[N]['list'][len] = tree.nodes[N]['height']
    elif len % 2 == 0 and tree.nodes[N]['list'][len] > tree.nodes[N]['height']:
        tree.nodes[N]['list']+=[tree.nodes[N]['height']]
    elif len % 2 == 1 and tree.nodes[N]['list'][len] >= tree.nodes[N]['height']:
        tree.nodes[N]['list'][len] = tree.nodes[N]['height']
    elif len % 2 == 1 and tree.nodes[N]['list'][len] < tree.nodes[N]['height']:
        tree.nodes[N]['list']+=[tree.nodes[N]['height']]
         
