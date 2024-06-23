def findType(n):
    s=0
    for i in range(1,n+1):
        if (n%i)==0:
            s+=1
    if s==4:
        print("Nice")
    else:
        print("Not Nice")
        
n=int(input())
findType(n)