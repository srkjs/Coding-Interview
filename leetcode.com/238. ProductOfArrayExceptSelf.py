# Leetcode question 238 - https://leetcode.com/problems/product-of-array-except-self/

# Time - O(n), Space - O(n), where n is len(nums)
def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = [1 for num in nums]
    # prefix = 1
    for i in range(1, len(nums)):
        res[i] = res[i - 1] * nums[i - 1]
    
    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] = res[i] * postfix
        postfix *= nums[i]
    
    return res