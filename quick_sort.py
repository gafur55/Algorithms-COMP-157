def quick_sort(arr, low, high):
    if(low < high):
        s = partition(arr, low, high)
        quick_sort(arr, low, s - 1)
        quick_sort(arr, s+1, high)

def partition(arr, l, h):
    pivot = arr[l]
    i = l + 1
    j = h
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            (arr[i], arr[j]) = (arr[j], arr[i])
        else:
            break
    
    (arr[l], arr[j]) = (arr[j], arr[l])
    return j
data = ['e', 'x', 'a', 'm', 'p', 'l', 'e']
print("Unsorted Array")
print(data)

size = len(data)

quick_sort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)


