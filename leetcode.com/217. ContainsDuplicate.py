# Leetcode question 217 - https://leetcode.com/problems/contains-duplicate/

# Time - O(n) | Space - O(n), where n is len(nums)
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dic = {}
    for num in nums:
        if num in dic:
            return True
        else:
            dic[num] = True
    return False