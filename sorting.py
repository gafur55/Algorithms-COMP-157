import random
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


def insertion(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            swap(arr, arr[j], j, arr[j + 1], j+1)
            current = arr[j]
            j -= 1



def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        j = gap
        while j < len(arr):
            i = j - gap
            while i >= 0:
                if arr[i + gap] < arr[i]:
                    arr[i+gap], arr[i] = arr[i], arr[i+gap]
                else:
                    break
                i = i -gap
            j += 1
        gap = gap // 2

def reverse(arr):
    for i in range(0, len(arr)//2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]

# x = [1,2,3,4,5, 6]
# reverse(x)
# print(x)


def main():
    b_sort = []
    s_sort = []
    insertion_sort_arr = []
    shell_sort_arr = []
    decreasing_order_data = []
    increasing_order_data = []
    increasing_order = []
    decreasing_order = []

    #generating arrays in increasing order
    for i in [10, 100, 1000, 10000, 100000, 1000000]:
        arr = [0] * i
        for j in range(i):
            x = random.randrange(0, 100)
            arr[j] = x
        arr.sort()
        increasing_order.append(arr)
    # print(increasing_order)

    #generating arrays in decreasing order
    for i in increasing_order:
        reverse(i)
        decreasing_order.append(i)
    # print(decreasing_order)

    
    
    for i in increasing_order:
        start = time.time()
        shell_sort(i)
        end = time.time()
        increasing_order_data.append((end - start) * 10**3)
        print("timing for shell sort with ", len(i), " sized (increasing ordered) array ---->", (end - start) * 10**3, "ms")
    print()
    for i in increasing_order:
        start = time.time()
        insertion(i)
        end = time.time()
        increasing_order_data.append((end - start) * 10**3)
        print("timing for insertion sort with ", len(i), " sized (increasing ordered) array ---->", (end - start) * 10**3, "ms")
    print()
    for i in increasing_order:
        start = time.time()
        bubble_sort(i)
        end = time.time()
        increasing_order_data.append((end - start) * 10**3)
        print("timing for bubble sort with ", len(i), " sized (increasing ordered) array ---->", (end - start) * 10**3, "ms")
    print()
    for i in increasing_order:
        start = time.time()
        selection_sort(i)
        end = time.time()
        increasing_order_data.append((end - start) * 10**3)
        print("timing for selection sort with ", len(i), " sized (increasing ordered) array ---->", (end - start) * 10**3, "ms")
    print()

    for i in decreasing_order:
        start = time.time()
        shell_sort(i)
        end = time.time()
        decreasing_order_data.append((end - start) * 10**3)
        print("timing for shell sort with ", len(i), " sized (decreasing ordered) array ---->", (end - start) * 10**3, "ms")
    print()
    for i in decreasing_order:
        start = time.time()
        insertion(i)
        end = time.time()
        decreasing_order_data.append((end - start) * 10**3)
        print("timing for insertion sort with ", len(i), " sized (decreasing ordered) array ---->", (end - start) * 10**3, "ms")
    print()
    for i in decreasing_order:
        start = time.time()
        bubble_sort(i)
        end = time.time()
        decreasing_order_data.append((end - start) * 10**3)
        print("timing for bubble sort with ", len(i), " sized (decreasing ordered) array ---->", (end - start) * 10**3, "ms")
    print()
    for i in decreasing_order:
        start = time.time()
        selection_sort(i)
        end = time.time()
        decreasing_order_data.append((end - start) * 10**3)
        print("timing for selection sort with ", len(i), " sized (decreasing ordered) array ---->", (end - start) * 10**3, "ms")
    print()
    
    nums = [10, 100, 1000, 10000, 100000, 1000000]
    for i in nums:
        arr = [0] * i   
        for j in range(i):
            x = random.randrange(0, 100)
            arr[j] = x
        start = time.time()
        selection_sort(arr)
        end = time.time()
        s_sort.append((end-start) * 10**3)
        print("timing for selection sort with ", len(arr), " sized array ---->", (end - start) * 10**3, "ms")
    print()
    nums = [10, 100, 1000, 10000, 100000, 1000000]
    for i in nums:
        arr = [0] * i   
        for j in range(i):
            x = random.randrange(0, 100)
            arr[j] = x
        start = time.time()
        bubble_sort(arr)
        end = time.time()
        b_sort.append((end-start) * 10**3)
        print("timing for bubble sort with ", len(arr), " sized array ---->", (end - start) * 10**3, "ms")
    print()
    nums = [10, 100, 1000, 10000, 100000, 1000000]
    for i in nums:
        arr = [0] * i   
        for j in range(i):
            x = random.randrange(0, 100)
            arr[j] = x
        start = time.time()
        insertion(arr)
        end = time.time()
        insertion_sort_arr.append((end-start) * 10**3)
        print("timing for insertion sort with ", len(arr), " sized array ---->", (end - start) * 10**3, "ms")
    print()
    nums = [10, 100, 1000, 10000, 100000, 1000000]
    for i in nums:
        arr = [0] * i   
        for j in range(i):
            x = random.randrange(0, 100)
            arr[j] = x
        start = time.time()
        shell_sort(arr)
        end = time.time()
        shell_sort_arr.append((end-start) * 10**3)
        print("timing for shell sort with ", len(arr), " sized array ---->", (end - start) * 10**3, "ms")
    print()
    plt.plot(nums, b_sort, label = 'bubbleSort')
    plt.plot(nums, s_sort, label = 'selectionSort')
    plt.plot(nums, insertion_sort_arr, label = 'insertionSort')
    plt.plot(nums, shell_sort_arr, label = 'shellSort')

    plt.xlabel('array size')
    plt.ylabel('timing')
    plt.legend()
    plt.show()





if __name__ == "__main__":
    main()