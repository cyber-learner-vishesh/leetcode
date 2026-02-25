class Solution:
    def singleNumber(self, nums: List[int]) -> int:
     
        nums.sort()
        xor=0
        for i in range(0 , len(nums)):
            xor = xor^nums[i]
        
        return xor
            