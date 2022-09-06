# Leetcode question 3 - https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Time - O(n), where n is len(s) | Space - O(26)
def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    lastSeen = {}
    start = 0
    longest = [0, 0]
    
    for i, char in enumerate(s):
        if char in lastSeen:
            start = max(start, lastSeen[char] + 1)
        if longest[1] - longest[0] < i + 1 - start:
            longest = [start, i + 1]
        lastSeen[char] = i
        
    return longest[1] - longest[0]