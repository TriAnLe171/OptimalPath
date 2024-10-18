#-------------------------------------------
#  CSC 211 Examples with Graphs
#-------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack

g = LinkedDirectedGraph()

# add vertices
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.addVertex("G")

# add edges
g.addEdge("A", "B", 1)
g.addEdge("B", "A", 1)
g.addEdge("A", "C", 1)
g.addEdge("C", "A", 1)
g.addEdge("B", "D", 1)
g.addEdge("D", "B", 1)
g.addEdge("B", "E", 1)
g.addEdge("E", "B", 1)
g.addEdge("B", "F", 1)
g.addEdge("F", "B", 1)
g.addEdge("C", "E", 1)
g.addEdge("E", "C", 1)
g.addEdge("D", "E", 1)
g.addEdge("E", "D", 1)
g.addEdge("D", "G", 1)
g.addEdge("G", "D", 1)
g.addEdge("E", "G", 1)
g.addEdge("G", "E", 1)
g.addEdge("F", "G", 1)
g.addEdge("G", "F", 1)



# Try out some methods

print("\n print graph info: ")
print(g)


print("\n neighboring vertices of A:")
for vertex in g.neighboringVertices("A"):
    print(vertex)


print("\n incident edges of A:")
for edge in g.incidentEdges("A"):
    print(edge)

# ---- Test the DFS traversal ----

def dfs(g, v):
    """ recursive depth-first search """
    v.setMark()
    print(v.getLabel())
    for w in g.neighboringVertices(v.getLabel()):
        if not w.isMarked():
            dfs(g, w)


print("\n depth-first search: ")
g.clearVertexMarks()
dfs(g,g.getVertex("A"))

# ---- Test the BFS traversal ----

def bfs(g, v):
    """ breadth-first search """
    q=LinkedQueue()
    v.setMark()
    q.add(v)
    while len(q)>0:
        x=q.pop()
        print(x.getLabel())
        for w in g.neighboringVertices(x.getLabel()):
            if not w.isMarked():
                w.setMark()
                q.add(w)
        

print("\n breadth-first search: ")
g.clearVertexMarks()
bfs(g,g.getVertex("A"))



        
    
