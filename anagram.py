from asyncio.windows_events import NULL
from contextlib import nullcontext


def anagram(w1, w2):
    if(len(w1) != len(w2)):
        return False
    else:
        check = True
        arr1 = [] * len(w1)
        arr2 = [] * len(w2)
        for i in range(len(w1)):
            arr1.append(w1[i])
            arr2.append(w2[i])

        for i in range(len(arr1)):
            for j in range(len(arr2)):
                if(arr1[i] == arr2[j]):
                    arr2[j] = NULL
                    # break

        for i in range(len(arr2)):
            if (arr2[i] != NULL):
                check = False
    return check


print(anagram("teaate", "eat"))
        