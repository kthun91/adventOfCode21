import os
import itertools

#gets input file on every OS
script_dir = os.path.dirname(__file__) #abs script directory
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

# get the random numbers funtion
def getBingoNumbers(abs_file_path) -> list():
    with open(abs_file_path, "r") as f:
        return list(map(int, f.readline().rstrip("\n").split(',')))

# get the boards
def getBoards(abs_file_path) -> list:
    with open(abs_file_path, "r") as f:
        f.seek(0)
        boards = list()
        oneBoard = list()
        for line in f.readlines()[2::]:
            if line.split() == []:
                oneBoard.extend(generateVerticalToBoard(oneBoard))
                boards.append(oneBoard)
                #print(oneBoard)
                oneBoard = []
                continue
            liste = list(map(int, line.rstrip("\n").split()))
            makeBoardsMarkable(liste)
            oneBoard.append(makeBoardsMarkable(liste))
        return boards

def generateVerticalToBoard(board:list) -> list:
    workList = list()
    vertBoard = list()
    for i in range(len(board[0])):
        for line in board:
            workList.append(line[i])
        vertBoard.append(workList)
        workList = []
    return vertBoard

# must be markable (1)
def makeBoardsMarkable(integerList:list) -> list:
    return list(itertools.product(integerList, [0]))

# mark number
def markNumberInTuple(paar:tuple) -> tuple:
    l = list(paar)
    l[1] = 1
    return tuple(l)

# marks all numbers on board
def markBoard(board:list, num:int) -> list:
    for i1, line in enumerate(board):
        for i2, number in enumerate(line):
            if number[0] == num:
                board[i1][i2] = markNumberInTuple(number)
    return board
        
# check if board has won
def checkIfBoardHasWon(board:list) -> bool:
    return not not [line for line in board if sum(n for _, n in line) > 4] # not not to return empty list

# get all unmarked Numbers as Sum
def sumUnmarkedNumbers(board:list) -> int:
    mySum = 0
    for line in board:
        mySum += (sum([s for s, m in line if m == 0]))
    return int(mySum/2)

def bingoGame(numbers:list, board:list):
    for num in numbers:
        for board in boards:
            board = markBoard(board,num)
            if checkIfBoardHasWon(board):
                return board, num

numbers = getBingoNumbers(abs_file_path)
boards = getBoards(abs_file_path)

resultList = bingoGame(numbers, boards)
print(sumUnmarkedNumbers(resultList[0]) * resultList[1])


    