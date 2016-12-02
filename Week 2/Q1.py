import math

def Perfect_Square(p):
    interg=0
    while interg*interg < p:
        interg = interg+1
    if interg * interg != p:
        return "false"
    else:
        return p
