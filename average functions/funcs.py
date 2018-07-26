def mean(*args):
    result = sum(args) / len(args)
    if not result == int(result):
        result = round(result, int(input("How many significant digits would you like? ")))
    return result

def median(*args):
    vars = list(args)

    if (len(vars)) % 2  == 0:
        return list((vars[len(vars) // 2 - 1], vars[(len(vars) // 2)]))
    else:
        return [vars[(len(vars) // 2)]]

def mode(*args):
    count = {}
    for value in args:
        count[value] = count.get(value, 0) + 1
    max = sorted(count.items(), key=lambda x: x[1], reverse=True)[0][1]
    results = [key for key, value in count.items() if value == max]
    return results

