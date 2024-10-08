class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        result=[1]*length
        prefix=1
        postfix=1
        for i in range(length):
            result[i]=prefix
            prefix=prefix*nums[i]
        for i in range(length-1,-1,-1):
            result[i]*=postfix
            postfix*=nums[i]
        return result