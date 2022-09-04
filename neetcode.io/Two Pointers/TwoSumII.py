# Leetcode question 167 - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Time - O(n * log(n)), where n is len(numbers) | Space - O(1)
def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    def TwoNumberSum(array, targetSum):
        i, j = 0, len(array) - 1
        while i < j:
            currSum = array[i] + array[j]
            if currSum < targetSum:
                i += 1
            elif currSum > targetSum:
                j -= 1
            else:
                return [i + 1, j + 1]
    return TwoNumberSum(numbers, target)