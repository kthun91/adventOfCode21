import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    depths = list()
    for x in f.readlines():
        depths.append(x.rstrip("\n"))      
    currentValue = depths[0]
    counter = 0
    for i in depths[1:]:
        if (int(i) - int (currentValue)) > 0:
            counter += 1
        currentValue = i
    print(counter)
    