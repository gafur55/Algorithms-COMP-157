def mergeSort(arr):
    if len(arr) > 1:
        arrB = []
        arrC = []
        for i in range(0, (len(arr) // 2)):
            arrB.append(arr[i])
        for j in range((len(arr) // 2), len(arr)):
            arrC.append(arr[j])
        mergeSort(arrB)
        mergeSort(arrC)

        merge(arrB, arrC, arr)

def merge(arrB, arrC, arr):
    i = 0
    j = 0
    k = 0
    while i < len(arrB) and j < len(arrC):
        if arrB[i] <= arrC[j]:
            arr[k] = arrB[i]
            i += 1
        else:
            arr[k] = arrC[j]
            j += 1
        k += 1
    while i < len(arrB):
        arr[k] = arrB[i]
        i += 1
        k +=1
    while j < len(arrC):
        arr[k] = arrC[j]
        j += 1
        k += 1
    print(arr)


x = ['e', 'x', 'a', 'm', 'p', 'l', 'e']
mergeSort(x)
print(x)

