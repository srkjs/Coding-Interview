# Leetcode question 347 - https://leetcode.com/problems/top-k-frequent-elements/

# Time - O(n * log(n)) | Space - O(n), where n is len(nums)
def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    countDict = dict()
    for num in nums:
        if num not in countDict:
            countDict[num] = 0
        countDict[num] += 1
        
    arr = []
    for key in countDict:
        arr.append([key, countDict[key]])

    arr.sort(key = lambda x : x[1])

    return [x for x,y in arr[len(arr) - k:]]