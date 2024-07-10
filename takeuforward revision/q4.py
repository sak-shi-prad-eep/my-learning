##euclidean
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
while num1>0 and num2>0:
    if num1>num2:
        num1=num1%num2
    else:
        num2=num2%num1
if num1==0:
    print(num2)
else:
    print(num1)

# num1=int(input("enter a number: "))
# num2=int(input("enter a number: "))
# list1=[]
# max_num=max(num1,num2)
# for i in range(1,max_num):
#     if num1%i==0 and num2%i==0:
#         list1.append(i)
# print(max(list1))

##optimised
# num1=int(input("enter a number: "))
# num2=int(input("enter a number: "))
# list1=[]
# min_num=min(num1,num2)
# for i in range(min_num,0,-1):
#     if num1%i==0 and num2%i==0:
#         list1.append(i)
# print(max(list1))

