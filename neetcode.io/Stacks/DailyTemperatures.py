# Leetcode question 739 - https://leetcode.com/problems/daily-temperatures/

# Efficient Solution
# Time - O(n) | Space - O(n)
def dailyTemperatures(self, temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    stack = []
    res = [0] * len(temperatures)
    
    for i, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            poppedIdx = stack.pop()
            res[poppedIdx] = i - poppedIdx
        stack.append(i)
    
    return res 


# Brute-Force Solution
# Time - O(n * n) | Space - O(1)
def dailyTemperatures(self, temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    def find(idx, temperatures, num):
        if idx == len(temperatures):
            return 0
        
        for i in range(idx, len(temperatures)):
            if temperatures[i] > num:
                return i
        return 0
    
    res = []
    
    for i, num in enumerate(temperatures):
        immediateMaxIdx = find(i + 1, temperatures, num)
        res.append(immediateMaxIdx - i) if immediateMaxIdx > 0 else res.append(0)
    
    return res