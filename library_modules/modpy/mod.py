import math
def avg(a, b):
    return((a + b) / 2)
def calc(a, b, c):
    if b == "+":
        return(a + c)
    if b == "-":
        return(a - c)
    if b == "/":
        return(a / c)
    if b == "mod":
        return(a % c)
    if b == "^":
        return(a ** c)