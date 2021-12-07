import os
from collections import deque

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# faster
with open(abs_file_path, "r") as f:
    value = 0
    end = 256
    fish = f.readline()
    fish = list(map(int, fish.split(',')))
    age = deque()
    for i in range(0,9):
        age.append(fish.count(i))
    print(age)
    for day in range(0,end):
        value = age[0]
        age.rotate(-1)
        age[6] += value
    print(sum(age))
