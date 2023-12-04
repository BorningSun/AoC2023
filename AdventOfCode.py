import re

puzzle1input = "p1_input.txt"
test = "inputtest.txt" # gives 281

def solvePuzzle1p1():
    resultDict = {}
    result = 0
    with open(puzzle1input) as f:
        for line in f.readlines():
            for char in line:
                if char.isdigit():
                    if line in resultDict:
                        resultDict[line] = resultDict[line] + char
                    else:
                        resultDict[line] = char
    for line, strDigits in resultDict.items():
        if len(strDigits) == 1:
            resultDict[line] = int(strDigits+strDigits)
        else:
            resultDict[line] = int(strDigits[0] + strDigits[-1])
        result = result + resultDict[line]
    print(result)


#solvePuzzle1p1()


def solvePuzzle1p2():
    paterns = {
        "0":"zero",
        "1":"one",
        "2":"two",
        "3":"three",
        "4":"four",
        "5":"five",
        "6":"six",
        "7":"seven",
        "8":"eight",
        "9":"nine"
    }
    with open(test) as f:
        for line in f.readlines():
            print(line)

solvePuzzle1p2()
