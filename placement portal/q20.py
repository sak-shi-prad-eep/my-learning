def sumOfDigits(num):
    list1=[]
    list1=list(num)
    sum1=0
    for i in list1:
        sum1+=int(i)
    print(sum1)
    
n=input()
sumOfDigits(n)