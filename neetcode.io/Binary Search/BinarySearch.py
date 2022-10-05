# Leetcode question 76 - https://leetcode.com/problems/minimum-window-substring/

# Time - O(n * log(n)), where n is len(nums) | Space - O(1)
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        currIdx = right - left // 2
        currVal = nums[currIdx]
        if currVal == target:
            return currIdx
        elif currVal > target:
            right = currIdx - 1
        else:
            left = currIdx + 1
    return -1