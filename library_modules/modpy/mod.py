import math
def avg(a, b):
    outa = ((a + b) / 2)
    return(str(outa))
def calc(a, b, c):
    if b == "+":
        outa = a + c
    if b == "-":
        outa = a - c
    if b == "/":
        outa = a / c
    if b == "mod":
        outa = a % c
    if b == "^":
        outa = a ** c
    return(str(outa))
