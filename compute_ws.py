import numpy as np

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