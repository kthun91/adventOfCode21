import os

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

def flipString(string):
    return ''.join('1' if x == '0' else '0' for x in string)

report = generateListofFile(abs_file_path)
gamma = ""
epsilon = ""
for binPosition in range(len(report[0])):
    if (sum(int(repPosition[binPosition]) for repPosition in report)) > int(len(report)/2):
        gamma += "1"
    else:
        gamma += "0"

result = int(gamma, 2) * int(flipString(gamma), 2)
print(result)