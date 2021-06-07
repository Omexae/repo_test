import estPremier


def chance(arg1):
    res = True
    for num in range(1, arg1):
        if not estPremier.premier(arg1 + num + (num * num)):
            res = False
    return res
