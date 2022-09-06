num = int(input("enter a positive integer: "))

for i in range(num):
    if(i*i == num):
        print(i)
    elif(i*i < num and (i+1)*(i+1) > num):
        print(i)