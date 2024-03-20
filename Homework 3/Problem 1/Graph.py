from Vertex import *
from queue import Queue

class Graph:
    def __init__(self, filename):
        adjLabels = self.loadGraphFromFile(filename)  # initially it's only labels
        # creating Vertex objects using the labels, head of lists
        self.V = []
        for l in adjLabels:
            self.V.append(Vertex(l[0]))
        # changing the labels into references to objects in the list of lists
        n = len(adjLabels)
        for i in range(n):  # to select a Vertex objects in V
            label = self.V[i].label
            for j in range(n):  # to iterate through the lists
                try:
                    k = adjLabels[j].index(label)  # check whether the label appears in this adj list
                    adjLabels[j][k] = self.V[i]  # replace the simple label by a reference to the vertex
                except ValueError:
                    pass
        # creating the adjacency list as a dictionary
        self.adjLists = dict()
        for i in range(len(adjLabels)):  # to select a vertex from self.V
            self.adjLists[self.V[i]] = adjLabels[i][1:]

    def loadGraphFromFile(self, filename):
        labelLists = []
        infile = open(filename)
        for line in infile:
            labelLists.append(line.rstrip().split(","))
        return labelLists

    def __str__(self):
        output = ""
        for v in self.V:
            output += str(v) + "->"
            for u in self.adjLists[v][:-1]:
                output += str(u) + "->"
            output += str(self.adjLists[v][-1]) + "\n"
        return output
    
    def isBipartite(self):
        """ input: Graph self with self.V is the list of Vertex objects (head of lists).\\
            output: returns True if the Graph is bipartite and False otherwise with corresponding messages.\\
            additional data structures used: colorX is a dictionary with information about colors (gray (0) or black (1)) of each vertex in the Graph.  
        """
        colorX = {}  # creating the color of vertices as dictionary
        for s in self.V:
            colorX[s.label] = None  # initializing colors to None
        
        # function to check if the graph is bipartite starting from a vertex
        def bfs(s):
            """ input: Graph self with self.adjLists being its adjacency list as dictionary.\\
                       s is a vertex of Graph.\\
                       colorX is additional dictionary to store colors of each vertex of Graph.\\
                output: Each visited vertex will be colored either gray (0) or black (1) and function returns True if the graph is bipartite and False otherwise.\\
                additional data structures used: Q = Queue() a queue of vertices.  
            """
            Q = Queue() # creating empty queue
            Q.put(s) # Enqueue(Q, v)
            colorX[s.label] = 0  # coloring the starting vertex gray (0)
            
            while not Q.empty():
                u = Q.get() # Dequeue(Q)
                for v in self.adjLists[u]:
                    if colorX[v.label] is None:  # if the neighbor of u has not been colored yet
                        colorX[v.label] = 1 - colorX[u.label] # coloring the neighbor of u with a color opposite to color of u
                        Q.put(v) # Enqueue(Q, v)
                    elif colorX[v.label] == colorX[u.label]:  # if the neighbor of u has the same color as u
                        return False  # not bipartite
            return True  # bipartite
        
        # checking each component of the graph
        for s in self.V:
            if colorX[s.label] is None:
                if bfs(s) is False:
                    print("This graph is not bipartite.")
                    return False
        
        # once we reach here it means that the graph is bipartite
        grayX = [v.label for v in self.V if colorX[v.label] == 0]
        blackX = [v.label for v in self.V if colorX[v.label] == 1]
        print(f"This graph is bipartite as follows:\n{', '.join(grayX)}\n{', '.join(blackX)}")
        return True