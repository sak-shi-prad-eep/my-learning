from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1=defaultdict(int)
        for num in nums:
            dict1[num]+=1
        dict1=sorted(dict1.items(),key=lambda item:item[1],reverse=True)
        top=[item[0] for item in dict1[:k]]
        return top

        