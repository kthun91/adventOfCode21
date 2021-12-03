import os
import math
import time

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def generateListofFile(abs_file_path):
    with open(abs_file_path, "r") as f:
        report = list()
        for x in f.readlines():
            report.append(x.rstrip("\n"))
        return report

def getOxy(report, bitPosition):
    if len(report) == 1:
        return report
    if (sum([int(repPosition[bitPosition]) for repPosition in report])) >= math.ceil(len(report)/2):
        return(getOxy([repPosition for repPosition in report if repPosition[bitPosition] == '1'], bitPosition+1))
    else:
        return(getOxy([repPosition for repPosition in report if repPosition[bitPosition] == '0'], bitPosition+1))

    
def getCar(report, bitPosition):
    if len(report) == 1:
        return report
    if (len(report) - (sum([int(repPosition[bitPosition]) for repPosition in report]))) <= int(len(report)/2):
        return(getCar([repPosition for repPosition in report if repPosition[bitPosition] == '0'], bitPosition+1))
    else:
        return(getCar([repPosition for repPosition in report if repPosition[bitPosition] == '1'], bitPosition+1))

start = time.time()
report = generateListofFile(abs_file_path)
oxy = int(getOxy(report, 0)[0], 2)
car = int(getCar(report, 0)[0], 2)

print(oxy * car)
print(f"{(time.time() - start)*1e3} ms")