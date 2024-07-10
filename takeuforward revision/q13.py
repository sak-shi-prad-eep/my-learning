num=int(input("enter a number: "))
for i in range(num,0,-1):
    for j in range(num-i):
        print(" ",end='')
    for k in range(1,2*i):
        print("*",end='')
    print()
