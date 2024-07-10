##optimised
import math
num=int(input("enter a number: "))
sq=int(math.sqrt(num))
count=0
for i in range(1,sq+1):
    if num%i==0:
        count+=1
        if i!=num//i:
            count+=1
if count>2:
    print("composite")
else:
    print("prime")

# num=int(input("enter a number: "))
# def prime_check(num):
#     if num==0 or num==1:
#         return "composite"
#     elif num==2:
#         return "prime"
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 return "not prime"
#         else:
#             return "prime"
# print(prime_check(num))