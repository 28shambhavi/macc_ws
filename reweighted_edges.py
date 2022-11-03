# Algorithm 7: Procedure Reweight-Edges
# Input: the graphical representation G of a workspace matrix W
# Output: reweighted edges for G
# 1 (1) For each cell (i, j) in the workspace matrix W, compute the usefulness
# factor u(i, j) as follows:
# 2 (a) u(i, j) = 0
# 3 (b) For each tower of height h at location (i
# 0
# , j0
# ) that casts a non-zero

# shadow s on (i, j):
# 4 (i) u(i, j) = u(i, j) + s/h
# 5 (2) For each edge e in G:
# 6 (a) nmr = 1 + |difference in weights of its end-point nodes|
# 7 (b) dnr = 1 + sum of the usefulness factors of its end-point nodes
# 8 (c) weight of e = nmr/dnr

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
        