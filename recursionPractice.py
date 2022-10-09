def reverse_str(string):
    if string == "":
        return ""
    else:
        return reverse_str(string[1:]) + string[:1]

# arr = "kayak"
# newarr = reverse_str(arr)
# print(newarr)


def palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    else:
        if string[:1] == string[len(string)-1:]:
            return palindrome(string[1:len(string)-1])
    return False


# print(palindrome("abba"))

def dec_binary(num, result):
    if num == 0:
        return result
    else:
        result += str(num % 2)
        dec_binary(num//2, result) 
        
# x = ''
# print(dec_binary(25, x)

def sum_till(num):
    if num == 0:
        return 0
    else:
        return num + sum_till(num-1)

# print(sum_till(3))


def power_set(arr):         
    if len(arr) == 1:
        return ["", arr[0]]
    else:
        # arr.pop(len(arr) - 1)
        smaller_arr = power_set(arr[:-1])
        bigger_arr = []
        # bigger_arr = smaller_arr
        for i in smaller_arr:
            bigger_arr.append(i)
        for i in smaller_arr:
            x = i + ' ' + arr[len(arr) - 1]
            bigger_arr.append(x)
        
        return bigger_arr

print(power_set(['1', '2', '3']))

# def binary_search(arr, num, index):
#     if arr[index] == num: