from graph import Graph 
f = open("matrix.txt","r")
data = f.read()
f.close()

size = 80
g = Graph()
g.add_node("START")
for row in range(size):
    for col in range(size):
        g.add_node("%d,%d" % (row,col))

data2 = data.split("\n")
data = []
for i in data2:
    data += i.split(",")


#set start and end points
g.add_edge("START", "0,0", data[0])
#add rest of edges
for row in range(size):
    for col in range(size):
        #get src node name and right,left,up and down node names
        src = "%d,%d" % (row,col)
        down = "%d,%d" % (row+1, col)
        right = "%d,%d" % (row, col+1)
        up = "%d,%d" % (row-1,col)
        left = "%d,%d" % (row, col-1)
        g.add_edge(src, right, int(data[(size)*row + col + 1])) if ((size)*row + col + 1) % size > ((size)*row + col) % size else None
        g.add_edge(src, down, int(data[(size)*(row+1) + col])) if (size)*(row+1) + col < size * size else None
        g.add_edge(src, left, int(data[(size)*(row) + col - 1])) if ((size)*(row) + col - 1) % size < ((size)*(row) + col) % size else None
        g.add_edge(src, up, int(data[(size)*(row-1) + col])) if (size)*(row-1) + col >= 0 else None


print g.get_dist("START","%d,%d" % (size-1,size-1))
