n=input()
length=len(n)
w=0
c=0
for i in range(length):
    if n[i]=='1':
        w+=1
    else:
        c+=1
if w>c:
    print("Win")
else:
    print("Lose")