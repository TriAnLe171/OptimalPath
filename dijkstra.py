#-----------------------------------------------
#  CSC 211 Dijkstra's Algorithm Implementation
#-----------------------------------------------

from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack

def dijkstra(g, n):
    print("start")
    # n = g.sizeVertices()
    # list = g.getMyVertices()
    m = n**2
    # arr = []
    # for k in list:
    #     arr.append(k)
    # print(arr)
    D = []
    V = []
    for j in range(m):
        D.append(float('inf'))
        V.append(None)
    D[0] = 0
    try:
        g.getVertex(0).setMark()
    except:
        print("zero value is absent")
        return
    
    visited = True
    minIndex = 0
    extra = 0
    
    while visited:
        counter = 0
        for w in g.neighboringVertices(minIndex):
            if not w.isMarked():
                counter += 1
                k = w.getLabel()
                weight = g.getEdge(minIndex, k).getWeight()
                value = D[minIndex] + weight
                if D[k] > value:
                    D[k] = value
                    V[k] = minIndex
        
        if counter == 0:
            if extra == 0:
                extra = 1
            # minI = minIndex
            # minV = D[minIndex]
            # D[minIndex] = float('inf')
            g.getVertex(minIndex).setMark()
            k = -1
            j = 0
            while k < 0 and j < m:
                try:
                    if not g.getVertex(j).isMarked():
                        k = j
                    j += 1
                except:
                    j += 1
                    continue
                
            # find minimum cost unvisited vertex
            minIndex = k
            for j in range(0, m):
                try:
                    if not g.getVertex(j).isMarked():
                        if D[j] <= D[minIndex]:
                            minIndex = j
                    # D[minI] = minV
                except:
                    continue
            
            try:
                g.getVertex(minIndex)
            except:
                print("forced return")
                return D
            
        for w in g.neighboringVertices(minIndex):
            if not w.isMarked():
                counter += 1
                k = w.getLabel()
                weight = g.getEdge(minIndex, k).getWeight()
                value = D[minIndex] + weight
                if D[k] > value:
                    D[k] = value
                    V[k] = minIndex
            else:
                visited = False
                break
                
        k = -1
        j = 0
        while k < 0 and j < m:
            try:
                if not g.getVertex(j).isMarked():
                    k = j
                j += 1
            except:
                j += 1
                continue
            
        minIndex = k
        
        for j in range(0, m):
            try:
                if not g.getVertex(j).isMarked():
                    if D[j] < D[minIndex]:
                        minIndex = j
            except:
                continue
        
        try:
            g.getVertex(minIndex).setMark()
        except:
            print('k==-1')
            return D
        
    return D


#-----------------------------------
# Test out the method below

g = LinkedDirectedGraph()

# add vertices
for i in range(0,9):
    g.addVertex(i)

# add edges
N=3
# add vertices
for i in range(N**2):
    g.addVertex(i)


# add edges
for i in range(N):
    for j in range(N-1):
        g.addEdge(N*i+j,N*i+j+1,1)
        g.addEdge(N*i+j+1,N*i+j,1)

for j in range(N):
    for i in range(N-1):
        g.addEdge(N*i+j,N*(i+1)+j,1)
        g.addEdge(N*(i+1)+j,N*i+j,1)

print(g)


#print(g)

# try it out
print(dijkstra(g,0))

