def LargestSequence(sequence):
    finalList = []
    tempList = []
    num = 0
    
    for i in range(len(sequence)-1):
        if i == 0:
            tempList.append(sequence[i])
        else:
            if sequence[i] >= sequence[i-1]:
                tempList.append(sequence[i])
            if sequence[i] < sequence[i-1]:
                finalList.append(tempList)
                tempList = []
                tempList.append(sequence[i])
    finalList.append(tempList)

    print(finalList)
    
    for i in range(len(finalList)):
        if i == 0:
            num = len(finalList[i])
            sequence = finalList[i]
        else:
            if len(finalList[i]) > num:
                num = len(finalList[i])
                sequence = finalList[i]
    return("This is the largest sequence " + str(sequence) + str(num))
    

sequence = [1,2,3,4,1,5,1,6,7]
print(LargestSequence(sequence))
