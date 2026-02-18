class Solution:
    def search(self, nums: List[int], target: int) -> int:
        list_sorted = sorted(nums)
        start = 0
        end=len(list_sorted)-1
        while(start<=end):
            mid = int((start + end )/2)
            if (list_sorted[mid] == target):
                return mid
            elif (list_sorted[mid]>target):
                end = mid-1
            else:
                start = mid+1
        return -1
