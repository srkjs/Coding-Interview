# Leetcode question 11 - https://leetcode.com/problems/container-with-most-water/

# Time - O(n), where n is len(height) | Space - O(1)
def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r = 0, len(height) - 1
    size = 0
    while l < r:
        size = max(size, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return size