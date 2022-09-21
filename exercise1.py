from array import array
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

test = euclid(60, 24)
# print(test)

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

test = int_check(60, 24)
# print(test)

time.sleep (1)
end = time.time()
print("algorithm time:", end - begin)


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

    return arr2

# print(prime_factorization(121))


def mid_school_gcd(m, n):
    arr1 = prime_factorization(m)
    arr2 = prime_factorization(n)

    arr1.remove(1)
    arr2.remove(1)

    arr3 = []
    arr4 = []

    for x in arr1:
        if(m % x == 0):
            arr3.append(x)

    for y in arr2:
        if(n % y == 0):
            arr4.append(y)

    factor1 = []
    factor2 = []
    
    for x in arr3:
        while(m % x == 0):
            factor1.append(x)
            m /= x

    for x in arr4:
        while(n % x == 0):
            factor2.append(x)
            n /= x



    mult = 1

    for x in factor1:
        for y in factor2:
            if (x == y):
                mult *= x
                factor2.remove(y)
                continue
        factor1.remove(x)
    
    return mult

begin = time.time()

# print(mid_school_gcd(60, 24))
time.sleep (1)
end = time.time()

print("algorithm time:", end - begin)
