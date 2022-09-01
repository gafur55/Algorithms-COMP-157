import time

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

begin = time.time()

test = euclid(56212, 789744)
print(test)

time.sleep (1)
end = time.time()

print("algorithm time:", end - begin)

def int_check(a, b):
    t = a
    while(t != 1):
        if(b < t):
            t = b
        if(a % t == 0):
            if(b % t == 0):
                return t
            else:
                t -= 1
        else:
            t -= 1


begin = time.time()

test = int_check(56212, 789744)
print(test)

time.sleep (1)
end = time.time()
print("algorithm time:", end - begin)
