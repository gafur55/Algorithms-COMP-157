from cProfile import label
import random
from selectors import SelectSelector
import time
import matplotlib.pyplot as plt

def swap(arr, x, index_x, y, index_y):
    temp = x
    arr[index_x] = y
    arr[index_y] = temp 
    

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                swap(arr, arr[j], j, arr[j+1], j+1)

def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if(arr[i] != arr[min]):
            swap(arr, arr[i], i, arr[min], min)



def main():
    b_sort = []
    s_sort = []
    nums = [10, 100, 1000]
    for i in nums:
        arr = [0] * i   
        for j in range(i):
            x = random.randrange(0, 100)
            arr[j] = x
        # print("before sorting \n", arr)
        # bubble_sort(arr)
        start = time.time()
        selection_sort(arr)
        end = time.time()
        b_sort.append((end-start) * 10**3)
        print("timing for selection sort with ", len(arr), " sized array ---->", (end - start) * 10**3, "ms")
        # print("after sorting \n", arr)

    nums = [10, 100, 1000]
    for i in nums:
        arr = [0] * i   
        for j in range(i):
            x = random.randrange(0, 100)
            arr[j] = x
        start = time.time()
        bubble_sort(arr)
        end = time.time()
        s_sort.append((end-start) * 10**3)
        print("timing for bubble sort with ", len(arr), " sized array ---->", (end - start) * 10**3, "ms")

    plt.plot(nums, b_sort, label = 'bubbleSort')
    plt.plot(nums, s_sort, label = 'sortingLabel')
    plt.xlabel('array size')
    plt.ylabel('timing')
    plt.legend()
    plt.show()





if __name__ == "__main__":
    main()