# Leetcode question 189 - https://leetcode.com/problems/rotate-array/

# Time - O(n), where n is len(nums) | Space - O(1)
def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    def reverse(nums, startIdx, endIdx):
        while startIdx < endIdx:
            nums[startIdx], nums[endIdx] = nums[endIdx], nums[startIdx]
            startIdx += 1
            endIdx -= 1
    
    # if k > len(nums)
    # Eg: k = 2, nums = [-1]
    k = k % len(nums)
    
    # [1, 2, 3, 4, 5, 6, 7]
    reverse(nums, 0, len(nums) - 1)
    # [7, 6, 5, 4, 3, 2, 1]
    reverse(nums, 0, k - 1)
    # [5, 6, 7, 4, 3, 2, 1]
    reverse(nums, k, len(nums) - 1)
    # [5, 6, 7, 1, 2, 3, 4]