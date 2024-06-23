s=input()
list1=[]
list1=list(s)
for i in range(len(list1)):
    if i%2==0:
        print(list1[i],end='')