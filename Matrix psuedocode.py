Matrix Psuedocode

    MatrixAdding[M1,M2]
      FreshMatrix <-- [[0,0],[0,0]]
      For i in RANGE[LENGTH[M1]]
       For j in RANGE(LENGTH(M2))
           FreshMatrix <-- M1 + M2
      Return FreshMatrix

      MatrixSubtracting[M1,M2]
        FreshMatrix <-- [[0,0],[0,0]]
        For i in RANGE[LENGTH[M1]]
         For j in RANGE(LENGTH(M2))
             FreshMatrix <-- M1 - M2
        Return FreshMatrix

        MatrixMultiplying[M1,M2]
          FreshMatrix <-- [[0,0],[0,0]]
          For i in RANGE[LENGTH[M1]]
            For j in RANGE(LENGTH(M2))
                FreshMatrix <-- M1 * M2
          Return FreshMatrix
