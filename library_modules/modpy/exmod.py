def count(intx):
    x=float(intx)
    z=0
    y=1
    i=1
    if x>5:
        print("WARNING: overload risk")
        print("Do you want to continue? (y/n)")
        if input() == "n":
            quit()
    if x > float(5.814316417866508):

        print("""Traceback (most recent call last):
          File "mod.py", line 3, in <module>
            if input() > 5.814316417866508:
                       ^ ^^^^^^^^^^^^^^^^^
        OutputError: exited 5.814316417866508""")
        quit(1)
    while z<x:
        y=y+2
        i=i+1
        print(z)
        z=(1/y)+z
    print(f"""{i} itterations passed
    """)
# count(input("number, please"))
