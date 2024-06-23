class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
        l,r,res=0,0,0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l+=1
            hashset.add(s[r])
            res=max(res,len(hashset))
             
        return res  