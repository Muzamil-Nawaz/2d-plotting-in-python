import math

def distance(x1 , y1 , x2 , y2):
    return math.sqrt(math.pow(x2 - x1, 2) +math.pow(y2 - y1, 2) * 1.0)



x1 = int(input("Enter x for point 1 : "))
y1 = int(input("Enter y for point 1:"))

x2 = int(input("Enter x for point 2 : "))
y2 = int(input("Enter y for point 2:"))



if x1 =="" or x2 == "" or y1 =="" or y2 == "":
    print("Invalid input, point values can't be empty, quitting program")
    pass
else:
    print("Distance between points ("+str(x1)+","+str(y1)+") ("+str(x2)+","+str(y2)+") is "+str(distance(x1,y1,x2,y2)))

    
# import matplotlib.pyplot as plt
#     x = [x1,x2]
#     y = [y1,y2]
    
#     from mpl_toolkits.axisartist import SubplotZero

#     # Create the cartesian axis
#     axes = Axes(xlim=(-1,8), ylim=(-1,18), figsize=(9,7))

#     # Create two points
#     p1 = Point(x1,  y1, color='#ffa500')
#     p2 = Point(x2, y2, color='#0000ff')

#     axes.addPoints([p1, p2])
#     axes.draw()

