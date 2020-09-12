# Given a non-empty array containing only positive integers, 
# find if the array can be partitioned into two subsets
# such that the sum of elements in both subsets is equal.

class Solution:
    def can_partition(self, arr):
        if sum(arr) % 2 == 0:
            subset_sum = sum(arr) / 2
        else:
            return 0
        return  self._dfs(arr, len(arr) - 1, subset_sum)            

    def _dfs(self, nums, n, subset_sum):
        if subset_sum == 0:
            return True
        
        return self._dfs(nums, n - 1, subset_sum - nums[n - 1]) or self._dfs(nums, n - 1, subset_sum)






s = Solution()
s.can_partition([1, 2, 3, 4, 2]) # true [1,2,3] [4,2]


