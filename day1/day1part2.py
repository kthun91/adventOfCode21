import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# using zip would be better
def getListOfThree(abs_file_path):
    with open(abs_file_path, "r") as f:
        rawList = list()
        depths = list()
        for x in f.readlines():
            rawList.append(x.rstrip("\n"))      
        for i in range(len(rawList)):
            if i > 1997:
                break
            depths.append(int(rawList[i]) + int(rawList[i+1]) + int(rawList[i+2]))
        return depths

sumOfDepths = getListOfThree(abs_file_path)
currentValue = sumOfDepths[0]
counter = 0
for i in sumOfDepths[1:]:
    if (int(i) - int (currentValue)) > 0:
        counter += 1
    currentValue = i
print(counter)