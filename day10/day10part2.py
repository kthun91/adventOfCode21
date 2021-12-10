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

def getValidList(abs_file_path, charDict) -> list:
    rawList = getList(abs_file_path)
    incorrect = list()
    for line in rawList:
        incorrect.append(getIncorrectLine(line, charDict))
    return list(set(rawList) - set(incorrect))

def getIncorrectLine(line, charDict) -> list:
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
                return line

def getUnclosed(line, charDict):
    stack = list()
    for char in line:
        if char in charDict:  # first is always opening char
            stack.append(char)
        else:
            if len(stack) == 0:  # stack got popped empty
                continue
            if isOpposite(char, stack[-1], charDict):
                stack.pop(-1)
    return stack

charDict = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}

scoreDict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
    'None': 0
}

valid = getValidList(abs_file_path,charDict)
totalPoints = list()
for v in valid:
    missingBrackets = getUnclosed(v, charDict)
    revMissing = list(reversed(missingBrackets))
    score = 0
    for r in revMissing:
        score = score * 5 + scoreDict.get(charDict.get(r))
    totalPoints.append(score)
middle = (len(totalPoints) // 2 )
print(sorted(totalPoints)[middle])

