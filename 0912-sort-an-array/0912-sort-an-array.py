from typing import List

class Solution:

    def merge(self, start, mid, end, arr):
        temp = []
        left = start
        right = mid + 1

        while left <= mid and right <= end:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

     
        while left <= mid:
            temp.append(arr[left])
            left += 1

    
        while right <= end:
            temp.append(arr[right])
            right += 1

     
        for i in range(len(temp)):
            arr[start + i] = temp[i]

    def divide(self, start, end, arr):
        if start >= end:
            return

        mid = (start + end) // 2

        self.divide(start, mid, arr)
        self.divide(mid + 1, end, arr)
        self.merge(start, mid, end, arr)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.divide(0, len(nums) - 1, nums)
        return nums
