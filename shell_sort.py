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
                
arr =['s','h','e','l','l','s','o','r','t','i','s','u','s','e','f','u','l']
shell_sort(arr)
print(arr)