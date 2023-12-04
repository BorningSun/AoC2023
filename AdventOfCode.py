puzzle1input = "p1_input.txt"

def solvePuzzle1():
    listOfDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    resultDict = {}
    listOfDoubleDigits = []
    result = 0
    with open(puzzle1input) as f:
        for line in f.readlines():
            for char in line:
                if char in listOfDigits:
                    if line in resultDict:
                        resultDict[line] = resultDict[line] + char
                    else:
                        resultDict[line] = char
    for strDigits in resultDict.values():
        if len(strDigits) == 1:
            listOfDoubleDigits.append(strDigits+strDigits)
        else:
            firstD, lastD = strDigits[0], strDigits[-1]
            listOfDoubleDigits.append(firstD+lastD)
    for n in range(1000):
        listOfDoubleDigits[n] = int(listOfDoubleDigits[n])
        result = result + listOfDoubleDigits[n]
    print(result)



solvePuzzle1()