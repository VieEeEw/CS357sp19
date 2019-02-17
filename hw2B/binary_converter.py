def binary(x, n):
    int_str = bin(int(x))
    deci = x - int(x)
    deci_str = ""
    while deci != 0 and n > 0:
        n -= 1
        if int(deci*2) >= 1:
            deci_str += "1"
        else:
            deci_str += "0"
        deci = deci*2 - int(deci*2)
    print(int_str + "." + deci_str)

binary(100000.1,53)
binary(100000.2,53)
binary(100000.2 - 100000.1 ,53)
binary(0.1,53)
binary(0.2,53)
