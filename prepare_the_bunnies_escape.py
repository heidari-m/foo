import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

# Run solution(map), map = Test case.
def graph_maker(map):
    row = []
    col = []
    for i in range(0,map.shape[0]):
        for j in range(0, map.shape[1]):
            if(map[i,j] == 0):
                if(j < map.shape[1]-1):
                    if(map[i,j+1] == 0):
                        row.append(i*map.shape[1]+j)
                        col.append(i*map.shape[1]+(j+1))
                if(0 < j):
                    if(map[i,j-1] == 0):
                        row.append(i*map.shape[1]+j)
                        col.append(i*map.shape[1]+(j-1))
                if(i < map.shape[0]-1):
                    if(map[i+1,j] == 0):
                        row.append(i*map.shape[1] + j)
                        col.append((i+1)*map.shape[1] + j)
                if(0 < i):
                    if(map[i-1,j] == 0):
                        row.append(i*map.shape[1]+j)
                        col.append((i-1)*map.shape[1]+j)
    graph = csr_matrix((np.ones([len(row)],dtype=int),(row, col)))
    return graph

def solution(map):
    # Your code here
    map = np.array(map)
    graph = graph_maker(map)
    dist_matrix, predecessors = dijkstra(csgraph=graph, return_predecessors=True)
    out = dist_matrix[0,-1]
    for i in range(0,map.shape[0]):
        for j in range(0, map.shape[1]):
            if(map[i,j] != 0):
                tmp = np.copy(map)
                tmp[i,j] = 0
                tmpG = graph_maker(tmp)
                dist_matrixR, predecessorsR = dijkstra(csgraph=tmpG, indices=0, return_predecessors=True)
                if (dist_matrixR[-1] < out):
                    out = dist_matrixR[-1]
    return int(out+1)

# Uncomment following to see the the example
# print(solution([[0,0,0,0,0,0],[1,1,1,1,1,0],[0,0,0,0,0,0],[0,1,1,1,1,1],[0,1,1,1,1,1],[0,0,0,0,0,0]]))
