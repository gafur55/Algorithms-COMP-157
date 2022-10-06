from operator import truediv


def reverse_str(string):
    if string == "":
        return ""
    else:
        return reverse_str(string[1:]) + string[:1]

# arr = "rufag sevol anaili"
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
# print(dec_binary(25, x))

def sum_till(num):
    if num == 0:
        return 0
    else:
        return num + sum_till(num-1)

# print(sum_till(3))


def power_sert(arr, size):
    if size == -1:
        return [""]
    else:
        for i in range (size):
            arr2.append(arr)
            return 