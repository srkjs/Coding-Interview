# Leetcode question 128 - https://leetcode.com/problems/longest-consecutive-sequence/

# Time - O(n) | Space - O(n), where n is len(nums)
def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ht = {num:False for num in nums}
    longest = 0
    for num in nums:
        if ht[num] is True:
            continue
        currLongest = 1
        ht[num] = True
        left = num - 1
        while left in ht:
            currLongest += 1
            ht[left] = True
            left -= 1
        right = num + 1
        while right in ht:
            currLongest += 1
            ht[right] = True
            right += 1
        longest = max(longest, currLongest)
    
    return longest