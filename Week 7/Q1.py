class Node:

    def __init__(self, total):
        self.node = node
        self.adjacent = {}

    def add_Adjacent(self,adjacentList):
        self.adjacent[adjacentList]= adjacentList
        

class UnweightedGraph:
    def __init__(self):
        self.NewNodes = {}


    def addNodes(self, total):
        node = node(total)
        self.nodes[total] = node
        print("Node Added" + str(total))
        
    def addEdges(self, total, adjacentL):
        self.nodes[total].add_Adjacent(self.nodes[adjacentL])
        self.nodes[adjacentL].add_Adjacent(self.nodes[total])
        

    def PrintGraph(self):
        List = []
        for value in self.NewNodes:
            List.append(value)
        for value in List:
            print(str(value))

graph = UnweightedGraph()

graph.addNodes(1)
graph.addNodes(2)
graph.addNodes(3)
graph.addNodes(4)

graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(3, 4)

graph.PrintGraph()

            
        
