##optimised-cut in half because if d is a divisor of n, then n/d is also a divisor of n
##we go uptill the square root cause sqr*sqr will give the number

import math
num=int(input("enter a number: "))
sq=int(math.sqrt(num))
divisors=[]
for i in range(1,sq+1):
    if num%i==0:
        divisors.append(i)
        if i!=num//i:
            divisors.append(num//i)
divisors.sort()
print(divisors)




# num=int(input("enter a number: "))
# for i in range(1,num):
#     if num%i==0:
#         print(i)