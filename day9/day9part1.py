import os
import numpy as np

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def getHeightMap(abs_file_path):
    with open(abs_file_path, "r") as f:
        rawList = list()
        for line in f.readlines():
            rawList.append(line.rsplit("\n")[0])
        heightMap = np.arange(len(rawList[0] * len(rawList))).reshape(len(rawList),len(rawList[0]))
        for x,line in enumerate(rawList):
            for y,dig in enumerate(line):
                heightMap[x][y] = int(dig)
        return heightMap

def compLeft(xCord, yCord, heightMap):
    return heightMap[xCord][yCord] < heightMap[xCord][yCord-1]

def compRight(xCord, yCord, heightMap):
    return heightMap[xCord][yCord] < heightMap[xCord][yCord+1]

def compAbove(xCord, yCord, heightMap):
    return heightMap[xCord][yCord] < heightMap[xCord-1][yCord]

def compBelow(xCord, yCord, heightMap):
    return heightMap[xCord][yCord] < heightMap[xCord+1][yCord]

def isLowPoint(xCord, yCord, heightMap) -> bool:
    if yCord == 0 and xCord == 0:
        #vgl r,u
        return compRight(xCord, yCord, heightMap) and compBelow(xCord, yCord, heightMap)
    if xCord == 0 and yCord == (len(heightMap[0])-1):# not used
        #vgl l,u
        return compLeft(xCord, yCord, heightMap) and compBelow(xCord, yCord, heightMap)
    if xCord == 0 and yCord == (len(heightMap[0])-1):
        #vgl o,r
        return compAbove(xCord, yCord, heightMap) and compRight(xCord, yCord, heightMap)
    if xCord == (len(heightMap)) and yCord == (len(heightMap[0])-1):
        #vgl l,o
        return compLeft(xCord, yCord, heightMap) and compAbove(xCord, yCord, heightMap)
    if xCord == 0:
        # vgl l,r,u
        return compLeft(xCord, yCord, heightMap) and (compRight(xCord, yCord, heightMap) and compBelow(xCord, yCord, heightMap))
    if xCord == (len(heightMap)-1):
        # vgl l,r,o
        return compLeft(xCord, yCord, heightMap) and (compRight(xCord, yCord, heightMap) and compAbove(xCord, yCord, heightMap))
    if yCord == 0:
        # vgl o,u,r
        return compRight(xCord, yCord, heightMap) and (compAbove(xCord, yCord, heightMap) and compBelow(xCord, yCord, heightMap))
    if yCord == (len(heightMap[0])-1):
        #vgl o,l,u
        return compAbove(xCord, yCord, heightMap) and (compLeft(xCord, yCord, heightMap) and compBelow(xCord, yCord, heightMap))
    else:
        #vgl o,u,l,r
        return (compLeft(xCord, yCord, heightMap) and compAbove(xCord, yCord, heightMap)) and (compRight(xCord, yCord, heightMap) and compBelow(xCord, yCord, heightMap))

heightMap = getHeightMap(abs_file_path)
lowPoints = list()
for x in range(0, len(heightMap)):
    for y in range(0, len(heightMap[0])):
        if isLowPoint(x,y,heightMap):
            lowPoints.append(heightMap[x][y])
print(sum(list(map(lambda x: x+1, lowPoints))))


        
