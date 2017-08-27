import sys

#Class to represent the graph
class DirectedGraph:
    def __init__(self, v):
        self.noOfVerticies = v
        self.adjacencyListArray = [{}]
        self.adjacencyListArray.clear()
        self.shortestPathArray = []
        self.shortestPathArray.clear()
        self.visitedArray = []
        self.visitedArray.clear()
        self.graphQueue = []
        self.graphQueue.clear()
        
        for i in range(v):
            self.adjacencyListArray.append({})
        
        for j in range(v):
            self.shortestPathArray.append(sys.maxsize)
            
        for k in range(v):
            self.visitedArray.append(False)
    
    #To print the graph representation
    def printGraph(self):
        for i in range(0,self.noOfVerticies):
            print ("For",i,"=",self.adjacencyListArray[i])
            
    #To print the shortest path
    def printShortestPath(self):
        for i in range(self.noOfVerticies):
            print ("Bellman-Ford",i,"=",self.shortestPathArray[i])

#Function to add edges and their weight
def addEdge(graph, src, dest, weight):
    #Saving neighbors and weights in dicts
    graph.adjacencyListArray[src].__setitem__(dest,weight)

def BellmanFordFunction(graph):
    #Peforming dijkstras on all nodes
    while graph.graphQueue != list():
        BellmanFordFunctionAlgorithm(graph, graph.graphQueue.pop())

def BellmanFordFunctionAlgorithm(graph, source):
    #if the source has been visited, return
    if graph.visitedArray[source] == True:
        return
    
    tempArray = [] #To temporarily store the adjacenet sums
    tempArray.clear()
    leastIndex = 0 #To store the least element's index
    minValue = sys.maxsize #Value used to store the minimum value
    
    #print ("Before the adjacencyListArray Loop")
    #graph.adjacencyListArray[source] = Gives the list of adjacent nodes for the source
    #graph.adjacencyListArray[source].keys() = These are the keys of the adjacent node dict
    #list(graph.adjacencyListArray[source].keys())[i] = Gives linear access to the keys of adjacent nodes dict
    for i in range(graph.adjacencyListArray[source].__len__()):
        #tempAdd = Is a temporary value to store the new distance calculated
        tempAdd = graph.shortestPathArray[source] + graph.adjacencyListArray[source][list(graph.adjacencyListArray[source].keys())[i]]
        tempArray.append(tempAdd)
        
        #Updating the shortest path array
        if graph.shortestPathArray[list(graph.adjacencyListArray[source].keys())[i]] > tempAdd:
            graph.shortestPathArray[list(graph.adjacencyListArray[source].keys())[i]] = tempAdd
            graph.graphQueue.insert(0,list(graph.adjacencyListArray[source].keys())[i])
            graph.visitedArray[list(graph.adjacencyListArray[source].keys())[i]] = False            
            
    #Adding the remaining neighbors to the queue
    i = 0
    for i in range(graph.adjacencyListArray[source].__len__()):
        #Checking if the node has been visited already or if it is already in the queue
        if graph.visitedArray[list(graph.adjacencyListArray[source].keys())[i]] == False and list(graph.adjacencyListArray[source].keys())[i] not in graph.graphQueue:
            graph.graphQueue.insert(0,list(graph.adjacencyListArray[source].keys())[i])
    
    #Marking the node as visited
    graph.visitedArray[source] = True
    
    #print ("source =",source,"End of BellmanFord algorithm", graph.shortestPathArray)
    #print ("Graph Queue",graph.graphQueue)



#Function to create graph
def createDirectedGraph(graph, source):
    #Making the source as 0.
    graph.shortestPathArray[source] = 0
    #Initiating the stack with source node
    graph.graphQueue.insert(0,source)
    
    #Adding edges to the directedGraph
    #0->1
    addEdge(graph, 0, 1, 4)
    #0->2
    addEdge(graph, 0, 2, 2)
    #1->2
    addEdge(graph, 1, 2, 3)
    #1->3
    addEdge(graph, 1, 3, 2)
    #1->4
    addEdge(graph, 1, 4, 3)
    #2->1
    addEdge(graph, 2, 1, 1)
    #2->3
    addEdge(graph, 2, 3, 4)
    #2->4
    addEdge(graph, 2, 4, 5)
    #4->3
    addEdge(graph, 4, 3, -5)