from array import array
# import time

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

# begin = time.time()

# test = euclid(56212, 789744)
# print(test)

# time.sleep (1)
# end = time.time()

# print("algorithm time:", end - begin)

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


# begin = time.time()

# test = int_check(0,0)
# print(test)

# time.sleep (1)
# end = time.time()
# print("algorithm time:", end - begin)


def prime_factorization(a):
    arr = [True] * (a + 1)
    for i in range(2, a + 1):
        if(arr[i] == True):
            t = 2
            
            while(t < len(arr)):
                z = i
                z = t * z
                if(z >= len(arr)):
                    break
                else:
                    arr[z] = False
                t += 1



    arr2 = []
    for x in range(1, len(arr)):
        if(arr[x] == True):
            arr2.append(x)

    print(arr2)

prime_factorization(121)
