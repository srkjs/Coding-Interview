# Leetcode question 42 - https://leetcode.com/problems/trapping-rain-water/

# Time - O(n) | Space - O(n), where n is len(height)
def trap(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = [0 for x in height], [0 for x in height]
    leftMax, rightMax = 0, 0
    for i in range(len(height)):
        leftMax = max(leftMax, height[i])
        left[i] = leftMax
    for i in reversed(range(len(height))):
        rightMax = max(rightMax, height[i])
        right[i] = rightMax
        
    res = 0
    for i in range(1, len(height) - 1):
        res += min(left[i], right[i]) - height[i]
    
    return res