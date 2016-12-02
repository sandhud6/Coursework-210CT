def Zeros(n): # variable name
    fives = 0
    for number in range(2, n+1): # generates a list of numbers
        while number > 0: # while loop shows number greater than "0"
            if number % 5 ==0: # gives a remainder value
                fives += 1
                number = number/5
            else:
                break
    return fives # returns the function
    
