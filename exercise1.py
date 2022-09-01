def euclid(x, y):
    if(x == 0):
        return y
    elif(y == 0):
        return x
    else:
        while(x != 0 and y != 0):
            if(x < y):
                m = x
                x = y
                y = m
            if(x == y):
                return x
            mod = x % y
            x = y
            y = mod
        return x

test = euclid(23, 0)
print(test)

