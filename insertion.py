def swap(arr, x, index_x, y, index_y):
    temp = x
    arr[index_x] = y
    arr[index_y] = temp 


def insertion(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            swap(arr, arr[j], j, arr[j + 1], j+1)
            current = arr[j]
            j -= 1


x = [12, 33, 20, -1, 45, 20, 5, 45]
insertion(x) 
print(x)