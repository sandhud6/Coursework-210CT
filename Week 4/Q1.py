def Binary_Search(List, high, low): # variable name defined 
    firstLow = 0 # the first number to be in the list
    lastHigh = len(List)-1 # the last number in the list
    answer = False

    while firstLow <= lastHigh and not answer:
        middleValue = (firstLow + lastHigh) // 2
        if List[middleValue] > high and List[middleValue] < low:
            answer = True

        else:
            if high < List[middleValue]:
                lastHigh = middleValue - 1
            else:
                firstLow = middleValue + 1

    return answer

print(Binary_Search([100,101,102,103,104,105,106,107,108,109,110,111],111,112))
