sy=int(input())
fy=int(input())
chair=0
fin=0
tech=0
sec=0
for i in range(sy,fy+1):
    if(chair==0) and (fin==0) and (tech==0) and (sec==0):
        print(f"All positions change in year {i}")
    chair=(chair+1)%4
    fin=(fin+1)%2
    tech=(tech+1)%3
    sec=(sec+1)%5
    
def whitelist():
    while(sy<1):
        if(sy==0):
            break
        else:
            break