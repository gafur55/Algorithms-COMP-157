import random

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

# problematic!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        swap(arr, arr[i], arr[min])
        # print(arr)



def main():
    for i in [10, 100, 1000, 10000, 100000, 1000000]:
        arr = []
        for j in range(i):
            x = random.randrange(0, 100)
            arr.append(x)
        print("before sorting \n", arr)
        # bubble_sort(arr)
        selection_sort(arr)
        print("after sorting \n", arr)
        # selection_sort(x)
        # print(x)

if __name__ == "__main__":
    main()