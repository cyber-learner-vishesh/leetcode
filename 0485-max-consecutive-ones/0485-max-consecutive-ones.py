class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount=0
        currentCount=0
        for i in range(len(nums)):
            if(nums[i]==1):
                currentCount=currentCount+1
            else:
                maxcount=max(currentCount,maxcount)
                currentCount=0
        maxcount=max(currentCount,maxcount)
        return maxcount
            