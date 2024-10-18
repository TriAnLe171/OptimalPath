#-------------------------------------------
#  structuredGraphs.py
#-------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack

g = LinkedDirectedGraph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)
g.addVertex(9)

g.addEdge(0,1,3.8)
g.addEdge(1,0,3.8)
g.addEdge(1,2,1.3)
g.addEdge(2,1,1.3)

g.addEdge(4,5,3.1)
g.addEdge(5,4,3.1)
g.addEdge(6,7,4.3)
g.addEdge(7,6,4.3)
g.addEdge(7,8,1.1)
g.addEdge(8,7,1.1)

g.addEdge(1,4,1.2)
g.addEdge(4,1,1.2)
g.addEdge(2,5,0.7)
g.addEdge(5,2,0.7)

g.addEdge(4,7,3.4)
g.addEdge(7,4,3.4)
g.addEdge(5,8,1.2)
g.addEdge(8,5,1.2)


# ---- Test the DFS traversal ----

# def dfs(g, v):
#     """ recursive depth-first search """
#     v.setMark()
#     print(v.getLabel())
#     for w in g.neighboringVertices(v.getLabel()):
#         if not w.isMarked():
#             dfs(g, w)


# print("\n depth-first search: ")
# g.clearVertexMarks()
# dfs(g,g.getVertex(0))

# # ---- Test the BFS traversal ----

# def bfs(g, v):
#     """ breadth-first search """
#     q=LinkedQueue()
#     v.setMark()
#     q.add(v)
#     while len(q)>0:
#         x=q.pop()
#         print(x.getLabel())
#         for w in g.neighboringVertices(x.getLabel()):
#             if not w.isMarked():
#                 w.setMark()
#                 q.add(w)
        

# print("\n breadth-first search: ")
# g.clearVertexMarks()
# bfs(g,g.getVertex(0))

def dijkstra(g, start):
    '''
    Dijkstra's Algorithm
    returns the shortest distance from start to all other vertices
    in graph g, along with the shortest path to each vertex
    '''

    # initialize values
    n=g.sizeVertices()  # number of vertices
    D=[]    # D[i] is the shortest distance from start to i
    V=[]    # V[i] is the previous vertex in the shortest path to i 
    for j in range(n):
        D.append(float('inf'))
        V.append(None)

    # set start vertex
    D[start] = 0

    # process vertices
    while True:
        # find minimum cost unvisited vertex
        minIndex = -1
        for j in range(n):
            if g.getVertex(j) and not g.getVertex(j).isMarked():
                if minIndex == -1 or D[j] < D[minIndex]:
                    minIndex = j

        if minIndex == -1 or D[minIndex] == float('inf'):
            break

        # mark vertex as visited
        g.getVertex(minIndex).setMark()

        # update distances to neighboring vertices
        for w in g.neighboringVertices(minIndex):
            if not w.isMarked():
                k=w.getLabel()
                edgeVal = g.getEdge(minIndex,k).getWeight()
                if D[k] > D[minIndex] + edgeVal:
                    D[k] = D[minIndex] + edgeVal
                    V[k] = minIndex

    return (D, V)

# g.removeVertex(5)
print(g)
print(dijkstra(g,0))


