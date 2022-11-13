import numpy as np
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