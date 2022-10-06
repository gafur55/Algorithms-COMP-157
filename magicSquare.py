# from datetime import datetime

# def magic_square(n):
#     start_time=datetime.now() #for finding efficiency of the code

#     magicSquare=[]
#     for i in range(n):
#         l=[]
#         for j in range(n):
#             l.append(0)
#         magicSquare.append(l)
#         i=n//2
#         j=n-1
#     num=n*n
#     count=1
#     while(count<=num):
#         if i==-1 and j==n:
#             j=n-2
#             i=0
#         else:
#             if j==n:
#                 j=0
#             if i<0:
#                 i=n-1
#         if magicSquare[int(i)][int(j)]!=0:
#             j = j - 2
#             i += 1
#             continue
#         else:
#             magicSquare[int(i)][int(j)]=count
#             count+=1
#         i-=1
#         j+=1
#     for i in range(n):
#         for j in range(n):
#             print(magicSquare[i][j],end=" ")
#         print()
#     print("the sum of each row/column/diagonl is:"+str(int(n*(n**2+1)/2)))

#     end_time=datetime.now() #for finding efficiency of the code
#     time_taken=abs(start_time-end_time)
#     print(time_taken.total_seconds())

# n=int(input("enter number to genarate magic Square:"))
# magic_square(n)


# def swap(arr, i, j):
#     temp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = temp

# def perm(arr, curr):
#     if(curr == len(arr) - 1):
#         print(arr)
#         return arr
#     else:
#         for i in range(curr, len(arr)):   
#             swap(arr, i, curr)
#             perm(arr, curr + 1)
#             swap(arr, i, curr)
            
# def arrChanger(arr, n):
#     arr1 = [[0]*n]*n
#     # print(arr1)
#     for i in range(n):
#         for j in range(n):
#             if(arr1[i][j] == 0):
#                 arr1[i][j] = arr[i*j]
#     return arr1
            
                



#function call
# arr1 = []
# arr1 = perm([1,2,3], 0)
# print("stored arr")
# print(arr1)
# arr = [1,2,3,4,5,6,7,8,9]
# x = arrChanger(arr, 3)
# print(x)


# Python program to generate magic square
import numpy as np
import sys
import time

order = int(input("Enter order of magic square (order must be odd): "))

# if even number is given then it will be incremented by one
if order%2==0:
    order = order+1
    print("Given order is even so it is incremented by 1.")

start = time.time()

mid = order//2

magic = np.zeros((order,order))

k = mid
j = 0



for i in range(1,order*order+1):
    magic[j][k] = i
    p = j
    j = j-1
    q = k
    k = k+1
    
    if j<0:
        j = order-1
    
    if k>order-1:
        k = 0
    
    if magic[j][k]!=0:
        k = q
        j = p+1
end = time.time()

print(end - start)


print("Generated Magic Square is: \n")

for j in range(order):
    print("|", end="")
    
    for k in range(order):
        print("%4d |" % magic[j][k], end="")
    
    print()
    
    for i in range(1, 6*order+1):
        print("-", end="")
    
    print()
    