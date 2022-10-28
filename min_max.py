def partition(arr, left, right, min_val, max_val):
    if left == right:
        min_val = arr[left]
        max_val = arr[left]
        return min_val, max_val
    elif left == right + 1:
        if arr[left] <= arr[right]:
            if min_val > arr[left]:
                min_val = arr[left]
            if max_val < arr[right]:
                max_val = arr[right]
        else:
            if min_val > arr[right]:
                min_val = arr[right]
            if max_val < arr[left]:
                max_val = arr[left]
        return min_val, max_val
    else:
        min_val, max_val = partition(arr, left, right//2, min_val, max_val)
        min_val, max_val = partition(arr, right//2 + 1, right, min_val, max_val)

nums = [7, 2, 9, 3, 1, 6, 7, 8, 4] 
min = 0
max = 0
(min, max) = partition(nums, 0, len(nums) - 1, min, max)

print("The minimum element in the list is", min)
print("The maximum element in the list is", max)