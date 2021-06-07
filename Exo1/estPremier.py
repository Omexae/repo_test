def premier(arg1):
    res = True
    for num in range(2, arg1):
        if arg1 % num == 0:
            res = False
    return res
