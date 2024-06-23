class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_dict={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in hash_dict:
                return [hash_dict[diff],i]
            hash_dict[n]=i