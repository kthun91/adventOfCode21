import os
import time

# gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# get list of numbers
def getListOfPositions(abs_file_path) -> list:
    positions = list()
    with open(abs_file_path, "r") as f:
        return list(map(int,(f.readline().split(","))))

start = time.time()

pos = getListOfPositions(abs_file_path)
countList = list()
pos.sort()
for i in range(min(pos),(max(pos)+1)): # possible positions
    counter = 0
    for elem in pos:
        for cost in range(1,abs(elem-i)+1):
            counter += cost
    countList.append(counter)

print(min(countList))
print(f"{(time.time() - start)*1e3} ms")