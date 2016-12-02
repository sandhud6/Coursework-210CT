class matrix:

    def matrixAddition(M1,M2):
        newMatrix = [[0,0],[0,0]]
        for i in range(len(M1)):
            for j in range(len(M2)):
                newMatrix = [i][j] = M1[i][j] + M2[i][j]
        return newMatrix

    def matrixSubtraction(M1,M2):
        newMatrix = [[0,0],[0,0]]
        for i in range(len(M1)):
            for j in range(len(M2)):
                newMatrix = [i][j] = M1[i][j] - M2[i][j]
        return newMatrix

    def matrixMultiplication(M1,M2):
        newMatrix = [[0,0],[0,0]]
        for i in range(len(M1)):
            for j in range(len(M2)):
                newMatrix = [i][j] = M1[i][j] * M2[i][j]
        return newMatrix
    

    

    
