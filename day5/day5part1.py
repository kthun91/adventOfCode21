import os
import numpy as np

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# get coordinates
def getCords(abs_file_path):
    with open(abs_file_path, "r") as f:
        coordinatesRaw = list()
        coordinates = list()
        for line in f.readlines():
            coordinatesRaw.append(line.rsplit("\n"))
        for line in coordinatesRaw:
            coordinates.append(line[0].split(" -> "))
        return(coordinates)
        
def getHorLines(cords: list) -> list:
    cords2 = list()
    for cord in cords:
        x1,y1 = cord[0].split(",")
        x2,y2 = cord[1].split(",")
        if y1 == y2:
            cords2.append(list(map(int,[x1,y1,x2,y2])))
    return cords2 

def getVerLines(cords: list) -> list:
    cords2 = list()
    for cord in cords:
        x1,y1 = cord[0].split(",")
        x2,y2 = cord[1].split(",")
        if x1 == x2:
            cords2.append(list(map(int,[x1,y1,x2,y2])))
    return cords2 

def markMatrix(matrix, cords):
    hor = getHorLines(cords)
    for cord in hor:
        x1 = cord[0] #0
        x2 = cord[2] #5
        y1 = cord[1] #9
        if x1 < x2:
            for x in range(x1,x2+1):
                matrix[y1][x] += 1
        else:
            for x in range(x2,x1+1):
                matrix[y1][x] += 1
    ver = getVerLines(cords)
    for cord in ver:
        x1 = cord[0]
        y1 = cord[1]
        y2 = cord[3]
        if y1 < y2:
            for y in range(y1,y2+1):
                matrix[y][x1] += 1
        else:
            for y in range(y2,y1+1):
                matrix[y][x1] += 1
    return matrix

# x1,y1 -> x2,y2
x = np.zeros((1000,1000))
cords = getCords(abs_file_path)
print(markMatrix(x,cords))

over2 = list()
for i  in range(len(x)):
    for j in range(len(x[i])):
        if x[i][j] > 1:
            over2.append(x[i][j])
print(len(over2))
