class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = 0 
        second =1
        while second<len(nums):
            if(nums[first]==nums[second]):
                nums.pop(second)
            else:
                second=second+1
                first=second -1
        
        return len(nums)