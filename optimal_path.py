from graph import LinkedDirectedGraph
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import random
import networkx as nx
import matplotlib.pyplot as plt

window = tk.Tk()
N = simpledialog.askinteger(
    'Input', 'Please enter the number of vertices in an egde:', parent=window)

while N < 0:
    N = simpledialog.askinteger(
        'Error', 'Please enter a positive integer:', parent=window)

g = LinkedDirectedGraph()


set_prob = simpledialog.askfloat(
    'Probability', 'Please enter the proportion of blocked and open vertices: ', parent=window)

while set_prob < 0 or set_prob > 1:
    set_prob = simpledialog.askfloat(
        'Error', 'Please enter a number from range 0 to 1:', parent=window)


def dijkstra(g, n):
    # print("satrt")
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
        return "There is no solution for optimal path", ''

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
                    # print("forced return")
                    return D, V
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

                # find minimum cost unvisited vertex
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

    if D[-1] == float("inf"):
        return "There is no solution for optimal path", ''
    else:
        return D, V


def generateGraph(N):
    for i in range(N**2):
        g.addVertex(i)


# add edges
    for i in range(N):
        for j in range(N-1):
            g.addEdge(N*i+j, N*i+j+1, 1)
            g.addEdge(N*i+j+1, N*i+j, 1)

    for j in range(N):
        for i in range(N-1):
            g.addEdge(N*i+j, N*(i+1)+j, 1)
            g.addEdge(N*(i+1)+j, N*i+j, 1)


def sketchGraph(N):
    # Original graph
    G = nx.Graph()
    for i in range(N**2):
        G.add_node(i)

    # add edges
    for i in range(N):
        for j in range(N-1):
            G.add_edges_from([(N*i+j, N*i+j+1)])

    for j in range(N):
        for i in range(N-1):
            G.add_edges_from([(N*i+j, N*(i+1)+j)])

# Blocked graph
    G_after = nx.Graph()
    for i in range(N**2):
        G_after.add_node(i)

    # add edges
    for i in range(N):
        for j in range(N-1):
            G_after.add_edges_from([(N*i+j, N*i+j+1)])

    for j in range(N):
        for i in range(N-1):
            G_after.add_edges_from([(N*i+j, N*(i+1)+j)])

    arr = []
    prob = set_prob
    n = int(G_after.number_of_nodes()*prob)
    for i in range(n):
        label = random.randrange(G_after.number_of_nodes())
        while arr.__contains__(label):
            label = random.randrange(G_after.number_of_nodes())
        arr.append(label)
    for i in arr:
        G_after.remove_node(i)

# Sketch both graphs
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
    nx.draw(G, with_labels=True, ax=ax1)
    ax1.set_title('Original Graph')
    nx.draw(G_after, with_labels=True, ax=ax2)
    ax2.set_title('Blocked Graph')
    plt.show()
# return arr contains blocked vertices for later use
    return arr


def remove_neighbors(graph, label):
    graph.removeVertex(label)
    g = graph


def remove_vertices(g, a):
    # blocked vertices in Arr
    Arr = sketchGraph(N)
    arr1 = []
    n = int(g.size*a)
    for i in Arr:
        remove_neighbors(g, i)

    # remaining vertices
    for i in range(g.size+n):
        if i not in Arr:
            arr1.append(i)
    return f"Remaining vertices in the graph: {arr1}\nBlocked vertices in the graph: {Arr}"

# return an optimal path for the puzzle


def print_path(V):
    current = V[-1]
    path = [current]
    while current != 0:
        current = V[current]
        path.append(current)
# insert number N**2 for it to become the beginning of the solution
    path.insert(0, N**2-1)
    return " -> ".join(map(str, reversed(path)))


"Test the code out"

generateGraph(N)
messagebox.showinfo('The information of the graphs',
                    remove_vertices(g, set_prob))
# Extract D and V from dijkstra algorithm to print out the results
D, V = dijkstra(g, N)
path = []
# check if D is a list
if isinstance(D, list):
    # check the value of the last element of D to see if there exists a solution and print it out
    if D[-1] == float('inf'):
        messagebox.showinfo("The optimal path", "There is no optimal path")
        print(V)

    else:
        messagebox.showinfo("The optimal distance", str(D[-1]))
        messagebox.showinfo("The optimal path", str(print_path(V)))
else:
    print(V)
    messagebox.showinfo("The optimal path", "There is no optimal path")

print('-----------#------------')
