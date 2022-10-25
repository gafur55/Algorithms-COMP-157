def bit_string(num, arr):
    if num == 1:
        arr.append('0')
        arr.append('1')
        return arr
    else:
        bit_string(num - 1, arr)
        arr1 = []
        for i in arr:
            arr1.append(i)
        del arr[:]
        for i in arr1:
            arr.append(i+'0')
            arr.append(i+'1')
    return arr

arr = []
print(bit_string(5, arr))














