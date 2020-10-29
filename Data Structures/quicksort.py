# Implementation of Kth Largest Element.
class Solution:
    def findKthLargest(self, nums: List[int], k: int):
        left = 0
        right = len(nums) - 1
        target = right - k
        while left <= right:
            i = left
            for j in range(left, right):
                if nums[j] < nums[right]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[right], nums[i] = nums[i], nums[right]
            if i == target:
                return nums[i]
            if i < target:
                left = i + 1
            else: 
                right = i - 1
        return -1
