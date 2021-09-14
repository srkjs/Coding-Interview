# O(n) Time | O(n) Space
def twoNumberSum(nums, target):
    dic = {}
    for i in range(len(nums)):
        firstNum = nums[i]
        secondNum = target - firstNum
        if secondNum in dic:
            return [secondNum, firstNum]
        else:
            dic[firstNum] = secondNum
    return []

# O(nlog(n)) Time | O(1) Space 
def twoNumberSum(array, targetSum):
    array.sort()
    i=0
    j=len(array)-1
    while i<=j:
        currSum = array[i]+array[j]
        if currSum == targetSum:	
            return [array[i],array[j]]
        elif currSum < targetSum:
            i+=1
        else:
            j-=1
    return []