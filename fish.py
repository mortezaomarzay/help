# x is the input value
# this code runs the input value through a series of if statements to determine what to print


def pondfish(fish):

    if type(fish) == type(1):
        value_error = ValueError(f"input should be 1, 2, 0, r or b")
        raise value_error
    if type(fish) == type(1.0):
        value_error = ValueError(f"input should be 1, 2, 0, r or b")
        raise value_error
    if fish == '':
        value_error = ValueError(f"input should be 1, 2, 0, r or b")
        raise value_error


    fish = str(fish.split())
    for y in fish:
        if "1" in y:
            print("One fish!", end =" ")
        if "2" in y:
            print("Two fish!", end =" ")
        if "r" in y:
            print("Red fish!", end =" ")
        if "b" in y:
            print("Blue fish!", end =" ")
        if "0" in y:
            print("No fish!", end =" ")




#pondfish("2")   # PASS
#pondfish('r 3')     # FAIL
#pondfish('3')       # FAIL
#pondfish('p')       # FAIL
#pondfish('   ')     # FAIL
#pondfish('')        # FAIL
#pondfish(0)         # FAIL
#pondfish(3.0)       # FAIL
