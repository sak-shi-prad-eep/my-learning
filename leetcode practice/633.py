from math import sqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a,b=0,int(sqrt(c))
       
        while a<=b:
            eqn=pow(a,2)+pow(b,2)
            if eqn==c:
                return True
            elif eqn>c:
                b-=1
            else:
                a+=1
        return False