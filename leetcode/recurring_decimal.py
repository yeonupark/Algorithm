def solve(numerator, denominator):

    ans = ""

    ans += str(abs(numerator)//abs(denominator))
    if numerator * denominator < 0:
        ans = "-" + ans
    
    numerator = abs(numerator)
    denominator = abs(denominator)
    remainder = numerator % denominator

    if remainder == 0:
        return ans
        
    store = {remainder: 0}

    tmp = ""
    idx = 1
    while (remainder > 0):
        tmp += str(remainder*10 // denominator)
        remainder = remainder*10 % denominator

        if remainder in store:
            i = store[remainder]
            tmp = tmp[:i] + "(" + tmp[i:] + ")"
            break

        store[remainder] = idx
        idx += 1

    return ans + "." + tmp