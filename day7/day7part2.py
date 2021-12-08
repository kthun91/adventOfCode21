import os
from line_profiler import LineProfiler

# gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# get list of numbers
def getListOfPositions(abs_file_path) -> list:
    positions = list()
    with open(abs_file_path, "r") as f:
        return list(map(int,(f.readline().split(","))))

def main():
    pos = getListOfPositions(abs_file_path)
    smallest = max(pos)
    pos.sort()
    for i in range(min(pos),(max(pos)+1)): # possible positions
        counter = 0
        for elem in pos:
            # avoids expensive abs() calls
            if elem > i:
                absEnd = (elem-i) + 1
            else:
                absEnd = (i-elem) + 1
            for cost in range(1,absEnd):
                counter += cost
        if smallest > counter:
            smallest = counter
    print(smallest)

if __name__ == "__main__":
    lp = LineProfiler()
    lp_wrapper = lp(main())
    lp.print_stats()