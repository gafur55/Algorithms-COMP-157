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
#problem is with the equal numbers in one array. For example, arr = [55, 22, 34, 6, 21, 5, 1] will return [1, 5, 6, 34, 22, 22, 55]
#the sudo code never handles this condition
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        swap(arr, arr[i], arr[min])
        # print(arr)



def main():
    nums = [10, 10, 10, 10]
    for i in nums:
        arr = [0] * i   
        for j in range(i):
            x = random.randrange(0, 100)
            arr[j] = x
        print("before sorting \n", arr)
        # bubble_sort(arr)
        selection_sort(arr)
        print("after sorting \n", arr)
        # selection_sort(x)
        # print(x)

if __name__ == "__main__":
    main()