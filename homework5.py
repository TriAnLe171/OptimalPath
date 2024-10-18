#-------------------------------------------
#  CSC 211 Prim's Algorithm Implementation
#-------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack

def prim(g, i):
    '''
    Prim's Algorithm
    returns the minimal spanning tree (mst)
    for graph g, starting with vertex i
    '''

    # initialize values
    n=g.sizeVertices()  # number of vertices to add
    D=[]    # D[i] is the cost/distance to add vertex i
    V=[]    # V[i] is the vertex in the MST adjacent to i 
    for j in range(0,n):
        D.append(float('inf'))
        V.append(None)

    # create MST and add vertex i into it 
    D[i]=0  
    mst = LinkedDirectedGraph()
    mst.addVertex(i)
    g.getVertex(i).setMark()

    # recently added vertex
    minIndex=i

    # add vertices until the mst has as many vertices as g
    while mst.sizeVertices()<n:

        # update D and V based on minIndex 
        for w in g.neighboringVertices(minIndex):
                if not w.isMarked():
                    k=w.getLabel()
                    edgeVal = g.getEdge(minIndex,k).getWeight()
                    if D[k]>edgeVal:
                        D[k]=edgeVal
                        V[k]=minIndex
      
        # find the first unvisited vertex
        k=-1
        j=0
        while k<0 and j<n:
            if not g.getVertex(j).isMarked():
                k=j
            j+=1

        # find minimum cost unvisited vertex
        minIndex=k
        for j in range(0,n):    
            if not g.getVertex(j).isMarked():
                if D[j]<D[minIndex]:
                    minIndex=j

        # add new vertex to the MST and mark it in g
        edgeVal = g.getEdge(V[minIndex],minIndex).getWeight()
        mst.addVertex(minIndex)
        mst.addEdge(minIndex,V[minIndex],edgeVal)
        mst.addEdge(V[minIndex],minIndex,edgeVal)

        g.getVertex(minIndex).setMark()

    return mst

#-----------------------------------
# Test out the method below

g = LinkedDirectedGraph()

# add vertices
for i in range(0,6):
    g.addVertex(i)

# add edges
g.addEdge(0,1,0.4)
g.addEdge(1,0,0.4)
g.addEdge(0,2,0.2)
g.addEdge(2,0,0.2)
g.addEdge(0,5,2.2)
g.addEdge(5,0,2.2)

g.addEdge(1,2,0.1)
g.addEdge(2,1,0.1)
g.addEdge(1,3,0.2)
g.addEdge(3,1,0.2)


g.addEdge(2,3,0.6)
g.addEdge(3,2,0.6)
g.addEdge(2,4,0.8)
g.addEdge(4,2,0.8)

g.addEdge(3,4,0.3)
g.addEdge(4,3,0.3)
g.addEdge(3,5,0.5)
g.addEdge(5,3,0.5)



# Try out some methods

print("\n print graph info : g ")
print(g)

m=prim(g,0)

print("\n print graph info : mst ")
print(m)







