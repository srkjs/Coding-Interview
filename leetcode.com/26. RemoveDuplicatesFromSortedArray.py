# Leetcode question 26 - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Time - O(n), where n is len(nums) | Space - O(1)
def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 1
    idxToUpdate = 1
    previousValue = nums[0]

    for i in range(1, len(nums)):
        currValue = nums[i]
        if previousValue == currValue:
            continue
        else:
            result += 1
            nums[idxToUpdate] = currValue
            previousValue = currValue
            idxToUpdate += 1
    return result