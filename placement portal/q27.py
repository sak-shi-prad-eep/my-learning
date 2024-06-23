name1=input()
name2=input()
count=0
countq=0
if len(name1)==len(name2):
    for i in range(len(name1)):
        if(name1[i])!="?" and name2[i]!="?" and name1[i]!=name2[i]:
            count+=1
            
        if(name1[i]=='?' or name2[i]=='?'):
            countq+=1
countq+=count
print(count,countq)