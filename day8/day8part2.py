import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

#get input as list [ten, four]
def getList(abs_file_path):
    with open(abs_file_path, "r") as f:
        digits = list()
        for line in f.readlines():
            ten, four = line.rsplit("\n")[0].split(" | ")
            digits.append([ten, four])
        return digits
        
def getNumbers(inputline):
    number = [0] * 10
    fiver = list()
    sixer = list()
    char = [0] * 7
    for elem in set(inputline[0].split()):
        if len(elem) == 2:
            number[1] = elem
        if len(elem) == 3:
            number[7] = elem
        if len(elem) == 4:
            number[4] = elem
        if len(elem) == 7:
            number[8] = elem
        if len(elem) == 6:
            sixer.append(elem)
        if len(elem) == 5:
            fiver.append(elem)
    char[0] = set(number[7]) - set(number[1])
    char[2] = set(number[1])
    char[5] = set(number[1])
    char[1] = set(number[4]) - set(number[7])
    char[3] = set(number[4]) - set(number[7])
    for six in sixer:
        if not char[2].issubset(set(six)):
            number[6] = six
    char[2] -= set(number[6])
    char[5] -= char[2]
    for six in sixer:
        if not char[1].issubset(set(six)):
            number[0] = six
    char[3] -= set(number[0])
    char[1] -= char[3]
    sixer.remove(number[0])
    sixer.remove(number[6])
    number[9] = sixer[0]
    char[4] = set(number[8]) - set(number[9])
    char[6] = set(number[0]) - set(number[7]) - char[1] - char[4]
    for five in fiver:
        if char[4].issubset(set(five)): 
            number[2] = five
        if char[1].issubset(set(five)): 
            number[5] = five
        if char[2].issubset(set(five)) and char[5].issubset(set(five)): 
            number[3] = five
    return number

input = getList(abs_file_path)
counter = 0
for inputline in input:
    output = ""
    numbers = getNumbers(inputline)
    for digit in inputline[1].split():
        for idx,number in enumerate(numbers):
            if set(number) == set(digit):
                output += str(idx)
    counter += int(output)
print(counter)
    
            
