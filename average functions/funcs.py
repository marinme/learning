def mean(*args):
    result = sum(args) / len(args)
    if not result == int(result):
        result = round(result, int(input("How many significant digits would you like? ")))
    return result

def median():
    pass

def mode():
    pass
