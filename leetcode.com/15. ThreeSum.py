# Leetcode question 15 - https://leetcode.com/problems/3sum/

# Time - O(n * log(n)) | Space - O(n), where n is len(nums)
def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    res = []
    for i in range(0, len(nums) - 1):
        
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        
        firstNum = nums[i]
        j, k = i + 1, len(nums) - 1
        
        while j < k:
            secondNum = nums[j]
            thirdNum = nums[k]
            threeSum = firstNum + secondNum + thirdNum
            if threeSum == 0:
                res.append([firstNum, secondNum, thirdNum])
                j += 1
                while j < k and nums[j - 1] == nums[j]:
                    j += 1
            elif threeSum > 0:
                k -= 1
            elif threeSum < 0:
                j += 1
    return res