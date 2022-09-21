from numpy import random

def swap(arr, x, y):
    # print(arr[arr.index(x)], arr[arr.index(y)])
    index_x = arr.index(x)
    index_y = arr.index(y)
    temp = arr[index_x]
    arr[index_x] = y
    arr[index_y] = temp 
    # print(arr[index_x], arr[index_y])
    

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                swap(arr, arr[j], arr[j+1])
                # print(arr)

def selection_sort(arr):
    print(arr)
    for i in range(len(arr)):
        min = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
        swap(arr, arr[i], min)
        # print(arr)



def main():
    for i in [10, 100, 1000, 10000, 100000, 1000000]:
        x=random.randint(1000, size=(i))
        bubble_sort(x)
        selection_sort(x)

if __name__ == "__main__":
    main()