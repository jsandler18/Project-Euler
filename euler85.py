target = 2000000
mindist = 999999999
mindim = '0x0'
minarea = 0
#loop through areas
for area in range(1900,3000):
    print area
    #loop through possible dimensions that make that area
    for width in range(1,area + 1):
        if area % width == 0:
            height = area/width
            possibilities = 0
            for w in range(1,width+1):
                for h in range(1, height+1):
                    possibilities += (width-w+1)*(height-h+1)
            if abs(target-possibilities) < mindist:
                mindist = abs(target-possibilities)
                mindim = "%d,%d" % (width, height)
                minarea = area

print mindist
print mindim
print minarea
                    
