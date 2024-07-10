num1=int(input("enter a number: "))
sum1=0
list1=list(map(int,str(num1)))
length=len(list1)
for i in list1:
    i=pow(i,length)
    sum1+=i
if sum1==num1:
    print("armstrong number")
else:
    print("nope")
