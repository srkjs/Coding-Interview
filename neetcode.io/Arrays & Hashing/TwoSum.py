# Leetcode question 1 - https://leetcode.com/problems/two-sum/

# Time - O(n) | Space - O(n), where n is len(nums)
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}
    
    for i,firstnum in enumerate(nums):
        secondNum = target - firstnum
        if secondNum in dic:
            return [i, dic[secondNum]]
        else:
            dic[firstnum] = i