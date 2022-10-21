def fakeCoin(a):
    if (len(a) < 3):
        fake = min(a)
        return fake
    else:
        b = []
        c =[]
        d = []
        e = []
        num = len(a) // 3 #integer division
        for i in range(num):
            b.append(a[i])
        for i in range(num, 2*num):
            c.append(a[i])
        for i in range(2*num, 3*num):
            d.append(a[i])
        for i in range(3*num, len(a)):
            e.append(a[i])
        if(sum(b) == sum(c) == sum(d)):
            return(min(e)); #return the minimum value from the ArrayE
        else:
            min_Sum = min(b, c, d) #Min_Sum = array with the smallest sum of element from B,C,D
            return fakeCoin(min_Sum)
x = fakeCoin([1, 2, 2, 2, 2,2, 2, 2, 2, 2])
print(x)