def reweight_edges():
    for i in range(1, len(W) - 1):
        for j in range(1, len(W[0]) - 1):
            u[i][j] = 0
            for h in range(1, W[i][j]):
                s = 0
                for i0 in range(i - h, i + h + 1):
                    for j0 in range(j - h, j + h + 1):
                        if (i0 - i) ** 2 + (j0 - j) ** 2 <= h ** 2:
                            s += W[i0][j0]
                u[i][j] += s / h
    for e in G.edges():
        nmr = 1 + abs(G.nodes[e[0]]['weight'] - G.nodes[e[1]]['weight'])
        dnr = 1 + u[e[0][0]][e[0][1]] + u[e[1][0]][e[1][1]]
        G.edges[e]['weight'] = nmr / dnr
        