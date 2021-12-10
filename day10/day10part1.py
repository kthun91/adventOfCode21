import os

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

def getList(abs_filepath) -> list:
    result = list()
    with open(abs_file_path, "r") as f:
        for line in f.readlines():
            result.append(line.rsplit("\n")[0])
        return result

def isOpposite(closing, stackChar, charDict):
    return closing == charDict.get(stackChar)

def getIncorrectChar(line, charDict):
    stack = list()
    for char in line:
        if char in charDict:  # first is always opening char
            stack.append(char)
        else:
            if len(stack) == 0:  # stack got popped empty
                continue
            if isOpposite(char, stack[-1], charDict):
                stack.pop(-1)
            else:
                return char

charDict = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}

scoreDict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
    'None': 0
}

# x = True if '[' in charDict else False
counter = 0
chunkList = getList(abs_file_path)
for line in chunkList:
    val = scoreDict.get((getIncorrectChar(line, charDict)))
    counter += int(0 if val is None else val)
print(counter)