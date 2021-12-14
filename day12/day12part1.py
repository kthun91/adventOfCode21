import os
import numpy as np

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def getPoints(abs_file_path):
    paper = np.zeros((894,1311))  # max+1 of x,y
    with open(abs_file_path, "r") as f:
        for line in f.readlines():
            x,y = line.split(",")
            paper[int(y)][int(x)] = 1
    return paper

def foldY(y, paper):
    i = 0
    while i != y:
        for x in range(0, len(paper[0])):
            paper[i][x] += paper[-(i+1)][x]
        i += 1
    return paper[0:-1][0:-y]

def foldX(x, paper):
    i = 0
    while i != x:
        for y in range(0, len(paper)):
            paper[y][i] += paper[y][-(i+1)]
        i += 1
    return paper[:,:x]

def countDots(paper) -> int:
    return sum([True for y in paper for x in y if x > 0])

paper = getPoints(abs_file_path)

paper = (foldX(655,paper))

print(countDots(paper))
