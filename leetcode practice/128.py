class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      set_nums=set(nums)
      longest=0
      for n in nums:
        if (n-1) not in set_nums:
            length=0
            while (n+length) in set_nums:
                length+=1
            longest=max(longest,length)
      return longest
    
    # class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     nums.sort()
    #     current=1
    #     longest=1
    #     if not nums:
    #         return 0
    #     for i in range(1,len(nums)):
    #         if nums[i] != nums[i - 1]:  
    #             if nums[i] - nums[i - 1] == 1:
    #                 current+= 1
    #             else:
    #                 longest=max(longest,current)
    #                 current=1
    #     longest=max(longest,current)
    #     return longest