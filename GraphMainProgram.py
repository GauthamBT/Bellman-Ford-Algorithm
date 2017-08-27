from  DirectedGraphClass import *

#***********************************************************************#
#                         Bellman-Ford Algorithm                        #
#***********************************************************************#

#Provide the number of vertices
numberOfVertices = 5
#Select source of the graph
source = 0

directedGraphVar = DirectedGraph(numberOfVertices)

createDirectedGraph(directedGraphVar, source)

BellmanFordFunction(directedGraphVar)
  
directedGraphVar.printShortestPath()