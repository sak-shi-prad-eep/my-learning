def findSum(n):
    s=0
    for i in range(n+1):
        s+=2**i
    print(s)
s=int(input())
findSum(s)
    