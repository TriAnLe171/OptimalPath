Overview

This Python program is an implementation of graph pathfinding using Dijkstra’s algorithm. The primary goal is to generate a grid graph, block a portion of the vertices based on user input, and then find the optimal path from the first vertex (0) to the last vertex (N² - 1). The program provides a graphical user interface (GUI) using tkinter for user input, visualization using networkx and matplotlib, and displays the results in message boxes.

Features

1.	Graph Generation:
•	A grid graph with ￼ vertices is generated based on user input.
•	Edges connect adjacent vertices horizontally and vertically.
2.	Blocked Vertices:
•	A percentage of the graph’s vertices is blocked (removed) based on user-defined probability.
•	The original graph and the blocked graph are visualized side-by-side.
3.	Pathfinding Using Dijkstra’s Algorithm:
•	The program finds the shortest path from the first vertex to the last vertex.
•	If a solution exists, the optimal path and distance are displayed.
•	If no solution exists, an appropriate message is shown.

Requirements

•	Python 3.x
•	Libraries used:
•	tkinter: For GUI input and message display.
•	networkx: For graph representation and manipulation.
•	matplotlib: For visualizing the graphs.
•	Custom imports: LinkedDirectedGraph, LinkedQueue, LinkedStack.

How to Run the Program

python optimal_path.py


How the Program Works

1.	User Input:
•	Number of Vertices (N): The user provides the size of the grid graph (N x N).
•	Blocking Probability: The user inputs a value between 0 and 1 to set the proportion of blocked vertices.
2.	Graph Generation and Visualization:
•	Two graphs are generated and displayed:
•	Original Graph: Contains all vertices and edges.
•	Blocked Graph: Some vertices are removed based on the given probability.
3.	Pathfinding:
•	The program uses Dijkstra’s algorithm to find the shortest path from vertex 0 to vertex N²-1.
•	If a path exists, it prints and shows the path along with the total distance.
•	If no path exists, the program informs the user.

Code Flow

1.	Graph Generation (generateGraph): Adds vertices and edges to the graph based on user input.
2.	Graph Visualization (sketchGraph): Uses networkx to plot both the original and blocked versions of the graph.
3.	Dijkstra’s Algorithm (dijkstra): Finds the shortest path from vertex 0 to vertex N²-1.
4.	Vertex Removal (remove_vertices): Blocks a percentage of vertices as per user input.
5.	Displaying Results:
•	If a valid path is found, the path and distance are shown in a message box.
•	If no path is available, the user is informed through a message box.

Example Walkthrough

1.	Input:
•	Number of vertices: 4
•	Blocking probability: 0.2
2.	Graphs:
•	The original graph is generated with all nodes connected.
•	20% of the vertices are blocked in the blocked graph.
3.	Result:
•	If a valid path exists, the shortest path and distance are displayed.
•	If no valid path exists, a message informs the user.

Potential Issues and Debugging

1.	Negative Inputs: If the user enters a negative number for N or set_prob, the program re-prompts for valid input.
2.	Blocked Graph Disconnected: If too many vertices are blocked, the graph may become disconnected, resulting in no valid path.
3.	Custom Modules: Ensure LinkedDirectedGraph, LinkedQueue, and LinkedStack are implemented correctly to avoid import issues.

Conclusion

This program demonstrates the practical application of Dijkstra’s algorithm to solve a graph-based pathfinding problem with blocked vertices. It provides a simple GUI for user interaction, graphical visualization of graphs, and informative messages for the optimal path and distance.
