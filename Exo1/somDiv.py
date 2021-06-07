def div(arg1):
    div1 = 0
    for num in range(1, arg1):
        if arg1 % num == 0:
            div1 += num
    return div1

