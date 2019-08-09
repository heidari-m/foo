def answer(n, b):
    z_str = n
    k = len(n)
    dic = dict()
    i = 0
    while 1:
        x = ''.join(sorted(z_str, reverse=True))
        y = ''.join(sorted(z_str))
        x_dec = int(x, b)  # convert to integers in base 10
        y_dec = int(y, b)
        z = x_dec - y_dec
        if z < b: return 1
        if z in dic:
            return len(dic) - dic[z]
        else:
            dic[z] = i
            z_str = n2b(z,b) # convert back to base b, still in integer
        if len(z_str) < k:
            z_str = '0' + z_str
        i += 1

def n2b(n, b):      # convert number n from base 10 to base b
    if n == 0:
        return 0
    d = []
    while n:
        d.append(int(n % b))
        n /= b
    return ''.join(map(str,d[::-1]))
