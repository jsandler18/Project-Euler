from graph import Graph 
f = open("matrix.txt","r")
data = f.read()
f.close()

size = 80

g = Graph()

for row in range(size):
    for col in range(size):
        g.add_node("%d,%d" % (row,col))
    g.add_node("START%d"%row)
    
print "Done adding nodes"

data2 = data.split("\n")
data = []
for i in data2:
    data += i.split(",")


#add rest of edges
for row in range(size):
    for col in range(size):
        #get src node name and right and down and up node names
        src = "%d,%d" % (row,col)
        down = "%d,%d" % (row+1, col)
        right = "%d,%d" % (row, col+1)
        up = "%d,%d" % (row - 1, col)
        g.add_edge(src, right, int(data[(size)*row + col + 1])) if (size)*row + col + 1 < size * size else None
        g.add_edge(src, down, int(data[(size)*(row+1) + col])) if (size)*(row+1) + col < size * size else None
        g.add_edge(src, up, int(data[(size)*(row-1) + col])) if (size)*(row-1) + col >= 0 else None
    #add edges between starting points and each node in column one
    g.add_edge("START%d"%row, "%d,0"%row, data[size*row])

print "done adding edges"

result = []
for i in range(size):
    print "dijkstra from START%d" %i
    dr = g.dijkstra("START%d"%i)
    for node, dist in dr.iteritems():
        if "START" in node:
            continue
        #if the node is in the last column,add its distance to the result
        if node[node.index(",")+1:] == str(size-1):
            result.append(dist[0])

print min(result)

