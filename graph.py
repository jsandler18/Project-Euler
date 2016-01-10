from sys import maxint as MAX
class Graph:
    """An object to represent a directed graph. It is self contained."""
                   
    def __init__(self):
        self.nodes = {}

    """adds a node to the graph if it does not exist and returns true,returns false otherwise"""
    def add_node(self, name):
        if not name in self.nodes:
            self.nodes[name] = {}
            return True
        return False

    """adds an edge from node1 to node2 and returns true, returns false if either
    node doesn't exist or the cost is negative"""
    def add_edge(self, node1, node2, cost):
        if cost >= 0 and node1 in self.nodes and node2 in self.nodes:
            self.nodes[node1][node2] = cost
            return True
        return False
                
            
    """removes an edge from node1 to node2. returns true if successful and false
    if there is no edge or if either node doesn't exist"""
    def remove_edge(self, node1,node2):
        if node1 in self.nodes and node2 in self.nodes and node2 in self.nodes[node1]:
            del self.nodes[node1][node2]
            return True
        return False

    """removes a node and all edges to and from it and returns true of successful.
    returns false if the node doesn't exist"""
    def remove_node(self, node):
        if node in self.nodes:
            del self.nodes[node]
            for key, value in self.nodes.iteritems():
                if node in value:
                    del value[node]
            return True
        return False

    def __str__(self):
        result = ""
        for key, val in self.nodes.iteritems():
            result += "\t" + key + " : " + str(val) + "\n"
        return result

    """returns a dictionary that has all nodes
    in the graph  as keys and  a 2-tuple
    containing the relative distance from the given starting node,
    and the preceding node. it returns the data structures used
    in dijkstra's algorithm"""
    def dijkstra(self, startnode):
        unprocessed = {}
        processed = {}
        for node in self.nodes:
            unprocessed[node] = [MAX, None]
        unprocessed[startnode] = [0, None]
        while len(self.nodes) > len(processed):
            smallest = MAX
            smallestnode = None
            #find smallest distance not yet processed
            for key, val in self.nodes.iteritems():
                if not key in processed and unprocessed[key][0] < smallest:
                    smallest = unprocessed[key][0]
                    smallestnode = key
            #end loop if all nodes are reached but not all are processed
            if smallestnode == None:
                break
            #iterate through unprocessed neighbors
            for key, val in self.nodes[smallestnode].iteritems():
                #if the neighbor is unprocessed
                if not key in processed:
                    #if the distance to this smallest node plus the distnce to the next
                    #node  from this smallest node is less than the distance given, reset the distance
                    if (smallest + int(self.nodes[smallestnode][key])) < unprocessed[key][0]:
                        unprocessed[key][0] = smallest + int(self.nodes[smallestnode][key])
                        unprocessed[key][1] = smallestnode
            #set the smallest as processed
            processed[smallestnode] = unprocessed[smallestnode]
            del unprocessed[smallestnode]
                    
            
        #process all unreachable nodes
        for key, val in unprocessed.iteritems():
            processed[key] = val
        return processed

    """returns an ordered list that contains the path from startnode to endnode"""
    def get_path(self,start,end):
        dr = self.dijkstra(start)
        pre = dr[end][1] # get destinations predecesor
        result = [end]
        while pre != None:
            result.insert(0,pre)
            pre = dr[result[0]][1]
        return result

    """gets the shortest distance between two nodes"""
    def get_dist(self, start,end):
        dr = self.dijkstra(start)
        return dr[end][0]
                    




















