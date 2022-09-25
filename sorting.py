import random
from selectors import SelectSelector
import time

def swap(arr, x, index_x, y, index_y):
    temp = x
    arr[index_x] = y
    arr[index_y] = temp 
    

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                swap(arr, arr[j], j, arr[j+1], j+1)
                # print(arr)

# problematic!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#problem is with the equal numbers in one array. For example, arr = [55, 22, 34, 6, 21, 5, 1] will return [1, 5, 6, 34, 22, 22, 55]
#the sudo code never handles this condition
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if(arr[i] != arr[min]):
            swap(arr, arr[i], i, arr[min], min)



def main():
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
        print("timing for selection sort with ", len(arr), " sized array ---->", (end - start) * 10**3, "ms")
        # print("after sorting \n", arr)

    nums = [10, 100, 1000]
    for i in nums:
        arr = [0] * i   
        for j in range(i):
            x = random.randrange(0, 100)
            arr[j] = x
        # print("before sorting \n", arr)
        start = time.time()
        bubble_sort(arr)
        end = time.time()
        print("timing for bubble sort with ", len(arr), " sized array ---->", (end - start) * 10**3, "ms")
        # selection_sort(arr)
        # print("after sorting \n", arr)

if __name__ == "__main__":
    main()