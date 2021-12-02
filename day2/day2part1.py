import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def generateListofFile(abs_file_path):
    with open(abs_file_path, "r") as f:
        directions = list()
        for x in f.readlines():
            directions.append(x.rstrip("\n"))
        return directions

#print(generateListofFile(abs_file_path))
horizontal = 0
depth = 0

for i in generateListofFile(abs_file_path):
    if "forward" in i:
        horizontal += [int(s) for s in i.split() if s.isdigit()][0]
    if "up" in i:
        depth -= [int(s) for s in i.split() if s.isdigit()][0]
    if "down" in i:
        depth += [int(s) for s in i.split() if s.isdigit()][0]
print(f"horizontal position of {horizontal} and a depth of {depth}")
print(f"multiplied is {horizontal * depth}")