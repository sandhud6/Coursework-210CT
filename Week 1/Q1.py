import random # random numbers is imported

def randomlist(List):
    answer= [] # variable name

    while len(List) > 0: # while loop shows the list is greater than "0"
        num = random.randrange(len(List)) # reorder the list
        answer.append(List.pop(num)) # takes element and puts it in a new list

    return answer # returns a new list


