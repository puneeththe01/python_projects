import random
import time

# x and y are random Coordinates  
x = 0 
y = 0

# variables
no_of_deers = 0
no_of_grass = 0
list_of_deers = {}
list_of_grass = {}

## genarate random coordinates and assign them to x and y
def randgenarater():
    global x, y
    x = random.randint(0,100)
    y = random.randint(0,100)

# genarate a new dear in the enviroment
def newDeer():
    randgenarater()
    global no_of_deers
    global list_of_deers
    name = f'deer{no_of_deers}'
    no_of_deers+= 1
    list_of_deers.update({name: {"energy": 10, "hungry": 10, "x-axis":x, "y-axis": y}})


# genarate a new grass in the enviroment
def newGrass():
    randgenarater()
    global no_of_grass, list_of_grass
    name = f'grass{no_of_grass}'
    no_of_grass+= 1
    list_of_grass.update({name: {"x-axis": x, "y-axis": y, "energy": 2}})


# this function find the grass near by the dear
def findGrass(deerName):
    # create a local varbiales in the function
    grass_x = []
    grass_y = []
    deer_x = []
    deer_y = []
    for i in range(no_of_grass):
        name = f'grass{i}'
        grass_x.append(list_of_grass[name]["x-axis"])
        grass_y.append(list_of_grass[name]["y-axis"])
    x_axis = list_of_deers[deerName]["x-axis"]
    y_axis = list_of_deers[deerName]["y-axis"]
    deer_x.append(x_axis)
    deer_y.append(y_axis)
    for n in range(1,11):
        deer_x.append(x_axis+n)
        deer_y.append(y_axis+n)
    for m in range(1, 11):
        deer_x.append(x_axis-m)
        deer_y.append(y_axis-m)
    print(deer_x, "x deer")
    print(grass_x, "xg")
    print(deer_y,"y deer")
    print(grass_y, "yg")
    index_d = 0
    # looping to find the coordinates of the grass and the deer are matching to move the deer towards the grass
    for a in deer_x:
        #temp varibales in this for loop
        index_g = 0 
        for x in grass_x:
            if x == a:
                if deer_y[index_d] == grass_y[index_g]:
                    print(f"location was found at the ({a}, {deer_y[index_d]})")
                    print(f"Index number of the grass is at {index_g} and {x}")
            index_g += 1
        index_d += 1


for i in range(5):
    newDeer()
    for i in range(200):
        newGrass()

findGrass('deer0')


print(no_of_deers)
print(no_of_grass)
print(list_of_deers)
