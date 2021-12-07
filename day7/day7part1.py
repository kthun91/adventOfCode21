import os

# gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# get list of numbers
def getListOfPositions(abs_file_path) -> list:
    positions = list()
    with open(abs_file_path, "r") as f:
        return list(map(int,(f.readline().split(","))))
    
pos = getListOfPositions(abs_file_path)
countList = list()
for i in range(min(pos),(max(pos)+1)): # possible positions
    counter = 0
    for elem in pos:
        counter += abs(elem-i)
    countList.append(counter)

print(min(countList))