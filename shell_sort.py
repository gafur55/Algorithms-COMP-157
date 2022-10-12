import random
import time
import matplotlib.pyplot as plt

def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        j = gap
        while j < len(arr):
            i = j - gap
            while i >= 0:
                if arr[i + gap] < arr[i]:
                    arr[i+gap], arr[i] = arr[i], arr[i+gap]
                    print(arr)
                else:
                    break
                i = i -gap
            j += 1
        gap = gap // 2
        
arr =['s','h','e','l','l','s','o','r','t','i','s','u','s','e','f','u','l']
shell_sort(arr)
print(arr)

'''
a) the implementation of shell_sort in ['s','h','e','l','l','s','o','r','t','i','s','u','s','e','f','u','l']:

['s', 'h', 'e', 'l', 'l', 'e', 'o', 'r', 't', 'i', 's', 'u', 's', 's', 'f', 'u', 'l']
['s', 'h', 'e', 'l', 'l', 'e', 'f', 'r', 't', 'i', 's', 'u', 's', 's', 'o', 'u', 'l']
['s', 'h', 'e', 'l', 'l', 'e', 'f', 'r', 'l', 'i', 's', 'u', 's', 's', 'o', 'u', 't']
['l', 'h', 'e', 'l', 'l', 'e', 'f', 'r', 's', 'i', 's', 'u', 's', 's', 'o', 'u', 't']
['l', 'e', 'e', 'l', 'l', 'h', 'f', 'r', 's', 'i', 's', 'u', 's', 's', 'o', 'u', 't']
['l', 'e', 'e', 'l', 'l', 'h', 'f', 'r', 's', 'i', 'o', 'u', 's', 's', 's', 'u', 't']
['e', 'e', 'l', 'l', 'l', 'h', 'f', 'r', 's', 'i', 'o', 'u', 's', 's', 's', 'u', 't']
['e', 'e', 'l', 'h', 'l', 'l', 'f', 'r', 's', 'i', 'o', 'u', 's', 's', 's', 'u', 't']
['e', 'e', 'l', 'h', 'f', 'l', 'l', 'r', 's', 'i', 'o', 'u', 's', 's', 's', 'u', 't']
['e', 'e', 'f', 'h', 'l', 'l', 'l', 'r', 's', 'i', 'o', 'u', 's', 's', 's', 'u', 't']
['e', 'e', 'f', 'h', 'l', 'l', 'l', 'i', 's', 'r', 'o', 'u', 's', 's', 's', 'u', 't']
['e', 'e', 'f', 'h', 'l', 'i', 'l', 'l', 's', 'r', 'o', 'u', 's', 's', 's', 'u', 't']
['e', 'e', 'f', 'h', 'l', 'i', 'l', 'l', 'o', 'r', 's', 'u', 's', 's', 's', 'u', 't']
['e', 'e', 'f', 'h', 'l', 'i', 'l', 'l', 'o', 'r', 's', 's', 's', 'u', 's', 'u', 't']
['e', 'e', 'f', 'h', 'i', 'l', 'l', 'l', 'o', 'r', 's', 's', 's', 'u', 's', 'u', 't']
['e', 'e', 'f', 'h', 'i', 'l', 'l', 'l', 'o', 'r', 's', 's', 's', 's', 'u', 'u', 't']
['e', 'e', 'f', 'h', 'i', 'l', 'l', 'l', 'o', 'r', 's', 's', 's', 's', 'u', 't', 'u']
['e', 'e', 'f', 'h', 'i', 'l', 'l', 'l', 'o', 'r', 's', 's', 's', 's', 't', 'u', 'u']
['e', 'e', 'f', 'h', 'i', 'l', 'l', 'l', 'o', 'r', 's', 's', 's', 's', 't', 'u', 'u']

b) shell sort is a stable algorithm

'''
