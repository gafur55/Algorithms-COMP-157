# the given program should find the prefix from given list of words
def prefix(arr):
    word = min(arr, key = len)
    print(word)
    pref = ''
    boolean = False
    for i in range(len(word)):
        for j in arr:
            if j[i] == pref:
                boolean = True
            else:
                boolean = False
        if boolean == True:
            pref += j[i]
        
    # print(pref)

    


def main():
    arr = ['gafur', "gafi", "gafar" ]
    prefix(arr)

if __name__ == "__main__":
    main()